# API Operations - bramclaw-obsidian

Complete API reference for Obsidian vault operations via Google Drive.

---

## Quick Reference

### Read Operations (Safe for Agent) ✅

```python
from scripts.obsidian_vault import ObsidianVaultSkill

vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1ABC...xyz',
    delegated_email='your-email@domain.com'
)

# Search notes
results = vault.search_notes('project alpha', max_results=10)
for note in results:
    print(f"{note['name']} - {note['modifiedTime']}")

# Read specific note
content = vault.read_note(file_id='1ABC...xyz')
print(content)

# List all notes
notes = vault.list_notes(max_results=100)
```

### Write Operations (Require Confirmation) ⚠️

All write operations require `confirmed=True`:

```python
# Create new note
result = vault.create_note(
    name="Daily Note 2026-02-20.md",
    content="# 2026-02-20\n\n## Tasks\n- [ ] Review PRs",
    confirmed=True  # REQUIRED
)
print(f"Created: {result['id']}")

# Append to existing note
vault.append_to_note(
    file_id='1ABC...xyz',
    content="\n## New Section\n\nAppended content here",
    confirmed=True  # REQUIRED
)
```

---

## Phase 1: Read Operations

### search_notes()

Search vault for markdown files matching query.

**Signature:**
```python
vault.search_notes(query: str, max_results: int = 10) -> list[dict]
```

**Parameters:**
- `query`: Search term (matches file names)
- `max_results`: Maximum results to return (default: 10)

**Returns:** List of note dictionaries with fields:
- `id`: Google Drive file ID
- `name`: Note filename
- `modifiedTime`: ISO 8601 timestamp

**Example:**
```python
results = vault.search_notes('meeting notes', max_results=5)
for note in results:
    print(f"{note['name']} (modified: {note['modifiedTime']})")
```

---

### read_note()

Read note content by file ID.

**Signature:**
```python
vault.read_note(file_id: str) -> str
```

**Parameters:**
- `file_id`: Google Drive file ID

**Returns:** Note content as UTF-8 string

**Example:**
```python
content = vault.read_note(file_id='1ABC...xyz')
print(content)
```

---

### list_notes()

List all markdown files in vault or specific folder.

**Signature:**
```python
vault.list_notes(folder_id: str = None) -> list[dict]
```

**Parameters:**
- `folder_id`: Optional folder ID (defaults to vault root)

**Returns:** List of note dictionaries (same format as `search_notes`)

**Example:**
```python
# List all notes in vault
all_notes = vault.list_notes()
print(f"Total notes: {len(all_notes)}")

# List notes in specific folder
subfolder_notes = vault.list_notes(folder_id='1DEF...abc')
```

---

## Phase 3: Write Operations

### create_note()

Create new note in vault.

**Signature:**
```python
vault.create_note(name: str, content: str, confirmed: bool = False) -> dict
```

**Parameters:**
- `name`: Note filename (e.g., "My Note.md")
- `content`: Note content (markdown)
- `confirmed`: Must be `True` to execute (security gate)

**Returns:** File metadata dictionary:
- `id`: Created file ID
- `name`: Filename

**Raises:**
- `SecurityError`: If `confirmed` is not True
- `ValueError`: If content exceeds 1MB
- `RateLimitError`: If too many creates (>10/minute)

**Example:**
```python
result = vault.create_note(
    name="Project Alpha Notes.md",
    content="# Project Alpha\n\n## Status\n\nIn progress",
    confirmed=True
)
print(f"Created note: {result['id']}")
```

---

### append_to_note()

Append content to existing note.

**Signature:**
```python
vault.append_to_note(file_id: str, content: str, confirmed: bool = False) -> None
```

**Parameters:**
- `file_id`: Google Drive file ID
- `content`: Content to append
- `confirmed`: Must be `True` to execute (security gate)

**Raises:**
- `SecurityError`: If `confirmed` is not True or file not in vault
- `ValueError`: If total size would exceed 1MB

**Example:**
```python
vault.append_to_note(
    file_id='1ABC...xyz',
    content="\n## Update 2026-02-21\n\nProgress update here",
    confirmed=True
)
```

---

## Convenience Features (Phase 2)

### Daily Notes

Create daily notes with automatic date formatting:

```python
from datetime import datetime, timedelta

# Create today's daily note with default template
result = vault.create_daily_note(confirmed=True)
# Creates: 2026-02-20.md with default sections

# Create daily note for specific date
yesterday = datetime.now() - timedelta(days=1)
result = vault.create_daily_note(date=yesterday, confirmed=True)

# Use custom template (supports {date} placeholder)
custom_template = \"\"\"# {date}

## Morning Goals
- [ ]

## Afternoon Tasks
- [ ]

## Evening Reflection

\"\"\"
result = vault.create_daily_note(template=custom_template, confirmed=True)
```

