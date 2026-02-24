# Common ClickUp Queries

Cookbook of common task management patterns using `clickup_client.py`.

## Find Tasks by Assignee

Get all tasks assigned to a specific user across the workspace.

```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get workspace ID
workspaces = client.get_workspaces()
team_id = workspaces[0]['id']

# Search for tasks assigned to user 123
tasks = client.search_tasks(
    team_id=team_id,
    assignees=[123]
)

print(f"User 123 has {len(tasks)} tasks")

# Print task names
for task in tasks:
    print(f"- {task['name']} (Status: {task['status']['status']})")
```

**Note:** Replace `123` with actual user ID from `get_current_user()` or team members list.

---

## Find Overdue Tasks

Get tasks with due dates in the past.

```python
import time
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get current time in Unix milliseconds
now_ms = int(time.time() * 1000)

# Fetch tasks from a list
tasks = client.get_tasks(list_id='901234', include_closed=False)

# Filter for overdue tasks (client-side filtering)
overdue = [
    task for task in tasks
    if task.get('due_date') and int(task['due_date']) < now_ms
]

print(f"Found {len(overdue)} overdue tasks:")
for task in overdue:
    due = int(task['due_date']) / 1000  # Convert to seconds
    print(f"- {task['name']} (Due: {time.ctime(due)})")
```

**Note:** ClickUp API doesn't have a direct "overdue" filter. Fetch tasks and filter client-side.

---

## Get Tasks by Status

Filter tasks by one or more status names.

```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get tasks in "in progress" or "blocked" status
tasks = client.get_tasks(
    list_id='901234',
    statuses=['in progress', 'blocked']
)

print(f"Found {len(tasks)} tasks in progress or blocked:")
for task in tasks:
    print(f"- {task['name']} (Status: {task['status']['status']})")
```

**Tip:** Use `get_list(list_id)` to see available status names for a list.

---

## Get Recently Updated Tasks

Find tasks modified in the last 7 days.

```python
import time
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Calculate timestamp for 7 days ago
seven_days_ago = int((time.time() - 7 * 24 * 60 * 60) * 1000)

# Get tasks updated since then
tasks = client.get_tasks(
    list_id='901234',
    date_updated_gt=seven_days_ago,
    order_by='updated',
    reverse=True  # Most recent first
)

print(f"Found {len(tasks)} tasks updated in last 7 days:")
for task in tasks:
    updated = int(task['date_updated']) / 1000
    print(f"- {task['name']} (Updated: {time.ctime(updated)})")
```

---

## Get High Priority Tasks

Filter tasks by priority level.

```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get all tasks from list
tasks = client.get_tasks(list_id='901234', include_closed=False)

# Filter for urgent (priority 1) and high (priority 2) tasks
high_priority = [
    task for task in tasks
    if task.get('priority') and task['priority']['priority'] in ['1', '2']
]

print(f"Found {len(high_priority)} high priority tasks:")
for task in high_priority:
    priority = task['priority']['priority']
    priority_name = {'1': 'Urgent', '2': 'High'}[priority]
    print(f"- {task['name']} (Priority: {priority_name})")
```

**Priority levels:**
- `1` = Urgent
- `2` = High
- `3` = Normal
- `4` = Low

---

## Get Tasks with Specific Tags

Find tasks tagged with certain labels.

```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get all tasks from list
tasks = client.get_tasks(list_id='901234', include_closed=False)

# Filter for tasks with "bug" or "urgent" tags
tagged = [
    task for task in tasks
    if any(tag['name'] in ['bug', 'urgent'] for tag in task.get('tags', []))
]

print(f"Found {len(tagged)} tasks with bug/urgent tags:")
for task in tagged:
    tag_names = [tag['name'] for tag in task.get('tags', [])]
    print(f"- {task['name']} (Tags: {', '.join(tag_names)})")
```

---

## Traverse Workspace Hierarchy

Get all lists in a workspace.

