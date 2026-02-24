# Test Plan - bramclaw-clickup

## Overview

Comprehensive test plan for bramclaw-clickup skill covering authentication, read operations, write operations (with approval), error handling, and integration.

## Prerequisites

- ClickUp API key configured
- `CLICK_UP_API_KEY` environment variable set
- ClickUp workspace with at least one space, folder, list, and task

## Phase 1: Authentication Tests

### Test 1.1: Valid Authentication

**Objective:** Verify API key authenticates successfully

**Steps:**
```bash
cd scripts
python3 clickup_agent.py whoami
```

**Expected:**
- Output: Name and email (e.g., "Jamie Oarton (jamie@bramforth.ai)")
- No errors

**Pass Criteria:**
- [ ] Successfully authenticates
- [ ] Returns user details
- [ ] No authentication errors

---

### Test 1.2: Missing Environment Variable

**Objective:** Verify clear error when API key missing

**Steps:**
```bash
unset CLICK_UP_API_KEY
cd scripts
python3 clickup_agent.py whoami
```

**Expected:**
- Error: "ClickUp API key not found. Set CLICK_UP_API_KEY environment variable."

**Pass Criteria:**
- [ ] Clear error message (not generic exception)
- [ ] Tells user what's missing
- [ ] Doesn't expose credentials in error

---

### Test 1.3: Invalid API Key

**Objective:** Verify error handling for invalid credentials

**Steps:**
```bash
export CLICK_UP_API_KEY=invalid_key_123
cd scripts
python3 clickup_agent.py whoami
```

**Expected:**
- Error about authentication failure (401)

**Pass Criteria:**
- [ ] Graceful error (not crash)
- [ ] Mentions authentication/401 error
- [ ] Suggests checking API key

---

## Phase 2: Read Operations Tests

### Test 2.1: List Workspaces

**Objective:** Retrieve workspaces successfully

**Steps:**
```bash
cd scripts
python3 clickup_agent.py workspaces
```

**Expected:**
```
1. [Workspace Name] (ID: [workspace_id])
```

**Pass Criteria:**
- [ ] At least one workspace shown
- [ ] Numbered list format
- [ ] No error messages
- [ ] Clean output (no debug info)

---

### Test 2.2: List Spaces

**Objective:** Retrieve spaces in a workspace

**Steps:**
```bash
# Use workspace ID from Test 2.1
cd scripts
python3 clickup_agent.py spaces [workspace_id]
```

**Expected:**
- List of spaces in workspace
- Clean numbered format

**Pass Criteria:**
- [ ] Spaces listed
- [ ] No errors
- [ ] Proper formatting

---

### Test 2.3: Search Tasks

**Objective:** Search tasks with filters

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()
workspaces = client.get_workspaces()
team_id = workspaces[0]['id']

tasks = client.search_tasks(
    team_id=team_id,
    include_closed=False
)

print(f"Found {len(tasks)} open tasks")
```

**Expected:**
- Returns list of tasks
- No errors

**Pass Criteria:**
- [ ] Search executes successfully
- [ ] Returns task list (or empty list)
- [ ] No errors

---

### Test 2.4: Get Task Details

**Objective:** Retrieve specific task details

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Get a task ID from Test 2.3
task = client.get_task(task_id='[task_id]')

print(f"Task: {task['name']}")
print(f"Status: {task['status']['status']}")
```

**Expected:**
- Returns task details
- Has name, status, assignees, etc.

**Pass Criteria:**
- [ ] Task details retrieved
- [ ] Required fields present
- [ ] No truncated data

---

### Test 2.5: Handle Empty Results

**Objective:** Gracefully handle no results found

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Search with filters that return no results
tasks = client.search_tasks(
    team_id='[workspace_id]',
    assignees=[999999999]  # Non-existent user
)

