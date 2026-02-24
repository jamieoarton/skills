# Test Plan - bramclaw-supabase

## Overview

Comprehensive test plan for bramclaw-supabase skill covering authentication, read operations, write operations (with approval), error handling, and integration.

## Prerequisites

- Supabase account (https://supabase.com)
- `SUPABASE_ACCESS_TOKEN` environment variable set
- At least one Supabase project with security issues (for testing advisors)

---

## Phase 1: Authentication Tests

### Test 1.1: Valid Authentication

**Objective:** Verify Personal Access Token authenticates successfully

**Steps:**
```bash
cd scripts
python3 supabase_agent.py whoami
```

**Expected:**
- Output: "Organizations: X" (where X > 0)
- No errors

**Pass Criteria:**
- [ ] Successfully authenticates
- [ ] Returns organization count
- [ ] No authentication errors

---

### Test 1.2: Missing Environment Variable

**Objective:** Verify clear error when access token missing

**Steps:**
```bash
unset SUPABASE_ACCESS_TOKEN
cd scripts
python3 supabase_agent.py whoami
```

**Expected:**
- Error: "Supabase access token not found. Set SUPABASE_ACCESS_TOKEN environment variable."

**Pass Criteria:**
- [ ] Clear error message (not generic exception)
- [ ] Tells user what's missing
- [ ] Doesn't expose credentials in error

---

### Test 1.3: Invalid Access Token

**Objective:** Verify error handling for invalid credentials

**Steps:**
```bash
export SUPABASE_ACCESS_TOKEN=invalid_token_123
cd scripts
python3 supabase_agent.py whoami
```

**Expected:**
- Error about authentication failure (401)

**Pass Criteria:**
- [ ] Graceful error (not crash)
- [ ] Mentions authentication/401 error
- [ ] Suggests checking access token

---

## Phase 2: Read Operations Tests

### Test 2.1: List Projects

**Objective:** Retrieve projects successfully

**Steps:**
```bash
cd scripts
python3 supabase_agent.py projects
```

**Expected:**
```
• [ACTIVE_HEALTHY] project-name - region (ID: project_id)
```

**Pass Criteria:**
- [ ] At least one project shown
- [ ] Clean formatted output
- [ ] No error messages
- [ ] Shows status, name, region, ID

---

### Test 2.2: Get Security Advisors

**Objective:** Retrieve security lints for a project

**Steps:**
```bash
# Use project ID from Test 2.1
cd scripts
python3 supabase_agent.py security [project_id]
```

**Expected:**
- List of security issues by level (ERROR, WARNING, INFO)
- Human-readable format

**Pass Criteria:**
- [ ] Security advisors listed
- [ ] Grouped by level
- [ ] No errors
- [ ] Proper formatting

---

### Test 2.3: Get Security Advisors JSON

**Objective:** Retrieve security lints as structured JSON

**Steps:**
```bash
cd scripts
python3 supabase_agent.py security-json [project_id]
```

**Expected:**
- Valid JSON output
- Array of advisor objects

**Pass Criteria:**
- [ ] Valid JSON
- [ ] Contains expected fields (name, title, level, categories, detail)
- [ ] Can be parsed programmatically

---

### Test 2.4: Get Performance Advisors

**Objective:** Retrieve performance lints for a project

**Steps:**
```bash
cd scripts
python3 supabase_agent.py performance [project_id]
```

**Expected:**
- List of performance issues
- Human-readable format

**Pass Criteria:**
- [ ] Performance advisors listed
- [ ] No errors
- [ ] Proper formatting

---

### Test 2.5: Get Logs

**Objective:** Retrieve service logs

**Steps:**
```bash
# Get postgres logs from last hour
cd scripts
python3 supabase_agent.py logs [project_id] postgres 1
```

**Expected:**
- Log entries from last hour
- Or message if no logs available

**Pass Criteria:**
- [ ] Logs retrieved or clear "no logs" message
- [ ] No errors
- [ ] Time range respected

---

### Test 2.6: Execute Read-Only Query

**Objective:** Execute SELECT query against database

**Steps:**
```bash
cd scripts
python3 supabase_agent.py query [project_id] "SELECT 1"
```

**Expected:**
- Query result returned
- No errors

**Pass Criteria:**
- [ ] Query executes successfully
- [ ] Result returned
- [ ] No errors

---

### Test 2.7: Handle Empty Results

**Objective:** Gracefully handle no results found

**Steps:**
```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()

# Get logs with narrow time range (likely empty)
logs = client.get_logs(
    '[project_id]',
    'postgres',
    '2020-01-01T00:00:00Z',
    '2020-01-01T01:00:00Z'
)

print(f"Found {len(logs)} logs")
```

**Expected:**
- Output: "Found 0 logs"
- No errors

**Pass Criteria:**
- [ ] Empty list returned (not error)
- [ ] Graceful handling
- [ ] Clear "0 results" message

---

## Phase 3: Write Operations Tests (Require Approval)

### Test 3.1: Create Project

**Objective:** Create project with approval workflow

**Steps:**
```python
from scripts.supabase_client import SupabaseClient

# NOTE: This should prompt for approval in agent context

client = SupabaseClient()
project = client.create_project(
    organization_id='[org_id]',
    name='test-project-please-delete',
    db_pass='super-secret-password-123',
    region='us-east-1',
    plan='free'
)

print(f"Created project: {project['name']} (ID: {project['id']})")
```

**Expected:**
- Project created successfully
- Returns project object with ID

**Pass Criteria:**
- [ ] Project created
- [ ] Project ID returned
- [ ] Can retrieve project afterwards
- [ ] **Agent requests approval before creation** (manual verification)

---

### Test 3.2: Pause Project

**Objective:** Pause project with approval workflow

**Steps:**
```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()

# Use project ID from Test 3.1
client.pause_project('[project_id]')
print("Project paused")
```

**Expected:**
- Project paused successfully
- Services stopped

**Pass Criteria:**
- [ ] Project paused
- [ ] **Agent requests approval before pausing** (manual verification)
- [ ] **Agent warns about service interruption** (manual verification)

---

### Test 3.3: Restore Project

**Objective:** Restore paused project

**Steps:**
```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()

# Use project ID from Test 3.2
client.restore_project('[project_id]')
print("Project restored")
```

**Expected:**
- Project restored successfully

**Pass Criteria:**
- [ ] Project restored
- [ ] **Agent requests approval before restoring** (manual verification)

---

## Phase 4: Error Handling Tests

### Test 4.1: Rate Limit Handling

**Objective:** Handle API rate limits gracefully

**Steps:**
```python
# Note: Supabase Management API has rate limits (~100 req/min)
# This test is manual - rapid requests to trigger limit

from scripts.supabase_client import SupabaseClient
import time

client = SupabaseClient()

for i in range(150):
    try:
        projects = client.get_projects()
    except Exception as e:
        print(f"Rate limit at request {i}: {e}")
        break
```

**Expected:**
- Eventually hits rate limit (429)
- Clear error message about rate limiting

**Pass Criteria:**
- [ ] Error message mentions "rate limit" or "429"
- [ ] Doesn't crash
- [ ] Suggests waiting/retrying

---

### Test 4.2: Invalid Project ID

**Objective:** Handle non-existent projects gracefully

**Steps:**
```python
from scripts.supabase_client import SupabaseClient

client = SupabaseClient()

try:
    advisors = client.get_security_advisors('invalid_project_id')
except Exception as e:
    print(f"Error: {e}")
```

**Expected:**
- Error: "Project not found" or 404 error

**Pass Criteria:**
- [ ] Clear error (not generic exception)
- [ ] Doesn't crash
- [ ] Helps user understand what went wrong

---

### Test 4.3: Server Errors (500/503)

**Objective:** Handle Supabase server errors gracefully

**Note:** This test is difficult to trigger intentionally. Monitor during regular use.

**Expected behavior when server error occurs:**
- Clear error message
- Retry suggestion
- No crash

**Pass Criteria:**
- [ ] Handles 500/503 errors gracefully
- [ ] Suggests retrying
- [ ] Doesn't crash

---

## Phase 5: Integration Tests

### Test 5.1: Trigger Pattern Accuracy

**Objective:** Verify skill triggers correctly in Claude

**Setup:**
- Start Claude Code session
- Load bramclaw-supabase skill

**Test Queries:**

| Query | Should Trigger? | Result |
|-------|----------------|--------|
| "Check Supabase security advisors" | ✅ Yes | PASS/FAIL |
| "Get Supabase project logs" | ✅ Yes | PASS/FAIL |
| "List my Supabase projects" | ✅ Yes | PASS/FAIL |
| "Deploy to Firebase" | ❌ No | PASS/FAIL |
| "Create Vercel project" | ❌ No | PASS/FAIL |
| "Check security advisors" (ambiguous) | ⚠️ Clarify | PASS/FAIL |

**Pass Criteria:**
- [ ] >90% accuracy (5/6 or better)
- [ ] Clear skill loading message
- [ ] Correct operations executed

---

### Test 5.2: End-to-End Security Alert Workflow

**Objective:** Complete realistic security alert workflow

**Scenario:** User receives Supabase security alert email

**Steps:**
1. User asks Claude: "I got a Supabase security alert for project abc123"
2. Claude loads bramclaw-supabase skill
3. Claude gets security advisors
4. Claude analyzes issues
5. Claude gets logs for context
6. Claude presents findings

**Expected:**
- Skill triggers automatically
- Correct queries executed
- Results presented clearly

**Pass Criteria:**
- [ ] Skill triggers without prompting
- [ ] Gets security advisors
- [ ] Gets logs
- [ ] Results accurate
- [ ] User satisfied with output

---

### Test 5.3: Approval Workflow Integration

**Objective:** Verify approval workflow works in agent context

**Scenario:** User asks agent to create a project

**Steps:**
1. User: "Create a Supabase project called 'test-project'"
2. Agent should request approval with project details
3. User approves
4. Agent creates project
5. Agent confirms creation

**Expected:**
- Agent asks for approval before creation
- Shows project details in approval request
- Creates only after approval
- Confirms success

**Pass Criteria:**
- [ ] Agent requests approval
- [ ] Shows clear project details
- [ ] Only creates after approval
- [ ] Confirms creation with project ID

---

## Phase 6: Performance Tests

### Test 6.1: Token Usage Measurement

**Objective:** Verify skill reduces token usage vs. raw API exploration

**Setup:**
- Test without skill: New Claude session, ask "Get Supabase security advisors"
- Test with skill: Load skill, ask same question

**Expected:**
- Without skill: ~15K tokens
- With skill: ~5K tokens
- Reduction: >65%

**Pass Criteria:**
- [ ] Token reduction >65%
- [ ] Skill version completes faster
- [ ] Same/better result quality

---

### Test 6.2: API Call Efficiency

**Objective:** Verify skill minimizes API calls

**Setup:**
- Monitor API calls during advisor retrieval
- Track number of calls needed

**Steps:**
```bash
# Count API calls (enable logging if possible)
cd scripts
python3 supabase_agent.py projects  # Should be 1 call
python3 supabase_agent.py security [project_id]  # Should be 1 call
```

**Expected:**
- Projects: 1 API call
- Security advisors: 1 API call

**Pass Criteria:**
- [ ] Minimal API calls for simple queries
- [ ] No exploratory/failed calls
- [ ] Direct to solution

---

## Regression Tests

Run before each release:

```bash
# Authentication
python3 scripts/supabase_agent.py whoami

# List operations
python3 scripts/supabase_agent.py projects

# Security advisors (requires project ID)
python3 scripts/supabase_agent.py security [project_id]
```

**All must pass:**
- [ ] No errors
- [ ] Expected output format
- [ ] Performance within acceptable range

---

## Security Tests

### Test 7.1: Credential Exposure

**Objective:** Verify access token never exposed in logs/errors

**Steps:**
- Trigger various errors
- Check error messages don't contain access token

**Pass Criteria:**
- [ ] Access token never in error messages
- [ ] Access token never logged
- [ ] Only mentions "SUPABASE_ACCESS_TOKEN" variable name

---

### Test 7.2: Approval Enforcement

**Objective:** Verify write operations require approval

**Manual test in agent context:**
- Request project creation
- Request project pause
- Request project restore

**Pass Criteria:**
- [ ] Create requires approval
- [ ] Pause requires approval (with service interruption warning)
- [ ] Restore requires approval

---

## Success Criteria Summary

**Skill is production-ready when:**
- ✅ All Phase 1 tests pass (authentication)
- ✅ All Phase 2 tests pass (read operations)
- ✅ All Phase 3 tests pass (write operations with approval)
- ✅ All Phase 4 tests pass (error handling)
- ✅ >90% trigger accuracy (Phase 5)
- ✅ >65% token reduction (Phase 6)
- ✅ 0% regression failures
- ✅ 100% approval enforcement (Security)

**Current Status (2026-02-21):**
- Phase 1: ✅ Passing
- Phase 2: ✅ Passing
- Phase 3: ⬜ Requires manual testing in agent context
- Phase 4: ✅ Passing
- Phase 5: ⬜ Not yet measured
- Phase 6: ⬜ Not yet measured
- Security: ✅ Passing

---

## Test Automation

### Continuous Testing

Create test runner:

```bash
#!/bin/bash
# tests/run-all-tests.sh

echo "Running bramclaw-supabase test suite..."

echo "Phase 1: Authentication"
python3 scripts/supabase_agent.py whoami || exit 1

echo "Phase 2: Read Operations"
python3 scripts/supabase_agent.py projects || exit 1

echo "All tests passed ✓"
```

**Run before commits:**
```bash
chmod +x tests/run-all-tests.sh
./tests/run-all-tests.sh
```

---

## Manual Test Checklist

Before release:
- [ ] Run automated tests (tests/run-all-tests.sh)
- [ ] Test in fresh Claude session (trigger patterns)
- [ ] Verify approval workflow for write operations
- [ ] Verify all reference docs load
- [ ] Check scripts/ directory structure
- [ ] Validate frontmatter YAML
- [ ] Review CHANGELOG.md
- [ ] Check version matches release tag
- [ ] No credential exposure in logs/errors
