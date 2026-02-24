---
name: bramclaw-obsidian
description: Use when users ask to read, create, or update Obsidian vault markdown notes stored in Google Drive, including daily notes, note lookup, and vault search tasks.
---

**Version:** 2.0.0 | [Changelog](CHANGELOG.md) | **Status:** ✅ Production

---

# bramclaw-obsidian

Obsidian vault access via Google Drive API with production-ready security features.

**Security Properties:**
- ✅ Direct Drive API access (no filesystem mounts)
- ✅ Service account + domain-wide delegation
- ✅ Confirmation gates for all writes
- ✅ Size limits (1MB per note)
- ✅ Path validation (vault folder only)
- ✅ Complete audit logging to `/root/logs/obsidian_vault.log`
- ✅ Rate limiting (10 creates/minute)
- ✅ Backup verification warnings

---

## When This Skill Should Trigger

**✅ Should trigger for:**
- "Read my Obsidian daily note"
- "Search vault for meeting notes"
- "List all notes in Obsidian"
- "Create daily note in vault"
- "Access Obsidian vault via Drive"
- "Get frontmatter from note"

**❌ Should NOT trigger for:**
- "Read Notion database" (different service)
- "Search local markdown files" (not Drive-based)
- "Access Dropbox vault" (different cloud service)
- "Use obsidian-cli tool" (not Drive API)

**⚠️ Ambiguous (ask for clarification):**
- "Search my notes" (Obsidian? Notion? Local?)
- "Create daily note" (Obsidian? Other system?)
- "Read vault" (Obsidian? Password vault?)

---

## Skill Confidence

**High confidence (>90%):**
- Explicit "Obsidian" mention
- "vault" + "Google Drive" context
- "daily note" + Obsidian context

**Medium confidence (50-90%):**
- Generic "vault" without service specified
- "markdown notes" without Obsidian context
- "daily note" without vault context

**Low confidence (<50%):**
- Generic "notes" or "search"
- No cloud storage context

---

## Success Metrics

See: [references/success-metrics.md](references/success-metrics.md) for detailed measurement framework.

**Key Targets:**
- **Triggering accuracy:** >90%
- **Token reduction:** >50% (2,500 → <1,250 tokens)
- **Setup time:** <1 hour (currently 47 min average ✅)
- **Security compliance:** 100% (no filesystem access)

**Current Performance:**
- Token reduction: 28% (target: >50%, improvement planned)
- Setup time: 47 min average (<1 hour ✅)
- Security: 100% compliance (3/3 deployments ✅)
- API efficiency: 85% (1.3 vs. 6.5 calls ✅)

---

## When to Use This Skill

**Decision Framework:**

```plaintext
Need Obsidian vault access?
    ├─ Vault on Google Drive? → Use bramclaw-obsidian ✅
    ├─ Vault local-only? → Sync to Drive first or use different approach
    ├─ Vault on Dropbox/Syncthing? → This skill is Drive-specific
    └─ Testing MCP locally? → OK for dev, use Drive API for production
```

**Use bramclaw-obsidian when:**
- ✅ Vault synced to Google Drive
- ✅ Need read access (search, read, list)
- ✅ Need write access with confirmation gates
- ✅ Container/cloud deployment required
- ✅ Production environment

**Use Obsidian desktop app when:**
- Visual vault browsing needed
- Complex plugin workflows
- Local-only vault (not synced)

**Alternatives Comparison:**

| Need | bramclaw-obsidian | Obsidian App | MCP Server | Filesystem Mount |
|------|-------------------|--------------|------------|------------------|
| **Cloud portability** | ✅ Best | ❌ No | ⚠️ Complex | ❌ No |
| **Container-safe** | ✅ Yes | ❌ No | ⚠️ Risky | ❌ No |
| **Security** | ✅ Best | ✅ Yes | ⚠️ Medium | ❌ Low |
| **Setup time** | ✅ <1 hour | ✅ Easy | ⚠️ Medium | ❌ Complex |
| **Production-ready** | ✅ Yes | ⚠️ Manual | ❌ No | ❌ No |

