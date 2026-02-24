# Test Plan - bramclaw-obsidian

Comprehensive test plan for bramclaw-obsidian skill covering authentication, read operations, write operations (with approval), error handling, and integration.

## Overview

Tests Obsidian vault access via Google Drive API with service account authentication.

## Prerequisites

- Google Workspace account
- Obsidian vault synced to Google Drive
- Service account with domain-wide delegation
- `OBSIDIAN_VAULT_FOLDER_ID` and `OBSIDIAN_DELEGATED_EMAIL` environment variables set

---

## Phase 1: Authentication Tests

### Test 1.1: Valid Authentication

**Objective:** Verify service account authenticates successfully

**Steps:**
```python
from scripts.obsidian_vault import ObsidianVaultSkill

vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1ABC...xyz',
    delegated_email='your-email@domain.com'
)

# Should succeed without errors
print("Authentication successful")
```

**Expected:**
- No errors
- ObsidianVaultSkill initialized

**Pass Criteria:**
- [ ] Successfully authenticates
- [ ] No authentication errors
- [ ] Audit log shows initialization

---

### Test 1.2: Missing Environment Variable

**Objective:** Verify clear error when credentials missing

**Steps:**
```python
# Remove credentials file temporarily
vault = ObsidianVaultSkill(
    service_account_file='/nonexistent/file.json',
    vault_folder_id='1ABC...xyz',
    delegated_email='your-email@domain.com'
)
```

**Expected:**
- Error about missing credentials file

**Pass Criteria:**
- [ ] Clear error message
- [ ] Doesn't crash
- [ ] Tells user what's missing

---

### Test 1.3: Invalid Folder ID

**Objective:** Verify error handling for invalid vault folder

**Steps:**
```python
vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='invalid_folder_id',
    delegated_email='your-email@domain.com'
)

# Try to list notes
notes = vault.list_notes()
```

**Expected:**
- Error: "Folder not found" or 404 error

**Pass Criteria:**
- [ ] Graceful error (not crash)
- [ ] Clear error message
- [ ] Suggests checking folder ID

---

## Phase 2: Read Operations Tests

### Test 2.1: Search Notes

**Objective:** Search vault successfully

**Steps:**
```python
vault = ObsidianVaultSkill(...)

results = vault.search_notes('meeting', max_results=5)
print(f"Found {len(results)} notes")
for note in results:
    print(f"  - {note['name']}")
```

**Expected:**
- List of matching notes
- Each note has: id, name, modifiedTime

**Pass Criteria:**
- [ ] At least one result found (if vault has matching notes)
- [ ] Clean formatted output
- [ ] No errors

---

### Test 2.2: Read Note

**Objective:** Read note content by file ID

**Steps:**
```python
# Use file ID from search results
file_id = results[0]['id']
content = vault.read_note(file_id=file_id)
print(content[:200])
```

**Expected:**
- Note content as UTF-8 string
- Markdown formatting preserved

**Pass Criteria:**
- [ ] Content retrieved successfully
- [ ] UTF-8 decoded correctly
- [ ] No errors

---

### Test 2.3: List All Notes

**Objective:** List all markdown files in vault

**Steps:**
```python
notes = vault.list_notes()
print(f"Total notes: {len(notes)}")
```

**Expected:**
- List of all notes in vault
- Reasonable number (depends on vault size)

**Pass Criteria:**
- [ ] Notes listed successfully
- [ ] Count matches expected vault size
- [ ] No errors

---

### Test 2.4: Handle Empty Search

**Objective:** Gracefully handle no results found

**Steps:**
```python
results = vault.search_notes('xyznonexistentquery123')
print(f"Found {len(results)} notes")
```

**Expected:**
- Empty list returned (not error)
- Output: "Found 0 notes"

**Pass Criteria:**
- [ ] Empty list returned
- [ ] No errors
- [ ] Clear "0 results" message

---

## Phase 3: Write Operations Tests (Require Approval)

### Test 3.1: Create Note

**Objective:** Create new note with confirmation

**Steps:**
```python
result = vault.create_note(
    name="Test Note.md",
    content="# Test Note\n\nThis is a test",
    confirmed=True
)
print(f"Created: {result['id']}")
```

**Expected:**
- Note created successfully
- Returns file ID

**Pass Criteria:**
- [ ] Note created
- [ ] File ID returned
- [ ] Can read note afterwards
- [ ] Audit log shows CREATE

---

### Test 3.2: Create Note Without Confirmation

**Objective:** Verify confirmation gate works

**Steps:**
```python
try:
    vault.create_note(
        name="Test.md",
        content="Content",
        confirmed=False  # Or omit parameter
    )
except SecurityError as e:
    print(f"Security gate worked: {e}")
```

**Expected:**
- Raises SecurityError
- Error message mentions confirmation required

**Pass Criteria:**
- [ ] SecurityError raised
- [ ] Clear error message
- [ ] No note created

---

### Test 3.3: Append to Note

