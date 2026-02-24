---
name: bramclaw-supabase
description: Use when users ask to inspect Supabase projects, logs, security advisors, or management API operations for database and platform monitoring tasks.
---

**Version:** 2.0.0 | [Changelog](CHANGELOG.md) | **Status:** ✅ Production

---

# bramclaw-supabase

Supabase Management API integration for project management, security monitoring, and database operations.

## When This Skill Should Trigger

**✅ Should trigger for:**
- "Check Supabase security advisors for my project"
- "Get logs from Supabase project"
- "List my Supabase projects"
- "Handle this security alert email" (if mentions Supabase)
- "Query database table count"
- "Show performance advisors"

**❌ Should NOT trigger for:**
- "Deploy to Firebase" (different service)
- "Check AWS RDS" (different database service)
- "Create Vercel project" (different platform)
- "Run database migration" (ambiguous - needs Supabase context)

**⚠️ Ambiguous (ask for clarification):**
- "Check security advisors" (Supabase? AWS? Other?)
- "Get project logs" (Supabase? Vercel? Other?)
- "Query database" (Supabase? Direct PostgreSQL? Other?)

## Skill Confidence

**High confidence (>90%):**
- Explicit "Supabase" mention
- "security advisors" + database context
- "performance advisors"
- Supabase security alert email

**Medium confidence (50-90%):**
- Generic "project logs" without service specified
- "database query" without Supabase context

**Low confidence (<50%):**
- Generic "security" or "monitoring"
- No database/platform context

---

## Success Metrics

See: [references/success-metrics.md](references/success-metrics.md) for detailed measurement framework.

**Key Targets:**
- **Triggering accuracy:** >90%
- **Token reduction:** >65% (15K → <5K tokens)
- **API efficiency:** 1 call vs. 8-13 exploratory calls
- **Security alert response:** <3 minutes (vs. 20 min manual)

**Current Performance:**
- Triggering: Not yet measured (baseline needed)
- Tokens: ~5K with skill vs. ~15K without (67% reduction ✅)
- API calls: 1 vs. 10 (90% reduction ✅)
- Security: 100% approval workflow ✅

---

## When to Use This Skill

**Decision Framework:**

```plaintext
Need Supabase operations?
    ├─ Security/performance monitoring? → Use bramclaw-supabase ✅
    ├─ Project management (list/logs)? → Use bramclaw-supabase ✅
    ├─ Complex migrations/branching? → Consider Supabase CLI or MCP
    └─ Visual dashboard needed? → Use Supabase UI
```

**Use bramclaw-supabase when:**
- ✅ Security advisor monitoring (email alerts)
- ✅ Quick project queries (list/status)
- ✅ Log analysis (errors, auth events)
- ✅ Read-only database queries
- ✅ Agent needs project access

**Use Supabase CLI when:**
- Complex migrations with multiple files
- Database branching workflows
- Local development setup

**Use Supabase Dashboard when:**
- Visual project setup
- Complex RLS policy creation
- Reporting and analytics

**Alternatives Comparison:**

| Need | bramclaw-supabase | Supabase UI | Supabase CLI | Supabase MCP |
|------|-------------------|-------------|--------------|--------------|
| **Security monitoring** | ✅ Best | ⚠️ Manual | ❌ No | ⚠️ Complex |
| **Email alert handling** | ✅ Yes | ⚠️ Manual | ❌ No | ⚠️ Complex |
| **Project logs** | ✅ Best | ⚠️ Manual | ❌ No | ✅ Yes |
| **Agent-friendly** | ✅ Yes | ❌ No | ⚠️ Shell | ✅ Yes |
| **Setup complexity** | ✅ Low (token) | ✅ Easy | ⚠️ Medium | ⚠️ Medium |

---

## Security Model

**Defense in Depth:**
- **Layer 1:** Direct API (no third-party proxy)
- **Layer 2:** Code-level controls (write methods clearly marked)
- **Layer 3:** Human approval (agent asks before writes)
- **Layer 4:** Monitoring (log all operations)

See: [references/security-advisors.md](references/security-advisors.md) for security monitoring details.

**What Agent Can Do (Safe ✅):**
- List organizations and projects
- Get security/performance advisors
- Get logs (postgres, auth, realtime, storage)
- Execute read-only queries (SELECT/EXPLAIN/SHOW)
- Monitor project health

**What Requires Approval (⚠️):**
- Create projects (billable resource)
- Pause/restore projects (service interruption)
- Execute migrations (DDL changes)

**Security Features:**
- ✅ Direct API access (no third-party proxy)
- ✅ Personal Access Token from environment
- ✅ No shell execution (Python module import)
- ✅ Read operations safe for agent use
- ⚠️ Write operations require human approval

---

## Setup

**Already configured.** `SUPABASE_ACCESS_TOKEN` is injected into the OpenClaw container via Docker Compose `env_file`.

**Environment variable pattern:**
```python
import os

access_token = os.environ.get("SUPABASE_ACCESS_TOKEN")
if not access_token:
    raise ValueError("SUPABASE_ACCESS_TOKEN is not set in container environment")
```

**Important:** Never read `.env` from skill directory. Always use environment variables at runtime.

See: [references/setup-guide.md](references/setup-guide.md) for detailed setup and credential management.

---

## Usage

### Quick Commands (Clean Output)