---

## Architecture

```
bram-claw → scripts/obsidian_vault.py → Google Drive API → Obsidian Vault
```

**No filesystem mounts** - uses Google Drive API for cloud portability.

See: [references/google-drive-integration.md](references/google-drive-integration.md) for complete implementation pattern.

---

## Setup

See: [references/setup-guide.md](references/setup-guide.md) for complete setup instructions.

### Quick Start

Environment variables (set in Docker Compose `env_file` or `.env`):

```bash
# Required
OBSIDIAN_VAULT_FOLDER_ID=1w-Hn25wNQbgx9vJuFsWGHs9hPLvfkAfv  # Your vault's Drive folder ID
OBSIDIAN_DELEGATED_EMAIL=jamie@bramforth.ai                # Email to impersonate

# Optional (have sensible defaults)
SERVICE_ACCOUNT_FILE=/root/.openclaw/credentials/service-account.json
OBSIDIAN_LOG_FILE=/root/logs/obsidian_vault.log
```

**Service account must have:**
1. Domain-wide delegation enabled
2. Access to vault folder (share folder with service account email)
3. `https://www.googleapis.com/auth/drive` scope

**Get vault folder ID:**
1. Navigate to vault in Google Drive
2. Extract ID from URL: `drive.google.com/drive/folders/<FOLDER_ID>`

---

## Usage from OpenClaw

See: [references/api-operations.md](references/api-operations.md) for complete API reference.

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
notes = vault.list_notes()
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

### Convenience Features ✨

See: [references/api-operations.md](references/api-operations.md#convenience-features-phase-2) for full details.

#### Daily Notes

```python
from datetime import datetime, timedelta

# Create today's daily note with default template
result = vault.create_daily_note(confirmed=True)
# Creates: 2026-02-20.md with default sections

# Create daily note for specific date
yesterday = datetime.now() - timedelta(days=1)
result = vault.create_daily_note(date=yesterday, confirmed=True)

# Use custom template (supports {date} placeholder)
custom_template = """# {date}

## Morning Goals
- [ ]

## Afternoon Tasks
- [ ]

## Evening Reflection

"""
result = vault.create_daily_note(template=custom_template, confirmed=True)
```

#### Frontmatter Operations

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
```

#### Internal Link Resolution

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

## Backup Verification

See: [references/backup-strategies.md](references/backup-strategies.md) for complete backup guide.

**CRITICAL:** Always ensure your vault is backed up before enabling write operations.

Before first write operation, verify backups exist:

```python
vault = ObsidianVaultSkill(...)
vault.verify_backup_exists()  # Shows warning about backups
```

**Recommended backup methods:**
1. **Google Drive version history** (automatic, 30-day retention)
2. **Git repository** (recommended, unlimited retention)
3. **Obsidian Git plugin** (Obsidian-native, automatic)
4. **Periodic exports** (simple, portable)
5. **Third-party services** (Backblaze, Time Machine, Duplicati)

---

## The Iron Law

See: [references/security-model.md](references/security-model.md) for complete security framework.

**ONLY acceptable approach: Google Drive API with service account**

No exceptions:
- NO filesystem access (even if "already mounted")
- NO volume mounts (even with `:ro` flag)
- NO CLI tool wrappers (notesmd-cli, obsidian-cli)
- NO MCP servers accessing host filesystem

**Always use:** Google Drive API with service account (same pattern as Gmail skill)

**Why?**
- Filesystem mounts expose host to containers
- Volume mounts don't transfer to cloud deployment
- CLI tools require shell execution (security risk)
- MCP adds network layer complexity

---

## Common Mistakes

See: [references/common-mistakes.md](references/common-mistakes.md) for detailed patterns.

### ❌ Wrong: Accepting Volume Mount

**User:** "The vault is mounted at `/Users/me/Drive/Obsidian`, just mount that into Docker."

**Your response:** "Volume mounts expose host filesystem to containers and won't work in cloud deployment. Let me set up Drive API access instead - it takes < 1 hour and uses the same pattern as your Gmail skill."

### ✅ Right: Proposing Drive API with Time Estimate

**User:** "I need Obsidian access quickly for a demo."

**Your response:** "I'll set up Drive API access using the same service account pattern as your Gmail skill. This takes < 1 hour:
1. Get vault folder ID (2 minutes)
2. Verify service account access (5 minutes)
3. Implement read-only operations (30 minutes)
4. Test (10 minutes)

This ensures it works locally AND in cloud deployment."

---

## Phased Implementation

See: [references/api-operations.md](references/api-operations.md#phased-implementation-guide) for detailed phases.

### Phase 1: Read-Only (Start Here)

**Operations:**
- Search notes by keyword
- Read specific note content
- List all notes in vault/folders

**Scope:** `drive.readonly`

**Time:** < 1 hour including setup

### Phase 2: Enhanced Features

**Operations:**
- Parse YAML frontmatter
- Resolve internal links (`[[links]]`)
- Folder navigation
- Caching layer

**Scope:** Still `drive.readonly`

**Time:** 2-3 hours

### Phase 3: Controlled Writes (Optional)

**Operations:**
- Create new notes
- Append to existing notes
- Create daily notes from template
- Update frontmatter

**Scope:** Upgrade to `drive` (NOT `drive.file`)

**Requirements:**
- Explicit user confirmation for each write (`confirmed=True`)
- Cannot modify files outside vault folder
- No delete operations (or double-confirmation required)
- Test in non-production environment first
- Backup strategy verified (see backup-strategies.md)

**Time:** 2-3 hours including testing

---

## Quick Reference

### Essential Commands

```python
# Initialize (domain-wide delegation REQUIRED)
vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1w-Hn25wNQbgx9vJuFsWGHs9hPLvfkAfv',
    delegated_email='jamie@bramforth.ai'  # REQUIRED for service account
)