print(f"Found {len(tasks)} tasks")
```

**Expected:**
- Output: "Found 0 tasks"
- No errors

**Pass Criteria:**
- [ ] Empty list returned (not error)
- [ ] Graceful handling
- [ ] Clear "0 results" message

---

## Phase 3: Write Operations Tests (Require Approval)

### Test 3.1: Create Task

**Objective:** Create task with approval workflow

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

# NOTE: This should prompt for approval in agent context

client = ClickUpClient()
task = client.create_task(
    list_id='[list_id]',
    name='Test task - please delete',
    description='Created by bramclaw-clickup test suite'
)

print(f"Created task: {task['name']} (ID: {task['id']})")
```

**Expected:**
- Task created successfully
- Returns task object with ID

**Pass Criteria:**
- [ ] Task created
- [ ] Task ID returned
- [ ] Can retrieve task afterwards
- [ ] **Agent requests approval before creation** (manual verification)

---

### Test 3.2: Update Task

**Objective:** Update task with approval workflow

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Use task ID from Test 3.1
updated = client.update_task(
    task_id='[task_id]',
    name='Test task - UPDATED',
    status='in progress'
)

print(f"Updated task: {updated['name']}")
```

**Expected:**
- Task updated successfully
- Changes reflected

**Pass Criteria:**
- [ ] Task updated
- [ ] Changes saved
- [ ] **Agent requests approval before update** (manual verification)

---

### Test 3.3: Delete Task (HIGH RISK)

**Objective:** Delete task with strict approval workflow

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

# Use task ID from Test 3.1
client.delete_task(task_id='[task_id]')

print("Task deleted")
```

**Expected:**
- Task deleted
- Confirmation returned

**Pass Criteria:**
- [ ] Task deleted
- [ ] **Agent ALWAYS requests approval before deletion** (manual verification)
- [ ] **Agent warns about permanent deletion** (manual verification)

---

## Phase 4: Error Handling Tests

### Test 4.1: Rate Limit Handling

**Objective:** Handle API rate limits gracefully

**Steps:**
```python
# Note: ClickUp limits are 100 req/min
# This test is manual - rapid requests to trigger limit

from scripts.clickup_client import ClickUpClient
import time

client = ClickUpClient()

for i in range(150):
    try:
        workspaces = client.get_workspaces()
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

### Test 4.2: Invalid Resource ID

**Objective:** Handle non-existent resources gracefully

**Steps:**
```python
from scripts.clickup_client import ClickUpClient

client = ClickUpClient()

try:
    task = client.get_task(task_id='invalid_id_123')
except Exception as e:
    print(f"Error: {e}")
