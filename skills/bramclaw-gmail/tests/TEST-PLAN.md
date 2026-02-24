# Test Plan - bramclaw-gmail

## Overview

Comprehensive test plan for bramclaw-gmail skill covering authentication, read operations, error handling, and integration.

## Prerequisites

- Service account configured with domain-wide delegation
- `SERVICE_ACCOUNT_FILE` and `EMAIL_ACCOUNT` env vars set
- Gmail account with at least 5 test emails

## Phase 1: Authentication Tests

### Test 1.1: Valid Authentication

**Objective:** Verify service account authenticates successfully

**Steps:**
```bash
cd tests
python3 -c "from gmail_test import get_gmail_service; svc = get_gmail_service(); print('✓ Auth success')"
```

**Expected:**
- No errors
- Output: "✓ Auth success"

**Pass Criteria:**
- [ ] Service object created
- [ ] No authentication errors
- [ ] Can access API

---

### Test 1.2: Missing Environment Variables

**Objective:** Verify clear error when env vars missing

**Steps:**
```bash
unset SERVICE_ACCOUNT_FILE
cd tests
python3 -c "from gmail_test import get_gmail_service; get_gmail_service()"
```

**Expected:**
- Error: "SERVICE_ACCOUNT_FILE is not set"

**Pass Criteria:**
- [ ] Clear error message (not generic exception)
- [ ] Tells user what's missing
- [ ] Doesn't expose credentials in error

---

### Test 1.3: Invalid Service Account File

**Objective:** Verify error handling for invalid credentials

**Steps:**
```bash
export SERVICE_ACCOUNT_FILE=/tmp/invalid.json
echo '{}' > /tmp/invalid.json
cd tests
python3 -c "from gmail_test import get_gmail_service; get_gmail_service()"
```

**Expected:**
- Error about invalid service account format

**Pass Criteria:**
- [ ] Graceful error (not crash)
- [ ] Helpful error message
- [ ] Suggests checking file path/contents

---

## Phase 2: Read Operations Tests

### Test 2.1: List Recent Emails

**Objective:** Retrieve email subjects successfully

**Steps:**
```bash
cd scripts
python3 gmail_agent.py subjects 5
```

**Expected:**
```
1. [Subject 1]
2. [Subject 2]
3. [Subject 3]
4. [Subject 4]
5. [Subject 5]
```

**Pass Criteria:**
- [ ] Exactly 5 subjects shown (or fewer if mailbox has less)
- [ ] Numbered list format
- [ ] No error messages
- [ ] Clean output (no debug info)

---

### Test 2.2: Get Email as JSON

**Objective:** Retrieve structured email data

**Steps:**
```bash
cd scripts
python3 gmail_agent.py json 3
```

**Expected:**
- JSON array with 3 email objects
- Each object has: from, subject, date, id

**Pass Criteria:**
- [ ] Valid JSON output
- [ ] All required fields present
- [ ] No truncated data

---

### Test 2.3: Search with Filters

**Objective:** Search emails with Gmail query syntax

**Steps:**
```python
from gmail_test import get_gmail_service

service = get_gmail_service()
results = service.users().messages().list(
    userId='me',
    q='newer_than:7d',
    maxResults=10
).execute()

print(f"Found {len(results.get('messages', []))} messages")
```

**Expected:**
- Returns messages from last 7 days only

**Pass Criteria:**
- [ ] Query syntax works
- [ ] Results filtered correctly
- [ ] No errors

---

### Test 2.4: Handle Empty Results

**Objective:** Gracefully handle no results found

**Steps:**
```python
from gmail_test import get_gmail_service

service = get_gmail_service()
results = service.users().messages().list(
    userId='me',
    q='from:definitely-does-not-exist@example.com',
    maxResults=10
).execute()

messages = results.get('messages', [])
print(f"Found {len(messages)} messages")
```

**Expected:**
- Output: "Found 0 messages"
- No errors

**Pass Criteria:**
- [ ] Empty list returned (not error)
- [ ] Graceful handling
- [ ] Clear "0 results" message

---

## Phase 3: Error Handling Tests

### Test 3.1: Rate Limit Handling

**Objective:** Handle API rate limits gracefully

**Steps:**
```python
# Make rapid requests to trigger rate limit
from gmail_test import get_gmail_service
import time

service = get_gmail_service()
for i in range(300):
    try:
        service.users().messages().list(userId='me', maxResults=1).execute()
    except Exception as e:
        print(f"Rate limit at request {i}: {e}")
        break
```

**Expected:**
- Eventually hits rate limit
- Clear error message

**Pass Criteria:**
- [ ] Error message mentions "rate limit" or "quota"
- [ ] Suggests waiting/retrying
- [ ] Doesn't crash

---

### Test 3.2: Invalid Message ID

**Objective:** Handle non-existent message gracefully

**Steps:**
```python
from gmail_test import get_gmail_service

service = get_gmail_service()
try:
    msg = service.users().messages().get(userId='me', id='invalid123').execute()
except Exception as e:
    print(f"Error: {e}")
```

