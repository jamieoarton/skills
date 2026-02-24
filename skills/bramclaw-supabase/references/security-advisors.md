# Security Advisors Reference

Complete guide to Supabase security advisor lints and security monitoring.

---

## Overview

Security advisors analyze your Supabase project for security vulnerabilities and configuration issues. They're categorized by severity level and provide actionable remediation steps.

**Use Case:** Handle email security alerts from Supabase

---

## Security Levels

Security lints are categorized by severity:

### ERROR Level (Critical)

Security issues that should be fixed immediately.

**Common ERROR lints:**

1. **RLS Disabled in Public**
   - **Description:** Tables in public schema without Row Level Security enabled
   - **Impact:** All data publicly accessible without authentication
   - **Fix:** Enable RLS on affected tables
   ```sql
   ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
   ```

2. **Sensitive Columns Exposed**
   - **Description:** Tables with sensitive data (passwords, session_ids, tokens) exposed without RLS
   - **Impact:** Credential leakage, account compromise
   - **Fix:** Enable RLS and create policies to restrict access

3. **Exposed service role key**
   - **Description:** Service role key detected in client code
   - **Impact:** Full database access from client
   - **Fix:** Use anon key in client, service role only on backend

4. **Weak password policy**
   - **Description:** Database password doesn't meet complexity requirements
   - **Impact:** Vulnerable to brute force attacks
   - **Fix:** Update password with strong complexity

---

### WARNING Level (Important)

Issues that should be addressed but don't pose immediate critical risk.

**Common WARNING lints:**

1. **Missing indexes**
   - **Description:** Large tables without appropriate indexes
   - **Impact:** Poor query performance, slow application
   - **Fix:** Add indexes on frequently queried columns
   ```sql
   CREATE INDEX idx_users_email ON users(email);
   ```

2. **Unrestricted API access**
   - **Description:** No API rate limiting configured
   - **Impact:** Potential abuse, DDoS vulnerability
   - **Fix:** Configure rate limits in project settings

3. **Unverified auth users**
   - **Description:** Auth users without email verification
   - **Impact:** Spam accounts, fake registrations
   - **Fix:** Enable email verification in auth settings

4. **Public storage buckets**
   - **Description:** Storage buckets accessible without authentication
   - **Impact:** Unauthorized file access
   - **Fix:** Configure bucket policies

---

### INFO Level (Advisory)

Informational items for optimization and best practices.

**Common INFO lints:**

1. **Unused extensions**
   - **Description:** PostgreSQL extensions enabled but not used
   - **Impact:** Minimal, slight performance overhead
   - **Fix:** Disable unused extensions

2. **Deprecated functions**
   - **Description:** Using deprecated Supabase features
   - **Impact:** May break in future versions
   - **Fix:** Migrate to recommended alternatives

3. **Suboptimal configuration**
   - **Description:** Settings that could be optimized
   - **Impact:** Performance or cost inefficiency
   - **Fix:** Review and adjust settings

---

## Response Format

Each security advisor lint includes structured data:

### Lint Object Structure

```json
{
  "name": "rls_disabled_in_public",
  "title": "RLS Disabled in Public",
  "level": "ERROR",
  "categories": ["SECURITY"],
  "description": "Tables in the public schema should have Row Level Security enabled.",
  "detail": "Table `public.users` is public, but RLS has not been enabled.",
  "remediation": "https://supabase.com/docs/guides/database/postgres/row-level-security",
  "metadata": {
    "schema": "public",
    "name": "users",
    "table_id": 12345
  }
}
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Lint rule identifier (e.g., `rls_disabled_in_public`) |
| `title` | string | Human-readable title |
| `level` | string | Severity: `ERROR`, `WARNING`, or `INFO` |
| `categories` | array | Categories like `["SECURITY"]` or `["PERFORMANCE"]` |
| `description` | string | General description of the issue |
| `detail` | string | Specific details for this finding (table name, etc.) |
| `remediation` | string | URL to documentation for fixing |
| `metadata` | object | Context (schema, table, column names, etc.) |

---

## Email Alert Workflow

When you receive a security alert email from Supabase:

### Example Email

```
Subject: Security vulnerabilities detected in your Supabase project

We detected security vulnerabilities in 1 of your projects:

Project: skool-goose-dev
ID: ovrxdoyvkyrczsxhvada
40 error(s), 3 warning(s)

View in dashboard: https://supabase.com/dashboard/project/ovrxdoyvkyrczsxhvada
```

### Response Workflow

**Step 1: Get security advisors**

```bash
python3 scripts/supabase_agent.py security ovrxdoyvkyrczsxhvada
```

**Output:**
```
Found 41 security issue(s):

❌ ERRORS (40 issues):
  • RLS Disabled in Public
    Table `public.users` is public, but RLS has not been enabled.
    Fix: https://supabase.com/docs/guides/database/...

  • RLS Disabled in Public
    Table `public.posts` is public, but RLS has not been enabled.
    Fix: https://supabase.com/docs/guides/database/...

