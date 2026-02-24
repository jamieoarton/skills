# API Operations Reference

Complete API reference for Supabase Management API operations.

---

## Read Operations ✅

Safe for agent use without approval.

---

### get_current_user()

Get information about the authenticated user.

**Returns:** User information including organizations

**Example:**
```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()
user = client.get_current_user()

print(f"Organizations: {len(user.get('organizations', []))}")
```

**CLI:**
```bash
python3 scripts/supabase_agent.py whoami
```

---

### get_projects()

List all projects across all organizations.

**Returns:** List of project objects

**Project Object:**
```json
{
  "id": "ovrxdoyvkyrczsxhvada",
  "name": "skool-goose-dev",
  "organization_id": "abc123",
  "region": "us-east-1",
  "status": "ACTIVE_HEALTHY",
  "created_at": "2026-01-15T10:30:00Z"
}
```

**Example:**
```python
projects = client.get_projects()

for project in projects:
    print(f"• [{project['status']}] {project['name']} - {project['region']}")
    print(f"  ID: {project['id']}")
```

**CLI:**
```bash
python3 scripts/supabase_agent.py projects
```

---

### get_security_advisors(project_id)

Get security advisor lints for a project.

**Parameters:**
- `project_id` (str): Project ID (e.g., "ovrxdoyvkyrczsxhvada")

**Returns:** List of security advisor objects

**Advisor Object:**
```json
{
  "name": "rls_disabled_in_public",
  "title": "RLS Disabled in Public",
  "level": "ERROR",
  "categories": ["SECURITY"],
  "description": "Tables in public schema should have RLS enabled",
  "detail": "Table `public.users` is public, but RLS has not been enabled",
  "remediation": "https://supabase.com/docs/guides/database/...",
  "metadata": {
    "schema": "public",
    "name": "users",
    "table_id": 12345
  }
}
```

**Example:**
```python
advisors = client.get_security_advisors('ovrxdoyvkyrczsxhvada')

# Filter ERROR-level issues
errors = [a for a in advisors if a.get('level') == 'ERROR']
print(f"Found {len(errors)} critical security issues")

# Group by type
from collections import Counter
issue_types = Counter(a['name'] for a in errors)
for issue, count in issue_types.most_common():
    print(f"  {issue}: {count}")
```

**CLI:**
```bash
# Human-readable output
python3 scripts/supabase_agent.py security ovrxdoyvkyrczsxhvada

# JSON output
python3 scripts/supabase_agent.py security-json ovrxdoyvkyrczsxhvada
```

---

### get_performance_advisors(project_id)

Get performance advisor lints for a project.

**Parameters:**
- `project_id` (str): Project ID

**Returns:** List of performance advisor objects

**Example:**
```python
advisors = client.get_performance_advisors('ovrxdoyvkyrczsxhvada')

# Filter for unindexed foreign keys
fk_issues = [a for a in advisors if 'foreign' in a.get('name', '').lower()]
print(f"Found {len(fk_issues)} unindexed foreign keys")
```

**CLI:**
```bash
# Human-readable output
python3 scripts/supabase_agent.py performance ovrxdoyvkyrczsxhvada

# JSON output
python3 scripts/supabase_agent.py performance-json ovrxdoyvkyrczsxhvada
```

---

### get_logs(project_id, service, iso_timestamp_start, iso_timestamp_end)

Get logs for a specific service.

**Parameters:**
- `project_id` (str): Project ID
- `service` (str): Service name (`postgres`, `auth`, `realtime`, `storage`, `edge-function`)
- `iso_timestamp_start` (str): Start time in ISO format (e.g., "2026-02-21T00:00:00Z")
- `iso_timestamp_end` (str): End time in ISO format

**Returns:** List of log entries

**Log Entry:**
```json
{
  "timestamp": "2026-02-21T10:30:45.123Z",
  "message": "SELECT * FROM users WHERE id = $1",
  "level": "INFO",
  "metadata": {
    "query_duration_ms": 12.5
  }
}
```

**Example:**
```python
from datetime import datetime, timedelta

# Get postgres logs from last 24 hours
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=24)

logs = client.get_logs(
    'ovrxdoyvkyrczsxhvada',
    service='postgres',
    iso_timestamp_start=start_time.isoformat() + 'Z',
    iso_timestamp_end=end_time.isoformat() + 'Z'
)

# Filter for errors
errors = [l for l in logs if 'ERROR' in l.get('message', '')]
print(f"Found {len(errors)} error log entries")
```

**CLI:**
```bash
# Get postgres logs (last 1 hour)
python3 scripts/supabase_agent.py logs ovrxdoyvkyrczsxhvada postgres 1

# Get auth logs (last 24 hours)
python3 scripts/supabase_agent.py logs ovrxdoyvkyrczsxhvada auth 24
```

**Supported Services:**
- `postgres` - Database logs
- `auth` - Authentication logs
- `realtime` - Realtime subscription logs
- `storage` - Storage operation logs
- `edge-function` - Edge function execution logs

**Limitations:**
- Max 24-hour time range per request
- Logs older than 7 days may not be available (free tier)

---

### execute_query(project_id, query)

Execute a read-only SQL query against the database.

**Parameters:**
- `project_id` (str): Project ID
- `query` (str): SQL query (SELECT, EXPLAIN, SHOW, DESCRIBE only)

**Returns:** Query results

