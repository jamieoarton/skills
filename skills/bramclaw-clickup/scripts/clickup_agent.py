#!/usr/bin/env python3
"""
ClickUp Agent Interface - Clean output for OpenClaw agent use
"""

import sys
import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import os
from clickup_client import ClickUpClient


def resolve_scope(requested_scope):
    """Resolve account scope for ClickUp operations."""
    default_scope = os.environ.get('CLICKUP_DEFAULT_SCOPE', 'principal').strip().lower()
    scope = (requested_scope or 'auto').strip().lower()
    if scope == 'auto':
        scope = default_scope if default_scope in ('principal', 'assistant') else 'principal'
    if scope not in ('principal', 'assistant'):
        raise ValueError("scope must be one of: principal, assistant, auto")
    return scope


def resolve_api_key_for_scope(scope):
    """Select API key by account scope with safe fallbacks."""
    primary = os.environ.get('CLICK_UP_API_KEY', '').strip()
    principal = os.environ.get('CLICK_UP_API_KEY_PRINCIPAL', '').strip()
    assistant = os.environ.get('CLICK_UP_API_KEY_ASSISTANT', '').strip()

    if scope == 'principal':
        return principal or primary
    if scope == 'assistant':
        return assistant or primary
    return primary


def get_client(scope='auto'):
    """Build ClickUp client for the requested scope."""
    resolved_scope = resolve_scope(scope)
    api_key = resolve_api_key_for_scope(resolved_scope)
    if not api_key:
        raise ValueError(
            f"No ClickUp API key available for scope '{resolved_scope}'. "
            "Set CLICK_UP_API_KEY, CLICK_UP_API_KEY_PRINCIPAL, or CLICK_UP_API_KEY_ASSISTANT."
        )
    return ClickUpClient(api_key=api_key), resolved_scope


