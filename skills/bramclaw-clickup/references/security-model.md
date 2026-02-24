# ClickUp Security Model

Security architecture and controls for `bramclaw-clickup` skill.

## Defense in Depth

**Layer 1: Direct API** - No third-party proxy (unlike ClawHub Maton skill)
**Layer 2: Code-level controls** - Write methods clearly marked in API reference
**Layer 3: Human approval** - Agent should ask before write operations
**Layer 4: Monitoring** - Log all ClickUp operations (see error-handling.md)

---

## What Agent Can Do (Safe ✅)

**Read Operations (No approval needed):**
- Read workspaces, spaces, folders, lists
- Read tasks (with filtering)
- Search tasks across workspace
- Get task details
- Get current user info
- Browse workspace hierarchy

**Rationale:** Read operations don't modify data and can't cause damage.

---

## What Agent Must Request Approval For (⚠️)

**Write Operations (Require approval):**
- Create tasks
- Update tasks
- Modify task assignees
- Change task status
- Add/remove tags
- Set due dates
- Update task descriptions

**High-Risk Operations (Always require approval):**
- Delete tasks
- Delete lists/folders/spaces
- Bulk operations without review

**Rationale:** Write operations modify production data. Mistakes can cause data loss or workflow disruption.

---

## Approval Workflow

### For Single Task Creation

**Agent should ask:**
> "I recommend creating a task in ClickUp:
>
> **List:** Engineering Tasks
> **Name:** Implement user authentication
> **Assignees:** @jamie
> **Due Date:** 7 days from now
> **Priority:** High
>
> May I create this task?"

**User responds:** "Yes" or "No"

### For Bulk Operations

**Agent should ask:**
> "I need to create 15 tasks based on your requirements. May I proceed with bulk task creation?"

**User responds:** "Yes" or "No"

### For Deletions

**Agent should ALWAYS ask:**
> "⚠️ WARNING: You're requesting to delete task 'Deploy to production' (ID: abc123). This is permanent and cannot be undone. Are you absolutely sure?"

**User must explicitly confirm.**

---

## Comparison: ClawHub Skill vs. Direct API

### Architecture Comparison

| Factor | ClawHub clickup-api | bramclaw-clickup | Winner |
|--------|---------------------|------------------|--------|
| **Third-party proxy** | Maton.ai gateway | Direct to ClickUp | ✅ Direct |
| **Credentials needed** | MATON_API_KEY + OAuth | CLICK_UP_API_KEY | ✅ Direct |
| **Setup complexity** | High (Maton signup + OAuth) | Low (key already exists) | ✅ Direct |
| **Shell execution** | Yes (Python heredoc) | No (module import) | ✅ Direct |
| **Vendor lock-in** | Maton.ai dependency | None | ✅ Direct |
| **Data exposure** | Maton sees all requests | ClickUp only | ✅ Direct |

### Security Implications

**ClawHub clickup-api (via Maton.ai):**
- ❌ Third-party sees all ClickUp data
- ❌ Requires Maton.ai account and OAuth
- ❌ Executes Python via shell (injection risk)
- ❌ Vendor lock-in (Maton dependency)
- ⚠️ Additional attack surface (Maton + ClickUp)

**bramclaw-clickup (Direct API):**
- ✅ No third-party data exposure
- ✅ Single credential (API key)
- ✅ No shell execution (pure Python import)
- ✅ No vendor dependencies
- ✅ Smaller attack surface

**Verdict:** Direct API approach (bramclaw-clickup) is simpler and more secure.

---

## Authentication

### Current Setup

API key is injected via Docker Compose environment file.

```bash
# Container environment (read-only)
CLICK_UP_API_KEY=pk_1234567890abcdef...
```

### Code Pattern

```python
import os

api_key = os.environ.get("CLICK_UP_API_KEY")
if not api_key:
    raise ValueError("CLICK_UP_API_KEY is not set in container environment")
```

**Security:**
- ✅ Environment variable (not in code)
- ✅ Loaded at container startup
- ✅ Not stored in skill directory
- ✅ Not passed via command line (would be visible in process list)