```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get workspace
workspaces = client.get_workspaces()
workspace = workspaces[0]
print(f"Workspace: {workspace['name']}")

# Get spaces in workspace
spaces = client.get_spaces(workspace['id'])

all_lists = []

for space in spaces:
    print(f"\nSpace: {space['name']}")

    # Get folders in space
    folders = client.get_folders(space['id'])

    for folder in folders:
        print(f"  Folder: {folder['name']}")

        # Get lists in folder
        lists = client.get_lists(folder['id'])
        all_lists.extend(lists)

        for list_obj in lists:
            print(f"    List: {list_obj['name']}")

    # Get folderless lists (directly in space)
    folderless = client.get_folderless_lists(space['id'])
    all_lists.extend(folderless)

    for list_obj in folderless:
        print(f"  List (no folder): {list_obj['name']}")

print(f"\nTotal lists found: {len(all_lists)}")
```

---

## Get Task Count by Status

Count tasks grouped by status.

```python
from collections import Counter
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get all tasks from list
tasks = client.get_tasks(list_id='901234', include_closed=True)

# Count by status
status_counts = Counter(
    task['status']['status'] for task in tasks
)

print(f"Task count by status:")
for status, count in status_counts.most_common():
    print(f"- {status}: {count}")
```

---

## Get My Assigned Tasks Across All Lists

Find all tasks assigned to current user.

```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get current user ID
user = client.get_current_user()
user_id = user['id']

# Get workspace
workspaces = client.get_workspaces()
team_id = workspaces[0]['id']

# Search for tasks assigned to me
my_tasks = client.search_tasks(
    team_id=team_id,
    assignees=[user_id],
    include_closed=False
)

print(f"You have {len(my_tasks)} open tasks:")
for task in my_tasks:
    print(f"- {task['name']} (Status: {task['status']['status']})")
```

---

## Create Task with Full Details (Requires Approval)

Example of creating a task with all fields.

```python
from scripts.clickup_client import ClickUpClient
import time

client = ClickUpClient()

# IMPORTANT: Agent should request approval before calling this

# Create task with full details
new_task = client.create_task(
    list_id='901234',
    name='Implement user authentication',
    description='Add OAuth2 login flow with Google and GitHub providers',
    assignees=[123, 456],  # User IDs
    tags=['backend', 'security'],
    status='in progress',
    priority=2,  # High priority
    due_date=int((time.time() + 7 * 24 * 60 * 60) * 1000)  # Due in 7 days
)

print(f"Created task: {new_task['name']}")
print(f"Task ID: {new_task['id']}")
print(f"URL: {new_task['url']}")
```

**Security:** Write operations require human approval. Agent should ask before creating tasks.

---

## Performance Tips

### 1. Cache Workspace/Space/List IDs

Don't fetch hierarchy every time:

```python
# ❌ Inefficient - fetches workspace every call
def get_my_tasks_slow():
    client = ClickUpClient()
    workspaces = client.get_workspaces()  # API call
    team_id = workspaces[0]['id']
    return client.search_tasks(team_id=team_id, assignees=[123])

# ✅ Efficient - cache workspace ID
WORKSPACE_ID = '9876'  # Fetch once, store in config

def get_my_tasks_fast():
    client = ClickUpClient()
    return client.search_tasks(team_id=WORKSPACE_ID, assignees=[123])
```

### 2. Use Filters to Reduce Response Size

```python
# ❌ Fetches all tasks, filters client-side
tasks = client.get_tasks(list_id='901234')
open_tasks = [t for t in tasks if t['status']['status'] != 'closed']

# ✅ Filters server-side
tasks = client.get_tasks(list_id='901234', include_closed=False)
```

### 3. Paginate Large Result Sets

```python
# Get first 100 tasks (page 0)
page_0 = client.get_tasks(list_id='901234', page=0)

# Get next 100 tasks (page 1)
page_1 = client.get_tasks(list_id='901234', page=1)
```

---

## Next Steps

- See [api-reference.md](api-reference.md) for complete method documentation
- See [error-handling.md](error-handling.md) for error handling patterns
- See [security-model.md](security-model.md) for security best practices