**Allowed Queries:**
- `SELECT` - Read data
- `EXPLAIN` - Analyze query plans
- `SHOW` - Show settings
- `DESCRIBE` - Describe tables

**Blocked Queries:**
- `INSERT`, `UPDATE`, `DELETE` - Data modification
- `CREATE`, `ALTER`, `DROP` - DDL operations
- `GRANT`, `REVOKE` - Permission changes

**Example:**
```python
# Get user count
result = client.execute_query(
    'ovrxdoyvkyrczsxhvada',
    'SELECT COUNT(*) FROM users'
)
print(f"User count: {result}")

# Get recent signups
result = client.execute_query(
    'ovrxdoyvkyrczsxhvada',
    "SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL '7 days'"
)
print(f"New users (7d): {result}")

# Check table sizes
result = client.execute_query(
    'ovrxdoyvkyrczsxhvada',
    """
    SELECT
      schemaname,
      tablename,
      pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
    FROM pg_tables
    WHERE schemaname = 'public'
    ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
    """
)
```

**CLI:**
```bash
python3 scripts/supabase_agent.py query ovrxdoyvkyrczsxhvada "SELECT COUNT(*) FROM users"
```

---

## Write Operations ⚠️

Require human approval before execution.

---

### create_project(organization_id, name, db_pass, region, plan)

Create a new Supabase project.

**⚠️ REQUIRES APPROVAL:** Billable resource creation

**Parameters:**
- `organization_id` (str): Organization ID
- `name` (str): Project name
- `db_pass` (str): Database password (min 12 characters)
- `region` (str): AWS region (e.g., "us-east-1")
- `plan` (str): Plan tier ("free", "pro", "team", "enterprise")

**Returns:** Project object

**Example:**
```python
# REQUIRES HUMAN APPROVAL
project = client.create_project(
    organization_id='abc123',
    name='my-new-project',
    db_pass='super-secret-password-123',
    region='us-east-1',
    plan='free'
)

print(f"Created project: {project['name']} (ID: {project['id']})")
```

**Approval Required Because:**
- Creates billable resource
- Consumes organization quota
- Irreversible without manual deletion

---

### pause_project(project_id)

Pause a project (suspends all services).

**⚠️ REQUIRES APPROVAL:** Service interruption

**Parameters:**
- `project_id` (str): Project ID

**Returns:** Status confirmation

**Example:**
```python
# REQUIRES HUMAN APPROVAL
client.pause_project('ovrxdoyvkyrczsxhvada')
print("Project paused - all services stopped")
```

**Approval Required Because:**
- Interrupts service for users
- Disconnects database connections
- May cause data loss if transactions in progress

---

### restore_project(project_id)

Restore a paused project.

**⚠️ REQUIRES APPROVAL:** Service state change

**Parameters:**
- `project_id` (str): Project ID

**Returns:** Status confirmation

**Example:**
```python
# REQUIRES HUMAN APPROVAL
client.restore_project('ovrxdoyvkyrczsxhvada')
print("Project restored - services starting")
```

**Approval Required Because:**
- Changes service state
- May incur costs
- Takes time to fully restore

---

### execute_migration(project_id, name, sql)

Apply a database migration.

**⚠️ REQUIRES APPROVAL:** DDL changes to database

**Parameters:**
- `project_id` (str): Project ID
- `name` (str): Migration name
- `sql` (str): SQL statements (CREATE, ALTER, DROP)

**Returns:** Migration result

**Example:**
```python
# REQUIRES HUMAN APPROVAL
result = client.execute_migration(
    'ovrxdoyvkyrczsxhvada',
    'add_users_table',
    '''
    CREATE TABLE users (
      id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
      email TEXT UNIQUE NOT NULL,
      created_at TIMESTAMPTZ DEFAULT NOW()
    );

    ALTER TABLE users ENABLE ROW LEVEL SECURITY;
    '''
)
```

**Approval Required Because:**
- Modifies database schema
- Irreversible (requires rollback migration)
- Can cause data loss if DROP used
- Can break application if schema changes

---

## Common Use Cases

### 1. Daily Security Check

```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()

# Get all projects
projects = client.get_projects()

for project in projects:
    # Check security
    advisors = client.get_security_advisors(project['id'])
    errors = [a for a in advisors if a.get('level') == 'ERROR']

    if errors:
        print(f"⚠️  {project['name']}: {len(errors)} critical issues")
```

### 2. Database Health Check

```python
# Check table row counts
tables = ['users', 'posts', 'comments']

for table in tables:
    result = client.execute_query(
        'ovrxdoyvkyrczsxhvada',
        f'SELECT COUNT(*) FROM {table}'
    )
    print(f"{table}: {result}")
```

### 3. Log Analysis

```python
from datetime import datetime, timedelta

# Get error logs
end = datetime.utcnow()
start = end - timedelta(hours=24)

logs = client.get_logs(
    'ovrxdoyvkyrczsxhvada',
    'postgres',
    start.isoformat() + 'Z',
    end.isoformat() + 'Z'
)

errors = [l for l in logs if 'ERROR' in l.get('message', '')]
print(f"Errors in last 24h: {len(errors)}")
```

---

## Resources

- **Management API Docs:** https://supabase.com/docs/reference/api/introduction
- **Project Management:** https://supabase.com/docs/guides/deployment/projects
- **Migrations:** https://supabase.com/docs/guides/cli/migrations

---

**Last updated:** 2026-02-21