**Never:**
- ❌ Read from `.env` file in skill directory
- ❌ Hardcode API key in Python files
- ❌ Pass as command-line argument
- ❌ Store in git repository

---

## Credential Rotation

### When to Rotate API Key

Rotate ClickUp API key if:
- Key exposed in logs/error messages
- Key committed to git (even if reverted)
- Suspicious API usage detected
- Team member with key access leaves
- Regular 90-day rotation policy

### How to Rotate

1. Generate new API key in ClickUp settings
2. Update `.env` file with new key
3. Restart OpenClaw container
4. Revoke old key in ClickUp
5. Verify new key works: `python3 scripts/clickup_agent.py whoami`

---

## Monitoring and Auditing

### What to Log

**Always log:**
- All write operations (create/update/delete)
- Task IDs affected
- User who initiated operation
- Timestamp
- Operation result (success/failure)

**Example log entry:**
```
2026-02-21 10:30:45 - INFO - CLICKUP_CREATE_TASK: list_id=901234, name="Deploy v2.0", assignee=123
2026-02-21 10:30:46 - INFO - CLICKUP_TASK_CREATED: task_id=abc456, url=https://app.clickup.com/t/abc456
```

**Never log:**
- API keys
- Full task descriptions (may contain sensitive data)
- User passwords

See [error-handling.md](error-handling.md) for detailed logging implementation.

---

## Alerts

Configure alerts for:
- **>50 API calls in 1 minute** (approaching rate limit)
- **Any delete operations** (high risk)
- **Failed authentication** (401 errors)
- **Unusual bulk operations** (>20 tasks created in 5 minutes)

---

## Best Practices

### 1. Principle of Least Privilege

Use API key with minimum necessary permissions:
- ✅ Read access to all workspaces
- ✅ Write access only to specific spaces/lists
- ❌ Avoid admin-level keys if possible

### 2. Request Approval for Write Operations

Agent should always ask before:
```python
# ❌ Bad - writes without asking
def auto_create_task(name):
    client = ClickUpClient()
    return client.create_task(list_id='901234', name=name)

# ✅ Good - requests approval
def create_task_with_approval(name):
    response = ask_user(f"May I create task: {name}?")
    if response.lower() == 'yes':
        client = ClickUpClient()
        return client.create_task(list_id='901234', name=name)
    else:
        return "Task creation cancelled by user"
```

### 3. Validate Input

Sanitize user input before passing to ClickUp API:
```python
# ✅ Good - validates input
def safe_create_task(name, description):
    if len(name) > 200:
        raise ValueError("Task name too long (max 200 chars)")
    if len(description) > 10000:
        raise ValueError("Description too long (max 10K chars)")

    client = ClickUpClient()
    return client.create_task(list_id='901234', name=name, description=description)
```

### 4. Rate Limit Protection

Implement backoff for rate limits:
```python
import time
import requests

def safe_api_call(func, *args, **kwargs):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except requests.HTTPError as e:
            if e.response.status_code == 429:  # Rate limited
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"Rate limited. Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Max retries exceeded")
```

### 5. Audit Trail

Maintain audit log of all write operations:
```python
import logging
import json

logging.basicConfig(
    filename='/var/log/bramclaw/clickup-audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def audit_log(operation, details):
    logging.info(json.dumps({
        'operation': operation,
        'timestamp': time.time(),
        'details': details
    }))

# Usage
audit_log('CREATE_TASK', {'list_id': '901234', 'name': 'Deploy v2.0'})
```

---

## Security Checklist

Before using bramclaw-clickup in production:

- [ ] API key stored in environment variable (not in code)
- [ ] API key not committed to git
- [ ] Write operations require human approval
- [ ] Audit logging enabled for all write operations
- [ ] Rate limit handling implemented
- [ ] Alerts configured for suspicious activity
- [ ] Credential rotation procedure documented
- [ ] Team trained on approval workflow
- [ ] Regular security audits scheduled (quarterly)

---

## Resources

- **ClickUp Security:** https://clickup.com/security
- **API Authentication:** https://clickup.com/api/developer-portal/authentication/
- **OAuth2 (alternative):** https://clickup.com/api/developer-portal/oauth/
- **Rate Limits:** https://clickup.com/api/developer-portal/rate-limits/