```

**Expected:**
- Error: "Task not found" or 404 error

**Pass Criteria:**
- [ ] Clear error (not generic exception)
- [ ] Doesn't crash
- [ ] Helps user understand what went wrong

---

### Test 4.3: Server Errors (500/503)

**Objective:** Handle ClickUp server errors gracefully

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
- Load bramclaw-clickup skill

**Test Queries:**

| Query | Should Trigger? | Result |
|-------|----------------|--------|
| "Show me my ClickUp tasks" | ✅ Yes | PASS/FAIL |
| "Create a task in ClickUp" | ✅ Yes | PASS/FAIL |
| "List tasks assigned to me" | ✅ Yes | PASS/FAIL |
| "Send an email" | ❌ No | PASS/FAIL |
| "Add to my calendar" | ❌ No | PASS/FAIL |
| "Create a task" (ambiguous) | ⚠️ Clarify | PASS/FAIL |

**Pass Criteria:**
- [ ] >90% accuracy (5/6 or better)
- [ ] Clear skill loading message
- [ ] Correct operations executed

---

### Test 5.2: End-to-End Workflow

**Objective:** Complete realistic workflow using skill

**Scenario:** User wants to find all high-priority tasks assigned to them

**Steps:**
1. User asks Claude: "Show me my high priority tasks in ClickUp"
2. Claude loads bramclaw-clickup skill
3. Claude gets user ID, workspace ID
4. Claude searches tasks with filters
5. Claude presents results

**Expected:**
- Skill triggers automatically
- Correct query constructed
- Results presented clearly

**Pass Criteria:**
- [ ] Skill triggers without prompting
- [ ] Query uses correct filters
- [ ] Results accurate
- [ ] User satisfied with output

---

### Test 5.3: Approval Workflow Integration

**Objective:** Verify approval workflow works in agent context

**Scenario:** User asks agent to create a task

**Steps:**
1. User: "Create a task in ClickUp called 'Review pull request #42'"
2. Agent should request approval with task details
3. User approves
4. Agent creates task
5. Agent confirms creation

**Expected:**
- Agent asks for approval before creation
- Shows task details in approval request
- Creates only after approval
- Confirms success

**Pass Criteria:**
- [ ] Agent requests approval
- [ ] Shows clear task details
- [ ] Only creates after approval
- [ ] Confirms creation with task URL

---

## Phase 6: Performance Tests

### Test 6.1: Token Usage Measurement

**Objective:** Verify skill reduces token usage vs. raw API exploration

**Setup:**
- Test without skill: New Claude session, ask "Get my ClickUp tasks"
- Test with skill: Load skill, ask same question

**Expected:**
- Without skill: ~13K tokens
- With skill: ~3K tokens
- Reduction: >70%

**Pass Criteria:**
- [ ] Token reduction >70%
- [ ] Skill version completes faster
- [ ] Same/better result quality

---

### Test 6.2: API Call Efficiency

**Objective:** Verify skill minimizes API calls

**Setup:**
- Monitor API calls during task retrieval
- Track number of calls needed

**Steps:**
```bash
# Count API calls (enable logging if possible)
cd scripts
python3 clickup_agent.py workspaces  # Should be 1 call
python3 clickup_agent.py tasks [list_id]  # Should be 1 call
```

**Expected:**
- Workspaces: 1 API call
- Tasks: 1 API call

**Pass Criteria:**
- [ ] Minimal API calls for simple queries
- [ ] No exploratory/failed calls
- [ ] Direct to solution

---

## Regression Tests

Run before each release:

```bash
# Authentication
python3 scripts/clickup_agent.py whoami

# List operations
python3 scripts/clickup_agent.py workspaces

# Search (requires workspace ID)
python3 -c "from scripts.clickup_client import *; c = ClickUpClient(); w = c.get_workspaces(); print(len(c.search_tasks(team_id=w[0]['id'])))"
```

**All must pass:**
- [ ] No errors
- [ ] Expected output format
- [ ] Performance within acceptable range

---

## Security Tests

### Test 7.1: Credential Exposure

**Objective:** Verify API key never exposed in logs/errors

**Steps:**
- Trigger various errors
- Check error messages don't contain API key

**Pass Criteria:**
- [ ] API key never in error messages
- [ ] API key never logged
- [ ] Only mentions "CLICK_UP_API_KEY" variable name

---

### Test 7.2: Approval Enforcement

**Objective:** Verify write operations require approval

**Manual test in agent context:**
- Request task creation
- Request task update
- Request task deletion

**Pass Criteria:**
- [ ] Create requires approval
- [ ] Update requires approval
- [ ] Delete ALWAYS requires approval
- [ ] Agent warns about deletion permanence

---

## Success Criteria Summary

**Skill is production-ready when:**
- ✅ All Phase 1 tests pass (authentication)
- ✅ All Phase 2 tests pass (read operations)
- ✅ All Phase 3 tests pass (write operations with approval)
- ✅ All Phase 4 tests pass (error handling)
- ✅ >90% trigger accuracy (Phase 5)
- ✅ >70% token reduction (Phase 6)
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

echo "Running bramclaw-clickup test suite..."

echo "Phase 1: Authentication"
python3 scripts/clickup_agent.py whoami || exit 1

echo "Phase 2: Read Operations"
python3 scripts/clickup_agent.py workspaces || exit 1

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