⚠️  WARNINGS (3 issues):
  • Missing indexes
    Table `public.users` has no index on `email`
    Fix: https://supabase.com/docs/guides/database/...
```

**Step 2: Get detailed JSON**

```bash
python3 scripts/supabase_agent.py security-json ovrxdoyvkyrczsxhvada > security-report.json
```

**Step 3: Analyze and prioritize**

```python
from scripts.supabase_client import SupabaseClient
import json

client = SupabaseClient()
advisors = client.get_security_advisors('ovrxdoyvkyrczsxhvada')

# Filter by level
errors = [a for a in advisors if a.get('level') == 'ERROR']
warnings = [a for a in advisors if a.get('level') == 'WARNING']

# Group by lint name
from collections import Counter
error_types = Counter(a['name'] for a in errors)

print(f"Top security issues:")
for lint_name, count in error_types.most_common(5):
    print(f"  {lint_name}: {count}")
```

**Step 4: Check recent logs**

```bash
python3 scripts/supabase_agent.py logs ovrxdoyvkyrczsxhvada postgres 24
```

**Step 5: Create action items**

Based on findings, create tasks:
- [ ] Enable RLS on 40 tables
- [ ] Add indexes on user lookup columns
- [ ] Configure auth email verification

---

## Querying Security Advisors

### CLI Usage

```bash
# Human-readable output
python3 scripts/supabase_agent.py security <project_id>

# JSON output (for parsing)
python3 scripts/supabase_agent.py security-json <project_id>
```

### Python API

```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()

# Get all security advisors
advisors = client.get_security_advisors('ovrxdoyvkyrczsxhvada')

# Filter ERROR-level issues
errors = [a for a in advisors if a.get('level') == 'ERROR']

# Get RLS-specific issues
rls_issues = [a for a in advisors if 'rls' in a.get('name', '').lower()]

# Extract affected tables
tables = set(a.get('metadata', {}).get('name') for a in advisors if 'metadata' in a)
```

---

## Remediation Examples

### Fix RLS Disabled

**Issue:** `rls_disabled_in_public`

**SQL Fix:**
```sql
-- Enable RLS on table
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

-- Create policy (authenticated users can see their own data)
CREATE POLICY "Users can view own data"
ON public.users
FOR SELECT
USING (auth.uid() = id);

-- Create policy (authenticated users can update their own data)
CREATE POLICY "Users can update own data"
ON public.users
FOR UPDATE
USING (auth.uid() = id);
```

### Fix Missing Indexes

**Issue:** `unindexed_foreign_keys` or `missing_indexes`

**SQL Fix:**
```sql
-- Add index on foreign key
CREATE INDEX idx_posts_user_id ON posts(user_id);

-- Add index on lookup column
CREATE INDEX idx_users_email ON users(email);

-- Composite index for common query
CREATE INDEX idx_posts_user_created ON posts(user_id, created_at);
```

### Fix Exposed Service Role Key

**Issue:** `exposed_service_role_key`

**Fix:**
1. Remove service role key from client code
2. Use anon key in frontend
3. Move service role operations to backend
4. Rotate service role key in Supabase dashboard

---

## Monitoring Script

Automated daily security check:

```python
#!/usr/bin/env python3
# daily_security_check.py

from scripts.supabase_client import SupabaseClient
from datetime import datetime

client = SupabaseClient()

# Get all projects
projects = client.get_projects()

print(f"Security Check - {datetime.now().isoformat()}")
print("=" * 60)

for project in projects:
    project_id = project['id']
    project_name = project['name']

    # Get security advisors
    advisors = client.get_security_advisors(project_id)

    # Count by level
    errors = sum(1 for a in advisors if a.get('level') == 'ERROR')
    warnings = sum(1 for a in advisors if a.get('level') == 'WARNING')
    info = sum(1 for a in advisors if a.get('level') == 'INFO')

    print(f"\n{project_name} ({project_id}):")
    print(f"  ❌ Errors: {errors}")
    print(f"  ⚠️  Warnings: {warnings}")
    print(f"  ℹ️  Info: {info}")

    # Alert if errors found
    if errors > 0:
        print(f"  🚨 ACTION REQUIRED: {errors} critical security issues")
```

**Run daily via cron:**
```bash
0 9 * * * /path/to/daily_security_check.py >> /var/log/supabase-security.log 2>&1
```

---

## Resources

- **Security Advisor Docs:** https://supabase.com/docs/guides/deployment/security-advisor
- **Row Level Security:** https://supabase.com/docs/guides/database/postgres/row-level-security
- **Auth Policies:** https://supabase.com/docs/guides/auth/policies
- **Database Best Practices:** https://supabase.com/docs/guides/database/best-practices

---

**Last updated:** 2026-02-21