**Expected:**
- Error: "Message not found" or similar

**Pass Criteria:**
- [ ] Clear error (not generic exception)
- [ ] Doesn't crash
- [ ] Helps user understand what went wrong

---

## Phase 4: Integration Tests

### Test 4.1: Trigger Pattern Accuracy

**Objective:** Verify skill triggers correctly in Claude

**Setup:**
- Start Claude Code session
- Load bramclaw-gmail skill

**Test Queries:**

| Query | Should Trigger? | Result |
|-------|----------------|--------|
| "Show me recent Gmail subjects" | ✅ Yes | PASS/FAIL |
| "Check my inbox for unread emails" | ✅ Yes | PASS/FAIL |
| "Search emails from alice@example.com" | ✅ Yes | PASS/FAIL |
| "Send an email to Bob" | ❌ No | PASS/FAIL |
| "Check my calendar" | ❌ No | PASS/FAIL |
| "Get my messages" | ⚠️ Ambiguous | PASS/FAIL |

**Pass Criteria:**
- [ ] >90% accuracy (5/6 or better)
- [ ] Clear skill loading message
- [ ] Correct operations executed

---

### Test 4.2: End-to-End Workflow

**Objective:** Complete realistic workflow using skill

**Scenario:** User wants to find all unread emails from last 3 days with attachments

**Steps:**
1. User asks Claude: "Find unread emails with attachments from last 3 days"
2. Claude loads bramclaw-gmail skill
3. Claude constructs query: `is:unread has:attachment newer_than:3d`
4. Claude uses gmail_agent.py or API
5. Claude presents results

**Expected:**
- Skill triggers automatically
- Correct query constructed
- Results presented clearly

**Pass Criteria:**
- [ ] Skill triggers without prompting
- [ ] Query syntax correct
- [ ] Results accurate
- [ ] User satisfied with output

---

## Phase 5: Performance Tests

### Test 5.1: Token Usage Measurement

**Objective:** Verify skill reduces token usage vs. raw API exploration

**Setup:**
- Test without skill: New Claude session, ask "Get my recent emails"
- Test with skill: Load skill, ask same question

**Measurement:**
```bash
# Without skill:
# Track token count in conversation

# With skill:
# Track token count in conversation
```

**Expected:**
- Without skill: ~10K tokens
- With skill: ~2K tokens
- Reduction: >70%

**Pass Criteria:**
- [ ] Token reduction >70%
- [ ] Skill version completes faster
- [ ] Same/better result quality

---

### Test 5.2: API Call Efficiency

**Objective:** Verify skill minimizes API calls

**Setup:**
- Enable API logging
- Run query with skill

**Steps:**
```bash
export GOOGLE_API_LOG_LEVEL=DEBUG
cd scripts
python3 gmail_agent.py subjects 5 2>&1 | grep -c "Making request"
```

**Expected:**
- 1 API call (messages.list)

**Pass Criteria:**
- [ ] Exactly 1 API call for simple query
- [ ] No exploratory/failed calls
- [ ] Direct to solution

---

## Regression Tests

Run before each release:

```bash
# Authentication
python3 tests/gmail_test.py

# CLI interface
cd scripts
python3 gmail_agent.py subjects 5
python3 gmail_agent.py json 3

# Search
python3 -c "from gmail_test import *; s = get_gmail_service(); print(len(s.users().messages().list(userId='me', q='newer_than:1d').execute().get('messages', [])))"
```

**All must pass:**
- [ ] No errors
- [ ] Expected output format
- [ ] Performance within acceptable range

---

## Success Criteria Summary

**Skill is production-ready when:**
- ✅ All Phase 1 tests pass (authentication)
- ✅ All Phase 2 tests pass (read operations)
- ✅ All Phase 3 tests pass (error handling)
- ✅ >90% trigger accuracy (Phase 4)
- ✅ >70% token reduction (Phase 5)
- ✅ 0% regression failures

**Current Status (2026-02-21):**
- Phase 1: ✅ Passing
- Phase 2: ✅ Passing
- Phase 3: ✅ Passing
- Phase 4: ⬜ Not yet measured
- Phase 5: ⬜ Not yet measured
- Regressions: ✅ None

---

## Test Automation

### Continuous Testing

Create test runner:

```bash
#!/bin/bash
# tests/run-all-tests.sh

echo "Running bramclaw-gmail test suite..."

echo "Phase 1: Authentication"
python3 tests/gmail_test.py || exit 1

echo "Phase 2: Read Operations"
cd scripts
python3 gmail_agent.py subjects 5 > /tmp/test-output.txt || exit 1
grep -q "1\. " /tmp/test-output.txt || exit 1

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
- [ ] Verify all reference docs load
- [ ] Check scripts/ directory structure
- [ ] Validate frontmatter YAML
- [ ] Review CHANGELOG.md
- [ ] Check version matches release tag
