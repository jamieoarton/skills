---
name: bramclaw-clickup
description: Use when users ask to list, search, create, update, or organize ClickUp tasks, spaces, or workspaces, including status, assignee, and priority workflows.
---

**Version:** 2.0.0 | [Changelog](CHANGELOG.md) | **Status:** ✅ Production

---

# bramclaw-clickup

Direct ClickUp API integration using API key authentication.

## When This Skill Should Trigger

**✅ Should trigger for:**
- "Create a ClickUp task for the bug we discussed"
- "What tasks are assigned to me?"
- "Check my ClickUp workspace"
- "Search for tasks tagged 'api'"
- "Show me high priority tasks"
- "List my open tasks in ClickUp"

**❌ Should NOT trigger for:**
- "Create a GitHub issue" (different tool)
- "Add to my calendar" (different service)
- "Make a note" (different tool)
- "Send an email" (different service)

**⚠️ Ambiguous (ask for clarification):**
- "Create a task" (ClickUp? GitHub? Local todo?)
- "Check my tasks" (ClickUp? Email? Calendar?)

## Skill Confidence

**High confidence (>90%):**
- Explicit "ClickUp" mention
- "task" + management context (assigned, priority, workspace)

**Medium confidence (50-90%):**
- Generic "task" without tool specified
- Context suggests task management but ambiguous

**Low confidence (<50%):**
- Generic "to-do" or "reminder"
- No task management context

---

## Success Metrics

See: [references/success-metrics.md](references/success-metrics.md) for detailed measurement framework.

**Key Targets:**
- **Triggering accuracy:** >90%
- **Token reduction:** >70% (13K → <4K tokens)
- **API efficiency:** 1-2 calls (vs. 12 exploratory calls)
- **Security:** 100% approval before writes, 100% audit logging

**Current Performance:**
- Triggering: Not yet measured (baseline needed)
- Tokens: ~3K with skill vs. ~13K without (77% reduction ✅)
- API calls: 1-2 vs. 12 (90% reduction ✅)
- Security: 100% approval workflow ✅

---

## When to Use This Skill

**Decision Framework:**

```plaintext
Need task management?
    ├─ ClickUp-specific? → Use bramclaw-clickup ✅
    ├─ GitHub issues? → Use GitHub tools
    ├─ Generic todos? → Ask user which system
    └─ Complex workflows? → Consider ClickUp MCP
```

**Use bramclaw-clickup when:**
- ✅ Simple CRUD operations on tasks
- ✅ Quick workspace/list/task queries
- ✅ Agent needs read-only task access
- ✅ Creating/updating individual tasks (with approval)

**Use ClickUp MCP when:**
- Advanced features (time tracking, custom fields, bulk operations)
- Complex automation workflows
- Deep integration requirements

**Use ClickUp UI when:**
- Visual board management
- Complex project setup
- Reporting and dashboards

**Alternatives Comparison:**

| Need | bramclaw-clickup | ClickUp UI | ClickUp MCP | ClawHub Maton |
|------|------------------|------------|-------------|---------------|
| **Read tasks** | ✅ Best | ⚠️ Manual | ✅ Good | ⚠️ Third-party proxy |
| **Create tasks** | ✅ Good (requires approval) | ✅ Yes | ✅ Yes | ⚠️ Third-party proxy |
| **Agent-friendly** | ✅ Yes | ❌ No | ✅ Yes | ⚠️ Complex setup |
| **Security** | ✅ Direct API | ✅ Direct | ✅ Direct | ❌ Maton.ai proxy |
| **Setup complexity** | ✅ Low (API key) | ✅ Easy | ⚠️ Medium | ❌ High (Maton + OAuth) |

---

## Security Model

**Defense in Depth:**
- **Layer 1:** Direct API (no third-party proxy)
- **Layer 2:** Code-level controls (write methods clearly marked)
- **Layer 3:** Human approval (agent asks before writes)
- **Layer 4:** Monitoring (log all operations)

See: [references/security-model.md](references/security-model.md) for complete security architecture.

**What Agent Can Do (Safe ✅):**
- Read workspaces, spaces, folders, lists, tasks
- Search tasks with filters
- Get current user info

**What Requires Approval (⚠️):**
- Create/update tasks
- Delete tasks (HIGH RISK)
- Bulk operations

**Security Features:**
- ✅ Direct API access (no third-party proxy like Maton.ai)
- ✅ Single credential (`CLICK_UP_API_KEY` from environment)
- ✅ No shell execution (Python module import)
- ✅ Read operations safe for agent use
- ⚠️ Write operations require human approval

---

## Setup

**Already configured.** `CLICK_UP_API_KEY` is injected into the OpenClaw container via Docker Compose `env_file`.

**Environment variable pattern:**
```python
import os

api_key = os.environ.get("CLICK_UP_API_KEY")
if not api_key:
    raise ValueError("CLICK_UP_API_KEY is not set in container environment")
```

**Important:** Never read `.env` from skill directory. Always use environment variables at runtime.

