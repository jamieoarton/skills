#!/usr/bin/env python3
"""
Supabase Agent Interface - Clean output for OpenClaw agent use
"""

import sys
import json
from pathlib import Path

# Import from same directory
sys.path.insert(0, str(Path(__file__).parent))

from supabase_client import SupabaseClient


def list_organizations():
    """List organizations (clean output)."""
    try:
        client = SupabaseClient()
        orgs = client.get_organizations()

        for org in orgs:
            print(f"• {org.get('name', 'Unnamed')} (ID: {org['id']})")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def list_projects():
    """List all projects (clean output)."""
    try:
        client = SupabaseClient()
        projects = client.get_projects()

        for project in projects:
            status = project.get('status', 'unknown')
            print(f"• [{status}] {project['name']} - {project['region']} (ID: {project['id']})")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_project_json(project_ref):
    """Get project details as JSON."""
    try:
        client = SupabaseClient()
        project = client.get_project(project_ref)
        print(json.dumps(project, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def check_security(project_ref):
    """
    Check security advisors for a project (clean output).

    Perfect for handling email alerts like:
    "We detected security vulnerabilities in 1 of your projects..."
    """
    try:
        client = SupabaseClient()
        advisors = client.get_security_advisors(project_ref)

        if not advisors:
            print("✓ No security issues found")
            return 0

        # Group by level (ERROR, WARNING, INFO)
        errors = [a for a in advisors if a.get('level') == 'ERROR']
        warnings = [a for a in advisors if a.get('level') == 'WARNING']
        info = [a for a in advisors if a.get('level') == 'INFO']

        print(f"Found {len(advisors)} security issue(s):\n")

        if errors:
            print(f"❌ ERRORS ({len(errors)} issues):")
            for advisor in errors:
                print(f"  • {advisor.get('title', advisor.get('name', 'Unknown issue'))}")
                if advisor.get('detail'):
                    print(f"    {advisor['detail']}")
                if advisor.get('remediation'):
                    print(f"    Fix: {advisor['remediation']}")

        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)} issues):")
            for advisor in warnings:
                print(f"  • {advisor.get('title', advisor.get('name', 'Unknown issue'))}")
                if advisor.get('detail'):
                    print(f"    {advisor['detail'][:100]}...")

        if info:
            print(f"\nℹ️  INFO ({len(info)} issues):")
            for advisor in info:
                print(f"  • {advisor.get('title', advisor.get('name', 'Unknown issue'))}")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_security_json(project_ref):
    """Get security advisors as JSON (for detailed analysis)."""
    try:
        client = SupabaseClient()
        advisors = client.get_security_advisors(project_ref)
        print(json.dumps(advisors, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def check_performance(project_ref):
    """Check performance advisors for a project (clean output)."""
    try:
        client = SupabaseClient()
        advisors = client.get_performance_advisors(project_ref)

        if not advisors:
            print("✓ No performance issues found")
            return 0

        # Group by level (ERROR, WARNING, INFO)
        errors = [a for a in advisors if a.get('level') == 'ERROR']
        warnings = [a for a in advisors if a.get('level') == 'WARNING']
        info = [a for a in advisors if a.get('level') == 'INFO']

        print(f"Found {len(advisors)} performance issue(s):\n")

        if errors:
            print(f"❌ ERRORS ({len(errors)} issues):")
            for advisor in errors:
                print(f"  • {advisor.get('title', advisor.get('name', 'Unknown issue'))}")
                if advisor.get('detail'):
                    print(f"    {advisor['detail']}")
                if advisor.get('remediation'):
                    print(f"    Fix: {advisor['remediation']}")

        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)} issues):")
            for advisor in warnings:
                print(f"  • {advisor.get('title', advisor.get('name', 'Unknown issue'))}")
                if advisor.get('detail'):
                    print(f"    {advisor['detail'][:100]}...")

        if info:
            print(f"\nℹ️  INFO ({len(info)} issues):")
            for advisor in info:
                print(f"  • {advisor.get('title', advisor.get('name', 'Unknown issue'))}")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_performance_json(project_ref):
    """Get performance advisors as JSON (for detailed analysis)."""
    try:
        client = SupabaseClient()
        advisors = client.get_performance_advisors(project_ref)
        print(json.dumps(advisors, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_logs(project_ref, service='postgres', hours=1):
    """Get logs for a service (clean output)."""
    try:
        from datetime import datetime, timedelta

        client = SupabaseClient()

        # Calculate time range
        end = datetime.utcnow()
        start = end - timedelta(hours=hours)

        logs = client.get_logs(
            project_ref=project_ref,
            service=service,
            iso_timestamp_start=start.isoformat() + 'Z',
            iso_timestamp_end=end.isoformat() + 'Z'
        )

        if not logs:
            print(f"No {service} logs found in last {hours} hour(s)")
            return 0

        print(f"Found {len(logs)} {service} log entries (last {hours}h):\n")

        for log in logs[:20]:  # Limit to 20 most recent
            timestamp = log.get('timestamp', 'N/A')
            message = log.get('message', log.get('event_message', 'N/A'))
            # Truncate long messages
            if len(message) > 100:
                message = message[:100] + '...'
            print(f"[{timestamp}] {message}")

        if len(logs) > 20:
            print(f"\n... and {len(logs) - 20} more entries")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def is_read_only_sql(query: str) -> bool:
    """
    Validate that SQL query is read-only (SELECT, EXPLAIN, SHOW, DESCRIBE only).

    Security: Prevents UPDATE, DELETE, INSERT, DROP, ALTER, TRUNCATE, CREATE, etc.
    """
    import re

    # Normalize: strip comments, collapse whitespace, uppercase
    normalized = re.sub(r'--[^\n]*', '', query)  # Remove -- comments
    normalized = re.sub(r'/\*.*?\*/', '', normalized, flags=re.DOTALL)  # Remove /* */ comments
    normalized = re.sub(r'\s+', ' ', normalized).strip().upper()

    # Allowed read-only commands (must be at start after WITH clauses)
    read_only_patterns = [
        r'^WITH\s+.*\s+SELECT\s+',  # CTEs with SELECT
        r'^SELECT\s+',
        r'^EXPLAIN\s+',
        r'^SHOW\s+',
        r'^DESCRIBE\s+',
        r'^DESC\s+',
    ]

    # Check if query starts with allowed pattern
    for pattern in read_only_patterns:
        if re.match(pattern, normalized):
            return True

    return False


def query_database(project_ref, query):
    """Execute a read-only database query (JSON output).

    Security: Only SELECT/EXPLAIN/SHOW/DESCRIBE queries allowed.
    """
    try:
        # Enforce read-only
        if not is_read_only_sql(query):
            print("Error: Only read-only queries (SELECT, EXPLAIN, SHOW, DESCRIBE) are allowed", file=sys.stderr)
            print("For mutations, use the Supabase Management API directly with explicit approval", file=sys.stderr)
            return 1

        client = SupabaseClient()
        result = client.execute_query(project_ref, query)
        print(json.dumps(result, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def whoami():
    """Show current user/organizations."""
    try:
        client = SupabaseClient()
        info = client.get_current_user()
        print(f"Organizations: {info.get('organization_count', 0)}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: supabase_agent.py <command> [args...]")
        print("")
        print("Commands:")
        print("  whoami                              - Show current user info")
        print("  organizations                       - List organizations")
        print("  projects                            - List all projects")
        print("  project <project_ref>               - Get project details (JSON)")
        print("  security <project_ref>              - Check security advisors")
        print("  security-json <project_ref>         - Security advisors (JSON)")
        print("  performance <project_ref>           - Check performance advisors")
        print("  performance-json <project_ref>      - Performance advisors (JSON)")
        print("  logs <project_ref> [service] [hours] - Get logs (default: postgres, 1h)")
        print("  query <project_ref> <sql>           - Execute read-only SQL query (JSON)")
        print("")
        print("Services: postgres, auth, realtime, storage, edge-function")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == 'whoami':
        sys.exit(whoami())

    elif cmd == 'organizations':
        sys.exit(list_organizations())

    elif cmd == 'projects':
        sys.exit(list_projects())

    elif cmd == 'project':
        if len(sys.argv) < 3:
            print("Error: project_ref required", file=sys.stderr)
            sys.exit(1)
        sys.exit(get_project_json(sys.argv[2]))

    elif cmd == 'security':
        if len(sys.argv) < 3:
            print("Error: project_ref required", file=sys.stderr)
            sys.exit(1)
        sys.exit(check_security(sys.argv[2]))

    elif cmd == 'security-json':
        if len(sys.argv) < 3:
            print("Error: project_ref required", file=sys.stderr)
            sys.exit(1)
        sys.exit(get_security_json(sys.argv[2]))

    elif cmd == 'performance':
        if len(sys.argv) < 3:
            print("Error: project_ref required", file=sys.stderr)
            sys.exit(1)
        sys.exit(check_performance(sys.argv[2]))

    elif cmd == 'performance-json':
        if len(sys.argv) < 3:
            print("Error: project_ref required", file=sys.stderr)
            sys.exit(1)
        sys.exit(get_performance_json(sys.argv[2]))

    elif cmd == 'logs':
        if len(sys.argv) < 3:
            print("Error: project_ref required", file=sys.stderr)
            sys.exit(1)
        service = sys.argv[3] if len(sys.argv) > 3 else 'postgres'
        hours = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        sys.exit(get_logs(sys.argv[2], service, hours))

    elif cmd == 'query':
        if len(sys.argv) < 4:
            print("Error: project_ref and SQL query required", file=sys.stderr)
            sys.exit(1)
        sys.exit(query_database(sys.argv[2], sys.argv[3]))

    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)