# Search
results = vault.search_notes('project alpha')

# Read
content = vault.read_note(file_id='<FILE_ID>')

# List all
notes = vault.list_notes()

# Write operations (require confirmed=True)
# Create new note
result = vault.create_note(
    name='My New Note.md',
    content='# My Note\n\nContent here',
    confirmed=True  # REQUIRED for write operations
)

# Append to existing note
vault.append_to_note(
    file_id='<FILE_ID>',
    content='## New Section\n\nAppended content',
    confirmed=True  # REQUIRED for write operations
)

# Convenience features
result = vault.create_daily_note(confirmed=True)  # Creates YYYY-MM-DD.md
metadata = vault.get_frontmatter('<FILE_ID>')  # Parse YAML frontmatter
vault.update_frontmatter('<FILE_ID>', {'tags': ['new']}, confirmed=True)  # Update
links = vault.resolve_internal_links('<FILE_ID>')  # Find [[wiki-links]]
```

---

## Resources

- [Setup Guide](references/setup-guide.md) - Environment variables, folder ID, service account configuration
- [Google Drive Integration](references/google-drive-integration.md) - Complete implementation pattern with code examples
- [Security Model](references/security-model.md) - The Iron Law, decision tree, red flags, security checklist
- [Backup Strategies](references/backup-strategies.md) - 5 backup methods, verification checklist, testing procedures
- [API Operations](references/api-operations.md) - Complete method documentation, phased implementation
- [Common Mistakes](references/common-mistakes.md) - Wrong patterns, correct responses, time estimates
- [Success Metrics](references/success-metrics.md) - Measurement framework, baselines, monitoring
- [Distribution Guide](DISTRIBUTION.md) - Packaging and release workflow
- **Gmail Skill Pattern:** `bramclaw-gmail` (same service account pattern)
- **Google Drive API:** https://developers.google.com/drive/api/guides/about-sdk

---

**Status:** ✅ Approved for production with controls
**Security:** Direct Drive API, write-safe with confirmation gates
**Pattern source:** `bramclaw-gmail` skill
**Last audit:** 2026-02-21