See: [references/security-model.md](references/security-model.md) for detailed setup and credential management.

---

## Usage

### Quick Commands (Clean Output)

```bash
# Who am I?
python3 scripts/clickup_agent.py whoami
# Output: Jamie Oarton (jamie@bramforth.ai)

# List workspaces
python3 scripts/clickup_agent.py workspaces
# Output:
# 1. Bramforth (ID: 90151855437)

# List spaces in workspace
python3 scripts/clickup_agent.py spaces 90151855437
# Output:
# 1. Engineering (ID: 90200...)
# 2. Marketing (ID: 90201...)

# Get tasks from list
python3 scripts/clickup_agent.py tasks 901234
# Output:
# 1. Implement user auth (Status: in progress)
# 2. Fix API bug (Status: blocked)
```

### Python API

```python
from scripts.clickup_client import ClickUpClient

# Get authenticated client
client = ClickUpClient()

# Get my tasks
user = client.get_current_user()
workspaces = client.get_workspaces()
team_id = workspaces[0]['id']

my_tasks = client.search_tasks(
    team_id=team_id,
    assignees=[user['id']],
    include_closed=False
)

print(f"You have {len(my_tasks)} open tasks")
for task in my_tasks:
    print(f"- {task['name']} (Status: {task['status']['status']})")
```

---

## Common Queries

See: [references/common-queries.md](references/common-queries.md) for complete cookbook.

**Popular queries:**
- Find tasks by assignee
- Get overdue tasks
- Search by status/priority/tags
- Tasks due this week
- Traverse workspace hierarchy

**Example - Find my tasks:**
```python
client = ClickUpClient()
user = client.get_current_user()
workspaces = client.get_workspaces()

my_tasks = client.search_tasks(
    team_id=workspaces[0]['id'],
    assignees=[user['id']]
)
```

---

## API Reference

See: [references/api-reference.md](references/api-reference.md) for complete API documentation.

**Quick reference:**

### Read Operations ✅
- `get_workspaces()` - List workspaces
- `get_spaces(team_id)` - List spaces
- `get_tasks(list_id, ...)` - List tasks with filters
- `search_tasks(team_id, ...)` - Search across workspace
- `get_current_user()` - Get authenticated user

### Write Operations ⚠️ (Require Approval)
- `create_task(list_id, name, ...)` - Create task
- `update_task(task_id, ...)` - Update task
- `delete_task(task_id)` - Delete task (HIGH RISK)

---

## Error Handling

See: [references/error-handling.md](references/error-handling.md) for detailed patterns.

**Common errors:**
- **401:** Authentication failed - check `CLICK_UP_API_KEY`
- **404:** Resource not found - verify ID is correct
- **429:** Rate limited - use exponential backoff (100 req/min limit)
- **500:** ClickUp server error - retry with delay

**Basic pattern:**
```python
import requests

try:
    tasks = client.get_tasks(list_id='901234')
except requests.HTTPError as e:
    if e.response.status_code == 401:
        print("Authentication failed - check CLICK_UP_API_KEY")
    elif e.response.status_code == 429:
        print("Rate limited - wait before retrying")
```

---

## Testing

See: [tests/TEST-PLAN.md](tests/TEST-PLAN.md) for comprehensive test plan.

**Quick validation:**
```bash
# Test authentication
python3 scripts/clickup_agent.py whoami

# Test list operations
python3 scripts/clickup_agent.py workspaces
```

**Test coverage:**
- ✅ Authentication (valid, invalid, missing credentials)
- ✅ Read operations (workspaces, tasks, search, empty results)
- ✅ Error handling (rate limits, 404, 500)
- ⬜ Trigger patterns (manual Claude testing)
- ⬜ Performance metrics (token usage, API efficiency)

---

## Implementation

**For agents:**
- `scripts/clickup_agent.py` - Clean CLI interface
- `scripts/clickup_client.py` - ClickUp API client library

**For testing:**
- `tests/TEST-PLAN.md` - Comprehensive test scenarios
- Test harness validates authentication, read ops, error handling

---

## Architecture

```
bram-claw → clickup_client.py → https://api.clickup.com
```

**No third-party proxy** (unlike ClawHub clickup-api skill which uses Maton.ai).

**Security advantage:** Direct API means no third-party sees your ClickUp data.

---

## Resources

- [Setup Guide](references/security-model.md#authentication) - Credential configuration
- [Common Queries](references/common-queries.md) - Query cookbook with examples
- [API Reference](references/api-reference.md) - Complete method documentation
- [Security Model](references/security-model.md) - Architecture and best practices
- [Error Handling](references/error-handling.md) - Patterns, rate limits, monitoring
- [Success Metrics](references/success-metrics.md) - Measurement framework
- [Distribution Guide](DISTRIBUTION.md) - Packaging and release workflow
- **ClickUp API Docs:** https://clickup.com/api

---

**Status:** ✅ Approved for production with controls
**Security:** Direct API, read-safe, writes require approval
**Last audit:** 2026-02-21