```bash
# Who am I?
python3 scripts/supabase_agent.py whoami
# Output: Organizations: 2

# List all projects
python3 scripts/supabase_agent.py projects
# Output:
# • [ACTIVE_HEALTHY] skool-goose-dev - us-east-1 (ID: ovrxdoyvkyrczsxhvada)

# Check security advisors
python3 scripts/supabase_agent.py security ovrxdoyvkyrczsxhvada
# Output:
# Found 41 security issue(s):
# ❌ ERRORS (40 issues):
#   • RLS Disabled in Public
#     Table `public.users` is public, but RLS has not been enabled.

# Get security details as JSON
python3 scripts/supabase_agent.py security-json ovrxdoyvkyrczsxhvada

# Check performance advisors
python3 scripts/supabase_agent.py performance ovrxdoyvkyrczsxhvada

# Get postgres logs (last hour)
python3 scripts/supabase_agent.py logs ovrxdoyvkyrczsxhvada postgres 1

# Execute read-only query
python3 scripts/supabase_agent.py query ovrxdoyvkyrczsxhvada "SELECT COUNT(*) FROM users"
```

### Python API

```python
from scripts.supabase_client import SupabaseClient

# Get authenticated client
client = SupabaseClient()

# Get all projects
projects = client.get_projects()

# Get security advisors
advisors = client.get_security_advisors('ovrxdoyvkyrczsxhvada')

# Filter ERROR-level issues
errors = [a for a in advisors if a.get('level') == 'ERROR']
print(f"Found {len(errors)} critical security issues")

# Get logs
from datetime import datetime, timedelta
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=24)

logs = client.get_logs(
    'ovrxdoyvkyrczsxhvada',
    service='postgres',
    iso_timestamp_start=start_time.isoformat() + 'Z',
    iso_timestamp_end=end_time.isoformat() + 'Z'
)
```

---

## Common Use Cases

See: [references/api-operations.md](references/api-operations.md) for complete API reference.

**Popular use cases:**
- Handle security alert emails
- Daily security monitoring
- Log analysis (errors, auth events)
- Database health checks
- Performance advisor tracking

**Example - Handle Security Alert Email:**
```bash
# 1. Get security advisors
python3 scripts/supabase_agent.py security ovrxdoyvkyrczsxhvada

# 2. Export detailed JSON
python3 scripts/supabase_agent.py security-json ovrxdoyvkyrczsxhvada > report.json

# 3. Check recent logs for context
python3 scripts/supabase_agent.py logs ovrxdoyvkyrczsxhvada postgres 24
```

---

## API Reference

See: [references/api-operations.md](references/api-operations.md) for complete API documentation.

**Quick reference:**

### Read Operations ✅
- `get_current_user()` - Get authenticated user info
- `get_projects()` - List all projects
- `get_security_advisors(project_id)` - Get security lints
- `get_performance_advisors(project_id)` - Get performance lints
- `get_logs(project_id, service, start, end)` - Get service logs
- `execute_query(project_id, query)` - Execute read-only SQL

### Write Operations ⚠️ (Require Approval)
- `create_project(...)` - Create new project (billable)
- `pause_project(project_id)` - Pause project (service interruption)
- `restore_project(project_id)` - Restore paused project
- `execute_migration(project_id, name, sql)` - Apply migration (DDL changes)

---

## Security Advisors

See: [references/security-advisors.md](references/security-advisors.md) for detailed security monitoring guide.

**Security Levels:**
- **ERROR:** Critical issues (RLS disabled, exposed keys, weak passwords)
- **WARNING:** Important issues (missing indexes, unrestricted API)
- **INFO:** Advisory items (unused extensions, deprecated functions)

**Email Alert Workflow:**
When you receive "Security vulnerabilities detected in your Supabase project":

```bash
# Step 1: Check advisors
python3 scripts/supabase_agent.py security <project_id>

# Step 2: Get detailed JSON
python3 scripts/supabase_agent.py security-json <project_id> > security-report.json

# Step 3: Check logs
python3 scripts/supabase_agent.py logs <project_id> postgres 24
```

---

## Error Handling

See: [references/error-handling.md](references/error-handling.md) for detailed patterns.

**Common errors:**
- **401:** Authentication failed - check `SUPABASE_ACCESS_TOKEN`
- **404:** Project not found - verify project ID
- **429:** Rate limited - use exponential backoff (~100 req/min limit)
- **500:** Supabase server error - retry with delay

**Basic pattern:**
```python
import requests

try:
    advisors = client.get_security_advisors('project_id')
except requests.HTTPError as e:
    if e.response.status_code == 401:
        print("Authentication failed - check SUPABASE_ACCESS_TOKEN")
    elif e.response.status_code == 429:
        print("Rate limited - wait before retrying")
```

---

## Implementation

**For agents:**
- `scripts/supabase_agent.py` - Clean CLI interface
  - Commands: whoami, projects, security, performance, logs, query
  - Clean formatted output or JSON
- `scripts/supabase_client.py` - Full Management API client
  - All API methods with error handling
  - Direct integration for custom workflows

**For testing:**
- Test harness validates authentication, read operations, error handling

---

## Resources

- [Setup Guide](references/setup-guide.md) - Token authentication and configuration
- [Security Advisors](references/security-advisors.md) - Security monitoring and email alerts
- [API Operations](references/api-operations.md) - Complete method documentation
- [Error Handling](references/error-handling.md) - Patterns, rate limits, monitoring
- [Success Metrics](references/success-metrics.md) - Measurement framework
- [Distribution Guide](DISTRIBUTION.md) - Packaging and release workflow
- **Supabase Management API:** https://supabase.com/docs/reference/api/introduction
- **Personal Access Tokens:** https://supabase.com/dashboard/account/tokens

---

**Status:** ✅ Approved for production with controls
**Security:** Direct API, read-safe, writes require approval
**Last audit:** 2026-02-21