**Objective:** Append content to existing note

**Steps:**
```python
# Use note from Test 3.1
vault.append_to_note(
    file_id='<FILE_ID>',
    content="\n## Appended Section\n\nNew content",
    confirmed=True
)

# Verify
updated_content = vault.read_note(file_id='<FILE_ID>')
assert "Appended Section" in updated_content
```

**Expected:**
- Content appended successfully
- Original content preserved

**Pass Criteria:**
- [ ] Content appended
- [ ] Original content intact
- [ ] Audit log shows APPEND

---

### Test 3.4: Size Limit Enforcement

**Objective:** Verify 1MB size limit

**Steps:**
```python
large_content = "x" * 2_000_000  # 2MB

try:
    vault.create_note(
        name="Large.md",
        content=large_content,
        confirmed=True
    )
except ValueError as e:
    print(f"Size limit enforced: {e}")
```

**Expected:**
- Raises ValueError
- Error mentions size limit (1MB)

**Pass Criteria:**
- [ ] ValueError raised
- [ ] Clear error message with sizes
- [ ] No note created

---

### Test 3.5: Rate Limiting

**Objective:** Verify 10 creates/minute limit

**Steps:**
```python
from scripts.obsidian_vault import RateLimitError

try:
    for i in range(15):
        vault.create_note(
            name=f"Test-{i}.md",
            content="Content",
            confirmed=True
        )
except RateLimitError as e:
    print(f"Rate limit enforced at note {i}: {e}")
```

**Expected:**
- First 10 succeed
- 11th raises RateLimitError

**Pass Criteria:**
- [ ] Rate limit enforced
- [ ] Clear error message
- [ ] Shows seconds to wait

---

### Test 3.6: Path Validation

**Objective:** Verify file must be in vault folder

**Steps:**
```python
# Try to append to file outside vault
external_file_id = '<EXTERNAL_FILE_ID>'

try:
    vault.append_to_note(
        file_id=external_file_id,
        content="Content",
        confirmed=True
    )
except SecurityError as e:
    print(f"Path validation worked: {e}")
```

**Expected:**
- Raises SecurityError
- Error mentions file not in vault

**Pass Criteria:**
- [ ] SecurityError raised
- [ ] Clear error message
- [ ] No modification made

---

## Phase 4: Convenience Features Tests

### Test 4.1: Create Daily Note

**Objective:** Create daily note with template

**Steps:**
```python
from datetime import datetime

result = vault.create_daily_note(confirmed=True)
expected_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
print(f"Created daily note: {result['name']}")
assert result['name'] == expected_name
```

**Expected:**
- Daily note created with YYYY-MM-DD.md format
- Default template applied

**Pass Criteria:**
- [ ] Daily note created
- [ ] Correct filename format
- [ ] Template content present

---

### Test 4.2: Get Frontmatter

**Objective:** Parse YAML frontmatter from note

**Steps:**
```python
# Create note with frontmatter
content = """---
tags: [test, demo]
status: active
---

# Content
"""
result = vault.create_note("Frontmatter Test.md", content, confirmed=True)

# Parse frontmatter
metadata = vault.get_frontmatter(result['id'])
print(metadata)
```

**Expected:**
- Dictionary with parsed frontmatter
- Tags as list, status as string

**Pass Criteria:**
- [ ] Frontmatter parsed correctly
- [ ] Types preserved (list, string, etc.)
- [ ] No errors

---

### Test 4.3: Update Frontmatter

**Objective:** Update frontmatter while preserving content

**Steps:**
```python
vault.update_frontmatter(
    file_id='<FILE_ID>',
    metadata={'status': 'completed', 'reviewed_by': 'Jamie'},
    confirmed=True
)

# Verify
updated_metadata = vault.get_frontmatter('<FILE_ID>')
assert updated_metadata['status'] == 'completed'
assert updated_metadata['reviewed_by'] == 'Jamie'
```

**Expected:**
- Frontmatter updated
- Existing fields preserved
- Content unchanged

**Pass Criteria:**
- [ ] Frontmatter updated
- [ ] Existing fields intact
- [ ] Content preserved

---

### Test 4.4: Resolve Internal Links

**Objective:** Find and resolve [[wiki-links]]

**Steps:**
```python
# Create notes with internal links
vault.create_note("Target Note.md", "# Target", confirmed=True)
vault.create_note(
    "Source Note.md",
    "# Source\n\nSee [[Target Note]] for details.\n\nBroken: [[Nonexistent]]",
    confirmed=True
)

# Resolve links
source_id = '<SOURCE_FILE_ID>'
links = vault.resolve_internal_links(source_id)
print(links)
```

**Expected:**
- Dictionary mapping link text to file IDs
- Valid links resolved to IDs
- Broken links return None

**Pass Criteria:**
- [ ] Valid links resolved
- [ ] Broken links identified (None)
- [ ] No errors

---

## Phase 5: Integration Tests