---

### Frontmatter Operations

Parse and update YAML frontmatter in notes:

```python
# Extract frontmatter from note
metadata = vault.get_frontmatter('1ABC...xyz')
print(metadata)
# {'tags': ['project', 'alpha'], 'status': 'in-progress', 'priority': 'high'}

# Update/merge frontmatter (preserves existing fields)
vault.update_frontmatter(
    file_id='1ABC...xyz',
    metadata={
        'status': 'completed',      # Override existing
        'reviewed_by': 'Jamie'       # Add new field
    },
    confirmed=True  # REQUIRED
)

# Add frontmatter to note without it
vault.update_frontmatter(
    file_id='1DEF...abc',
    metadata={'tags': ['new'], 'created': '2026-02-20'},
    confirmed=True
)
```

---

### Internal Link Resolution

Find and resolve Obsidian-style `[[wiki-links]]`:

```python
# Analyze note for internal links
links = vault.resolve_internal_links('1ABC...xyz')
print(links)
# {
#     'Project Alpha': '1QrP...WcLc',      # Valid link → file ID
#     'Meeting Notes': '1Ep2...jPtV',      # Valid link → file ID
#     'Non-Existent-Note': None            # Broken link → None
# }

# Check for broken links
broken = [link for link, file_id in links.items() if file_id is None]
if broken:
    print(f"Broken links: {broken}")
```

---

## Phased Implementation Guide

### Phase 1: Read-Only (Start Here)

**Operations:**
- `search_notes()` - Search vault by keyword
- `read_note()` - Read specific note content
- `list_notes()` - List all notes in vault/folders

**Scope:** `drive.readonly`

**Time:** < 1 hour including setup

**Use cases:**
- Search for meeting notes
- Read project documentation
- List all notes in folder
- Find notes by keyword

---

### Phase 2: Enhanced Features

**Operations:**
- `get_frontmatter()` - Parse YAML frontmatter
- `resolve_internal_links()` - Find `[[wiki-links]]`
- Folder navigation
- Caching layer

**Scope:** Still `drive.readonly`

**Time:** 2-3 hours

**Use cases:**
- Extract metadata from notes
- Find broken internal links
- Navigate folder hierarchy
- Cache frequently accessed notes

---

### Phase 3: Controlled Writes (Optional)

**Operations:**
- `create_note()` - Create new notes
- `append_to_note()` - Append to existing notes
- `create_daily_note()` - Create daily notes from template
- `update_frontmatter()` - Update note metadata

**Scope:** Upgrade to `drive` (NOT `drive.file`)

**Requirements:**
- Explicit user confirmation for each write (`confirmed=True`)
- Cannot modify files outside vault folder (`_validate_in_vault`)
- No delete operations (or double-confirmation required)
- Test in non-production environment first
- Backup strategy verified (see backup-strategies.md)

**Time:** 2-3 hours including testing

**Use cases:**
- Automated daily note creation
- Append meeting notes
- Update task statuses
- Tag notes with metadata

---

## Error Handling

```python
from scripts.obsidian_vault import SecurityError, RateLimitError

try:
    vault.create_note("Test.md", "Content", confirmed=True)
except SecurityError as e:
    print(f"Security check failed: {e}")
    # Caused by: confirmed=False or file outside vault
except RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
    # Caused by: >10 creates in last minute
except ValueError as e:
    print(f"Validation error: {e}")
    # Caused by: Content size > 1MB
```

---

## Security Limits

### Size Limit: 1MB per Note

```python
MAX_NOTE_SIZE = 1_048_576  # 1MB

# Raises ValueError if content > 1MB
large_content = "x" * 2_000_000
vault.create_note("Large.md", large_content, confirmed=True)  # ❌ Fails
```

### Rate Limit: 10 Creates/Minute

```python
MAX_CREATES_PER_MINUTE = 10

# Raises RateLimitError after 10 creates in 60 seconds
for i in range(15):
    vault.create_note(f"Note-{i}.md", "Content", confirmed=True)  # ❌ Fails at 11th
```

### Path Validation: Vault Folder Only

```python
# All file operations verify file is within vault
vault.append_to_note(external_file_id, "Content", confirmed=True)  # ❌ Fails
# Raises SecurityError if file not in vault
```

---

## Backup Verification

Before first write operation, verify backups exist:

```python
vault = ObsidianVaultSkill(...)
vault.verify_backup_exists()  # Shows warning about backups

# Then proceed with writes
vault.create_note("Test.md", "Content", confirmed=True)
```

See backup-strategies.md for complete backup setup guide.

---

**Last updated:** 2026-02-21
**Related:** google-drive-integration.md, setup-guide.md, backup-strategies.md