def due_today(scope='auto', limit=50):
    """List tasks due today in configured timezone for the selected account scope."""
    try:
        client, resolved_scope = get_client(scope)
        tz_name = os.environ.get('CLICKUP_TIMEZONE', 'UTC')
        tz = ZoneInfo(tz_name)
        now_local = datetime.now(tz)
        day_start = now_local.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = now_local.replace(hour=23, minute=59, second=59, microsecond=999000)
        start_utc_ms = int(day_start.astimezone(timezone.utc).timestamp() * 1000)
        end_utc_ms = int(day_end.astimezone(timezone.utc).timestamp() * 1000)

        workspaces = client.get_workspaces()
        if not workspaces:
            print(f"No ClickUp workspaces visible for scope '{resolved_scope}'.")
            return 0

        team_id = str(workspaces[0]['id'])
        page = 0
        found = []
        max_pages = 10

        while page < max_pages and len(found) < limit:
            tasks = client.search_tasks(team_id=team_id, page=page, order_by='due_date')
            if not tasks:
                break

            for task in tasks:
                due_raw = task.get('due_date')
                if not due_raw:
                    continue
                due_ms = int(due_raw)
                if start_utc_ms <= due_ms <= end_utc_ms:
                    found.append(task)
                    if len(found) >= limit:
                        break
            page += 1

        print(f"Scope: {resolved_scope}")
        print(f"Date: {now_local.date().isoformat()} ({tz_name})")
        print(f"Team: {workspaces[0]['name']} (ID: {team_id})")
        print(f"Tasks due today: {len(found)}")

        for task in found:
            due_iso = datetime.fromtimestamp(
                int(task['due_date']) / 1000, tz=timezone.utc
            ).astimezone(tz).isoformat()
            assignees = task.get('assignees', [])
            owners = []
            for assignee in assignees:
                owners.append(
                    assignee.get('username') or assignee.get('email') or str(assignee.get('id'))
                )
            owner_text = ", ".join(owners) if owners else "unassigned"
            status = task.get('status', {}).get('status', 'no status')
            print(
                f"• [{status}] {task.get('name', '(unnamed task)')} "
                f"(ID: {task.get('id')}, due: {due_iso}, owner: {owner_text})"
            )

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def list_workspaces():
    """List workspaces (clean output)."""
    try:
        client, _ = get_client('auto')
        workspaces = client.get_workspaces()

        for workspace in workspaces:
            print(f"• {workspace['name']} (ID: {workspace['id']})")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def list_spaces(team_id):
    """List spaces in workspace (clean output)."""
    try:
        client, _ = get_client('auto')
        spaces = client.get_spaces(team_id)

        for space in spaces:
            print(f"• {space['name']} (ID: {space['id']})")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def list_lists(space_id):
    """List folderless lists in space (clean output)."""
    try:
        client, _ = get_client('auto')
        # Get lists directly in space (not in folders)
        lists = client.get_folderless_lists(space_id)

        if not lists:
            print(f"No lists found in space {space_id}")
            print("Note: This only shows folderless lists. Use 'folders <space_id>' to find lists in folders.")
            return 0

        for lst in lists:
            print(f"• {lst['name']} (ID: {lst['id']})")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def list_tasks(list_id, limit=10):
    """List tasks in list (clean output)."""
    try:
        client, _ = get_client('auto')
        tasks = client.get_tasks(list_id, page=0, order_by='updated', reverse=True)

        # Limit results
        tasks = tasks[:limit]

        for task in tasks:
            status = task.get('status', {}).get('status', 'No status')
            print(f"• [{status}] {task['name']} (ID: {task['id']})")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_task_json(task_id):
    """Get task details as JSON."""
    try:
        client, _ = get_client('auto')
        task = client.get_task(task_id)
        print(json.dumps(task, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def search_tasks_by_name(team_id, query, limit=10):
    """Search tasks by name (clean output)."""
    try:
        client, _ = get_client('auto')
        query_lower = query.strip().lower()
        tasks = []
        page = 0
        max_pages = 10
        while page < max_pages and len(tasks) < limit:
            page_tasks = client.search_tasks(team_id=team_id, page=page, order_by='updated')
            if not page_tasks:
                break
            for task in page_tasks:
                if query_lower in task.get('name', '').lower():
                    tasks.append(task)
                    if len(tasks) >= limit:
                        break
            page += 1

        if not tasks:
            print(f"No tasks found matching '{query}'")
            return 0

        for task in tasks:
            list_name = task.get('list', {}).get('name', 'Unknown list')
            status = task.get('status', {}).get('status', 'No status')
            print(f"• [{status}] {task['name']} (in {list_name}) - ID: {task['id']}")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def whoami():
    """Get current user info (clean output)."""
    try:
        client, resolved_scope = get_client('auto')
        user = client.get_current_user()
        print(f"{user.get('username')} ({user.get('email')}) [scope={resolved_scope}]")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def create_task_cmd(list_id, name, scope='auto', description=None, assignees=None,
                    status=None, priority=None, due_date=None, tags=None):
    """
    Create a task in ClickUp.

    Args:
        list_id: List ID to create task in
        name: Task name
        scope: Account scope (principal|assistant|auto)
        description: Task description
        assignees: Comma-separated user IDs
        status: Status name
        priority: 1=urgent, 2=high, 3=normal, 4=low
        due_date: Unix timestamp in milliseconds OR 'today'
        tags: Comma-separated tag names
    """
    try:
        client, resolved_scope = get_client(scope)

        # Parse assignees
        assignee_list = None
        if assignees:
            assignee_list = [int(a.strip()) for a in assignees.split(',')]

        # Parse tags
        tag_list = None
        if tags:
            tag_list = [t.strip() for t in tags.split(',')]

        # Parse due_date
        due_date_ms = None
        if due_date:
            if due_date.lower() == 'today':
                # Get end of today in configured timezone
                tz_name = os.environ.get('CLICKUP_TIMEZONE', 'UTC')
                tz = ZoneInfo(tz_name)
                now_local = datetime.now(tz)
                day_end = now_local.replace(hour=23, minute=59, second=59, microsecond=999000)
                due_date_ms = int(day_end.astimezone(timezone.utc).timestamp() * 1000)
            else:
                due_date_ms = int(due_date)

        # Parse priority
        priority_int = None
        if priority:
            priority_int = int(priority)

        # Create task
        task = client.create_task(
            list_id=list_id,
            name=name,
            description=description,
            assignees=assignee_list,
            status=status,
            priority=priority_int,
            due_date=due_date_ms,
            tags=tag_list
        )

        print(f"✓ Task created successfully")
        print(f"Task ID: {task['id']}")
        print(f"Name: {task['name']}")
        print(f"URL: {task.get('url', 'N/A')}")
        print(f"Scope: {resolved_scope}")

        return 0
    except Exception as e:
        print(f"Error creating task: {e}", file=sys.stderr)
        return 1


def update_task_cmd(task_id, scope='auto', name=None, description=None,
                    status=None, priority=None, assignees=None):
    """
    Update an existing task.

    Args:
        task_id: Task ID to update
        scope: Account scope (principal|assistant|auto)
        name: New task name
        description: New description
        status: New status
        priority: New priority (1-4)
        assignees: Comma-separated user IDs
    """
    try:
        client, resolved_scope = get_client(scope)

        # Parse assignees
        assignee_list = None
        if assignees:
            assignee_list = [int(a.strip()) for a in assignees.split(',')]

        # Parse priority
        priority_int = None
        if priority:
            priority_int = int(priority)

        # Update task
        task = client.update_task(
            task_id=task_id,
            name=name,
            description=description,
            status=status,
            priority=priority_int,
            assignees=assignee_list
        )

        print(f"✓ Task updated successfully")
        print(f"Task ID: {task['id']}")
        print(f"Name: {task['name']}")
        print(f"Status: {task.get('status', {}).get('status', 'N/A')}")
        print(f"Scope: {resolved_scope}")

        return 0
    except Exception as e:
        print(f"Error updating task: {e}", file=sys.stderr)
        return 1


def delete_task_cmd(task_id, scope='auto', confirm=False):
    """
    Delete a task (requires confirmation).

    Args:
        task_id: Task ID to delete
        scope: Account scope (principal|assistant|auto)
        confirm: Must be True to actually delete
    """
    try:
        client, resolved_scope = get_client(scope)

        if not confirm:
            # Get task details to show what would be deleted
            task = client.get_task(task_id)
            print("⚠️  WARNING: Deletion requires confirmation")
            print(f"Task to delete: {task['name']} (ID: {task_id})")
            print(f"Status: {task.get('status', {}).get('status', 'N/A')}")
            print("\nTo confirm deletion, add --confirm flag")
            return 1

        # Delete task
        client.delete_task(task_id)

        print(f"✓ Task deleted successfully")
        print(f"Task ID: {task_id}")
        print(f"Scope: {resolved_scope}")

        return 0
    except Exception as e:
        print(f"Error deleting task: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: clickup_agent.py <command> [args...]")
        print("")
        print("Read Commands:")
        print("  whoami                      - Show current user")
        print("  workspaces                  - List workspaces")
        print("  spaces <team_id>            - List spaces in workspace")
        print("  lists <space_id>            - List lists in space")
        print("  tasks <list_id> [limit]     - List tasks in list")
        print("  task <task_id>              - Get task details (JSON)")
        print("  search <team_id> <query> [limit] - Search tasks")
        print("  due-today [scope] [limit]   - List tasks due today")
        print("")
        print("Write Commands (require authorization):")
        print("  create-task <list_id> <name> [options]")
        print("    --scope <principal|assistant|auto>")
        print("    --description <text>")
        print("    --assignees <user_id1,user_id2,...>")
        print("    --status <status_name>")
        print("    --priority <1-4>  (1=urgent, 2=high, 3=normal, 4=low)")
        print("    --due <timestamp_ms|today>")
        print("    --tags <tag1,tag2,...>")
        print("")
        print("  update-task <task_id> [options]")
        print("    --scope <principal|assistant|auto>")
        print("    --name <new_name>")
        print("    --description <text>")
        print("    --status <status_name>")
        print("    --priority <1-4>")
        print("    --assignees <user_id1,user_id2,...>")
        print("")
        print("  delete-task <task_id> [--scope <scope>] [--confirm]")
        print("    ⚠️  Requires --confirm flag for safety")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == 'whoami':
        sys.exit(whoami())

    elif cmd == 'workspaces':
        sys.exit(list_workspaces())

    elif cmd == 'spaces':
        if len(sys.argv) < 3:
            print("Error: team_id required", file=sys.stderr)
            sys.exit(1)
        sys.exit(list_spaces(sys.argv[2]))

    elif cmd == 'lists':
        if len(sys.argv) < 3:
            print("Error: space_id required", file=sys.stderr)
            sys.exit(1)
        sys.exit(list_lists(sys.argv[2]))

    elif cmd == 'tasks':
        if len(sys.argv) < 3:
            print("Error: list_id required", file=sys.stderr)
            sys.exit(1)
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        sys.exit(list_tasks(sys.argv[2], limit))

    elif cmd == 'task':
        if len(sys.argv) < 3:
            print("Error: task_id required", file=sys.stderr)
            sys.exit(1)
        sys.exit(get_task_json(sys.argv[2]))

    elif cmd == 'search':
        if len(sys.argv) < 4:
            print("Error: team_id and query required", file=sys.stderr)
            sys.exit(1)
        limit = int(sys.argv[4]) if len(sys.argv) > 4 else 10
        sys.exit(search_tasks_by_name(sys.argv[2], sys.argv[3], limit))

    elif cmd == 'due-today':
        scope = sys.argv[2] if len(sys.argv) > 2 else 'auto'
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 50
        sys.exit(due_today(scope, limit))

    elif cmd == 'create-task':
        if len(sys.argv) < 4:
            print("Error: create-task requires <list_id> <name>", file=sys.stderr)
            sys.exit(1)

        list_id = sys.argv[2]
        name = sys.argv[3]

        # Parse optional arguments
        scope = 'auto'
        description = None
        assignees = None
        status = None
        priority = None
        due_date = None
        tags = None

        i = 4
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg == '--scope' and i + 1 < len(sys.argv):
                scope = sys.argv[i + 1]
                i += 2
            elif arg == '--description' and i + 1 < len(sys.argv):
                description = sys.argv[i + 1]
                i += 2
            elif arg == '--assignees' and i + 1 < len(sys.argv):
                assignees = sys.argv[i + 1]
                i += 2
            elif arg == '--status' and i + 1 < len(sys.argv):
                status = sys.argv[i + 1]
                i += 2
            elif arg == '--priority' and i + 1 < len(sys.argv):
                priority = sys.argv[i + 1]
                i += 2
            elif arg == '--due' and i + 1 < len(sys.argv):
                due_date = sys.argv[i + 1]
                i += 2
            elif arg == '--tags' and i + 1 < len(sys.argv):
                tags = sys.argv[i + 1]
                i += 2
            else:
                i += 1

        sys.exit(create_task_cmd(
            list_id=list_id,
            name=name,
            scope=scope,
            description=description,
            assignees=assignees,
            status=status,
            priority=priority,
            due_date=due_date,
            tags=tags
        ))

    elif cmd == 'update-task':
        if len(sys.argv) < 3:
            print("Error: update-task requires <task_id>", file=sys.stderr)
            sys.exit(1)

        task_id = sys.argv[2]

        # Parse optional arguments
        scope = 'auto'
        name = None
        description = None
        status = None
        priority = None
        assignees = None

        i = 3
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg == '--scope' and i + 1 < len(sys.argv):
                scope = sys.argv[i + 1]
                i += 2
            elif arg == '--name' and i + 1 < len(sys.argv):
                name = sys.argv[i + 1]
                i += 2
            elif arg == '--description' and i + 1 < len(sys.argv):
                description = sys.argv[i + 1]
                i += 2
            elif arg == '--status' and i + 1 < len(sys.argv):
                status = sys.argv[i + 1]
                i += 2
            elif arg == '--priority' and i + 1 < len(sys.argv):
                priority = sys.argv[i + 1]
                i += 2
            elif arg == '--assignees' and i + 1 < len(sys.argv):
                assignees = sys.argv[i + 1]
                i += 2
            else:
                i += 1

        sys.exit(update_task_cmd(
            task_id=task_id,
            scope=scope,
            name=name,
            description=description,
            status=status,
            priority=priority,
            assignees=assignees
        ))

    elif cmd == 'delete-task':
        if len(sys.argv) < 3:
            print("Error: delete-task requires <task_id>", file=sys.stderr)
            sys.exit(1)

        task_id = sys.argv[2]

        # Parse optional arguments
        scope = 'auto'
        confirm = False

        i = 3
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg == '--scope' and i + 1 < len(sys.argv):
                scope = sys.argv[i + 1]
                i += 2
            elif arg == '--confirm':
                confirm = True
                i += 1
            else:
                i += 1

        sys.exit(delete_task_cmd(
            task_id=task_id,
            scope=scope,
            confirm=confirm
        ))

    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)