### Test 5.1: Trigger Pattern Accuracy

**Objective:** Verify skill triggers correctly in Claude

**Setup:**
- Start Claude Code session
- Load bramclaw-obsidian skill

**Test Queries:**

| Query | Should Trigger? | Result |
|-------|----------------|--------|
| "Read my Obsidian daily note" | ✅ Yes | PASS/FAIL |
| "Search vault for meeting notes" | ✅ Yes | PASS/FAIL |
| "List all notes in Obsidian" | ✅ Yes | PASS/FAIL |
| "Read Notion database" | ❌ No | PASS/FAIL |
| "Search local markdown files" | ❌ No | PASS/FAIL |
| "Search my notes" (ambiguous) | ⚠️ Clarify | PASS/FAIL |

**Pass Criteria:**
- [ ] >90% accuracy (5/6 or better)
- [ ] Clear skill loading message
- [ ] Correct operations executed

---

### Test 5.2: End-to-End Daily Note Workflow

**Objective:** Complete realistic daily note creation

**Scenario:** User asks agent to create today's daily note

**Steps:**
1. User: "Create my Obsidian daily note for today"
2. Agent loads bramclaw-obsidian skill
3. Agent calls `create_daily_note(confirmed=True)`
4. Agent confirms creation with file ID

**Expected:**
- Skill triggers automatically
- Daily note created with YYYY-MM-DD.md format
- Confirmation shown to user

**Pass Criteria:**
- [ ] Skill triggers without prompting
- [ ] Daily note created
- [ ] Correct filename format
- [ ] User receives confirmation

---

### Test 5.3: Approval Workflow Integration

**Objective:** Verify approval workflow works in agent context

**Scenario:** User asks agent to create a note

**Steps:**
1. User: "Create a note called 'Meeting Notes.md' in my Obsidian vault"
2. Agent should request approval with note details
3. User approves
4. Agent creates note with `confirmed=True`
5. Agent confirms creation

**Expected:**
- Agent asks for approval before creation
- Shows note name and content in approval request
- Creates only after approval
- Confirms success

**Pass Criteria:**
- [ ] Agent requests approval
- [ ] Shows clear note details
- [ ] Only creates after approval
- [ ] Confirms creation with file ID

---

## Phase 6: Security Tests

### Test 6.1: Backup Verification

**Objective:** Verify backup warning shown before writes

**Steps:**
```python
vault = ObsidianVaultSkill(...)
vault.verify_backup_exists()  # Should show warning
```

**Expected:**
- Warning message about backups
- Lists recommended backup methods
- Returns True after acknowledgment

**Pass Criteria:**
- [ ] Warning shown
- [ ] Backup methods listed
- [ ] Returns True
- [ ] Audit log shows verification

---

### Test 6.2: Credential Security

**Objective:** Verify access token never exposed

**Steps:**
- Trigger various errors
- Check error messages don't contain credentials
- Check audit log doesn't contain credentials

**Expected:**
- No credentials in error messages
- No credentials in logs
- Only environment variable names mentioned

**Pass Criteria:**
- [ ] Credentials never in error messages
- [ ] Credentials never in audit log
- [ ] Only variable names shown

---

### Test 6.3: Audit Logging

**Objective:** Verify all operations logged

**Steps:**
```bash
# Perform various operations
# Then check audit log
grep "CREATE:" /root/logs/obsidian_vault.log
grep "APPEND:" /root/logs/obsidian_vault.log
```

**Expected:**
- All write operations logged
- Log entries include: operation, file ID, size, vault ID

**Pass Criteria:**
- [ ] CREATE operations logged
- [ ] APPEND operations logged
- [ ] Log format correct
- [ ] No sensitive data in logs

---

## Success Criteria Summary

**Skill is production-ready when:**
- ✅ All Phase 1 tests pass (authentication)
- ✅ All Phase 2 tests pass (read operations)
- ✅ All Phase 3 tests pass (write operations with confirmation)
- ✅ All Phase 4 tests pass (convenience features)
- ✅ >90% trigger accuracy (Phase 5)
- ✅ 100% security compliance (Phase 6)
- ✅ 0% regression failures

**Current Status (2026-02-21):**
- Phase 1: ✅ Passing
- Phase 2: ✅ Passing
- Phase 3: ⬜ Requires manual testing in agent context
- Phase 4: ⬜ Requires manual testing
- Phase 5: ⬜ Not yet measured
- Phase 6: ✅ Passing

---

## Manual Test Checklist

Before release:
- [ ] Run automated tests
- [ ] Test in fresh Claude session (trigger patterns)
- [ ] Verify approval workflow for write operations
- [ ] Verify all reference docs load
- [ ] Check scripts/ directory structure
- [ ] Validate frontmatter YAML
- [ ] Review CHANGELOG.md
- [ ] Check version matches release tag
- [ ] No credential exposure in logs/errors
- [ ] Backup verification works

---

**Last updated:** 2026-02-21
**Version:** 2.0.0
