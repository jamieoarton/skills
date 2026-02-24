# Setup Guide - bramclaw-supabase

Complete guide for setting up Supabase Management API access.

---

## Prerequisites

- Supabase account (https://supabase.com)
- At least one Supabase project
- Python 3.x

---

## Get Personal Access Token

### Step 1: Generate Token

1. Go to https://supabase.com/dashboard/account/tokens
2. Click "Generate new token"
3. Give it a descriptive name (e.g., "bram-claw-access")
4. Copy the token immediately (it's only shown once)

**Token format:** `sbp_abc123...`

### Step 2: Add to Environment

**For Docker/OpenClaw:**

Add to your environment file:
```bash
SUPABASE_ACCESS_TOKEN=sbp_abc123...
```

**For local development:**

Add to `.env` file:
```bash
# .env
SUPABASE_ACCESS_TOKEN=sbp_abc123...
```

**For shell session:**

```bash
export SUPABASE_ACCESS_TOKEN=sbp_abc123...
```

### Step 3: Verify Setup

```bash
cd scripts
python3 supabase_agent.py whoami
```

**Expected output:**
```
Organizations: 2
```

**If error:**
```
Error: Supabase access token not found. Set SUPABASE_ACCESS_TOKEN environment variable.
```

Check that:
1. Environment variable is set
2. Token starts with `sbp_`
3. Token hasn't expired or been revoked

---

## Authentication Architecture

**Environment Variable Pattern:**

```python
import os

access_token = os.environ.get("SUPABASE_ACCESS_TOKEN")
if not access_token:
    raise ValueError("SUPABASE_ACCESS_TOKEN is not set in container environment")
```

**Security Model:**

- ✅ **Direct API:** No third-party proxy
- ✅ **Single credential:** Personal Access Token from environment
- ✅ **No shell execution:** Python module imports
- ✅ **Read operations:** Safe for agent use
- ⚠️ **Write operations:** Require human approval

**Important:** Never commit tokens to git. Always use environment variables.

---

## Permissions and Scopes

Personal Access Tokens have access to:

**Read Operations (Safe):**
- List organizations
- List projects
- Get security advisors
- Get performance advisors
- Get logs
- Execute read-only queries

**Write Operations (Require Approval):**
- Create projects (billable)
- Pause/restore projects (service interruption)
- Apply migrations (DDL changes)
- Update project settings

---

## Token Security Best Practices

### 1. Environment Variables Only

**Never:**
```python
# DON'T hardcode tokens
token = "sbp_abc123..."
```

**Always:**
```python
# DO use environment variables
token = os.environ.get("SUPABASE_ACCESS_TOKEN")
```

### 2. Gitignore Protection

Ensure `.env` is in `.gitignore`:
```bash
# .gitignore
.env
*.env
```

### 3. Token Rotation

- Rotate tokens every 90 days
- Revoke old tokens after rotation
- Use descriptive names to track token usage

### 4. Scope Limitation

- Use separate tokens for different environments (dev, prod)
- Revoke tokens immediately if compromised
- Monitor token usage in Supabase dashboard

---

## Testing Authentication

### Quick Test

```bash
# Test 1: Check organizations
python3 scripts/supabase_agent.py whoami

# Test 2: List projects
python3 scripts/supabase_agent.py projects

# Test 3: Get security advisors (requires project ID)
python3 scripts/supabase_agent.py security YOUR_PROJECT_ID
```

### Python Test

```python
from scripts.supabase_client import SupabaseClient

# Initialize client
client = SupabaseClient()

# Test authentication
try:
    projects = client.get_projects()
    print(f"✅ Authenticated successfully - {len(projects)} projects found")
except Exception as e:
    print(f"❌ Authentication failed: {e}")
```

---

## Troubleshooting

### Error: "401 Unauthorized"

**Cause:** Invalid or expired token

**Fix:**
1. Verify token in environment: `printenv | grep SUPABASE_ACCESS_TOKEN`
2. Check token hasn't expired
3. Generate new token if needed
4. Update environment variable

### Error: "Token not found"

**Cause:** Environment variable not set

**Fix:**
```bash
# Check if set
echo $SUPABASE_ACCESS_TOKEN

# Set for current session
export SUPABASE_ACCESS_TOKEN=sbp_abc123...

# Permanently (add to .bashrc or .zshrc)
echo 'export SUPABASE_ACCESS_TOKEN=sbp_abc123...' >> ~/.bashrc
```

### Error: "No projects found"

**Cause:** Token valid but no projects in account

**Fix:**
1. Create a project at https://supabase.com/dashboard
2. Or verify token belongs to correct account

---

## Configuration Files

### .env Example

```bash
# Supabase Management API
SUPABASE_ACCESS_TOKEN=sbp_your_token_here

# Optional: Default project ID
DEFAULT_PROJECT_ID=ovrxdoyvkyrczsxhvada
```

### Docker Compose Example

```yaml
services:
  app:
    environment:
      - SUPABASE_ACCESS_TOKEN=${SUPABASE_ACCESS_TOKEN}
    env_file:
      - .env
```

---

## API Endpoint

**Base URL:** `https://api.supabase.com/v1`

**Authentication Header:**
```
Authorization: Bearer sbp_abc123...
```

All requests include this header automatically when using `SupabaseClient`.

---

## Rate Limits

**Management API:**
- Per-user, per-scope rate limiting
- Exact limits not publicly documented
- Typical: ~100 requests per minute

**Best Practices:**
- Cache organization/project IDs
- Use filters to reduce response size
- Implement exponential backoff on 429 errors

---

## Resources

- **Personal Access Tokens:** https://supabase.com/dashboard/account/tokens
- **Management API Docs:** https://supabase.com/docs/reference/api/introduction
- **Authentication Guide:** https://supabase.com/docs/reference/api/authentication

---

**Last updated:** 2026-02-21
