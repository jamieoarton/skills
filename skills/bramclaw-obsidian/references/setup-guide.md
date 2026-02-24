# Setup Guide - bramclaw-obsidian

Complete guide for configuring Obsidian vault access via Google Drive API.

---

## Prerequisites

- Obsidian vault synced to Google Drive
- Service account with domain-wide delegation enabled
- Access to OpenClaw container environment

---

## Environment Variables

Configure these in Docker Compose `env_file` or `.env`:

### Required Variables

```bash
# Your Obsidian vault's Google Drive folder ID
OBSIDIAN_VAULT_FOLDER_ID=1w-Hn25wNQbgx9vJuFsWGHs9hPLvfkAfv

# Email to impersonate (must match your Google Workspace account)
OBSIDIAN_DELEGATED_EMAIL=jamie@bramforth.ai
```

### Optional Variables (with sensible defaults)

```bash
# Service account credentials file location
SERVICE_ACCOUNT_FILE=/root/.openclaw/credentials/service-account.json

# Audit log file location
OBSIDIAN_LOG_FILE=/root/logs/obsidian_vault.log
```

---

## Service Account Requirements

Your service account must have:

1. **Domain-wide delegation enabled**
   - Required for impersonating user email
   - Same pattern as bramclaw-gmail skill

2. **Access to vault folder**
   - Share folder with service account email in Google Drive
   - Grant "Viewer" or "Editor" role as needed

3. **Required OAuth scope**
   - `https://www.googleapis.com/auth/drive.readonly` (Phase 1 - read-only)
   - `https://www.googleapis.com/auth/drive` (Phase 3 - with writes)

---

## Getting Your Vault Folder ID

Extract the folder ID from Google Drive:

### Step 1: Navigate to Vault in Google Drive

Open your Obsidian vault folder in the Google Drive web interface.

### Step 2: Extract ID from URL

The URL format is:
```
https://drive.google.com/drive/folders/1ABC...xyz
```

Extract the ID:
```
1ABC...xyz  ← This is your OBSIDIAN_VAULT_FOLDER_ID
```

### Step 3: Verify Access

Ensure the service account email has access to this folder:
- Right-click folder → "Share"
- Add service account email (e.g., `openclaw@project.iam.gserviceaccount.com`)
- Grant "Viewer" or "Editor" permission

---

## Setup Steps

### 1. Get Vault Folder ID (2 minutes)

Follow steps above to extract folder ID from Google Drive URL.

### 2. Verify Service Account Access (5 minutes)

```bash
# Check if service account can access folder
python3 -c "
from google.oauth2 import service_account
from googleapiclient.discovery import build

credentials = service_account.Credentials.from_service_account_file(
    '/root/.openclaw/credentials/service-account.json',
    scopes=['https://www.googleapis.com/auth/drive.readonly']
).with_subject('jamie@bramforth.ai')

drive = build('drive', 'v3', credentials=credentials)
folder = drive.files().get(fileId='YOUR_FOLDER_ID').execute()
print(f\"Access verified: {folder['name']}\")
"
```

Expected output:
```
Access verified: MyVault
```

### 3. Configure Environment Variables

Add to `.env` or Docker Compose `env_file`:

```bash
OBSIDIAN_VAULT_FOLDER_ID=1ABC...xyz
OBSIDIAN_DELEGATED_EMAIL=your-email@domain.com
```

### 4. Test Read Operations (10 minutes)

```python
from scripts.obsidian_vault import ObsidianVaultSkill

vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1ABC...xyz',
    delegated_email='your-email@domain.com'
)

# Search notes
results = vault.search_notes('project alpha')
print(f"Found {len(results)} notes")

# Read specific note
content = vault.read_note(file_id=results[0]['id'])
print(content[:200])

# List all notes
notes = vault.list_notes()
print(f"Total notes: {len(notes)}")
```

### 5. Add Writes Later (Phase 3 - Optional)

When ready for write operations:

1. **Upgrade scope** to `https://www.googleapis.com/auth/drive`
2. **Verify backups exist** (see backup-strategies.md)
3. **Test in non-production** environment first
4. **Call `verify_backup_exists()`** before first write

---

## Initialization Pattern

### Python API

```python
from scripts.obsidian_vault import ObsidianVaultSkill

# Initialize with domain-wide delegation (REQUIRED)
vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1w-Hn25wNQbgx9vJuFsWGHs9hPLvfkAfv',
    delegated_email='jamie@bramforth.ai'  # REQUIRED for service account
)
```

### Environment-Based

```python
import os
from scripts.obsidian_vault import ObsidianVaultSkill

# Load from environment variables
vault = ObsidianVaultSkill(
    service_account_file=os.getenv('SERVICE_ACCOUNT_FILE'),
    vault_folder_id=os.getenv('OBSIDIAN_VAULT_FOLDER_ID'),
    delegated_email=os.getenv('OBSIDIAN_DELEGATED_EMAIL')
)
```

---

## Time Estimates

| Task | Time | Notes |
|------|------|-------|
| Get vault folder ID | 2 min | Extract from Google Drive URL |
| Verify service account access | 5 min | Check permissions, grant if needed |
| Implement Phase 1 (read-only) | 30 min | Copy Gmail skill pattern |
| Test read operations | 10 min | Search, read, list |
| **Total for working read-only** | **< 1 hour** | Production-ready |
| Add Phase 3 writes | 2-3 hours | Includes testing, safeguards |

---

## Troubleshooting

### Error: "Access token not found"

**Cause:** Service account credentials not accessible

**Solution:**
```bash
# Verify credentials file exists
ls -la /root/.openclaw/credentials/service-account.json

# Check environment variable is set
echo $SERVICE_ACCOUNT_FILE
```

### Error: "File not found" (404)

**Cause:** Service account doesn't have access to folder

**Solution:**
1. Go to Google Drive web interface
2. Right-click vault folder → "Share"
3. Add service account email
4. Grant "Viewer" or "Editor" permission

### Error: "Invalid grant: account not found"

**Cause:** Domain-wide delegation not enabled or wrong email

**Solution:**
1. Verify domain-wide delegation is enabled for service account
2. Check `OBSIDIAN_DELEGATED_EMAIL` matches your Google Workspace account
3. Ensure scope `https://www.googleapis.com/auth/drive` is authorized in Google Workspace Admin

### Error: "Insufficient permissions"

**Cause:** Service account scope doesn't include Drive API

**Solution:**
```python
# Verify scopes in code
scopes = [
    'https://www.googleapis.com/auth/drive.readonly',  # For read-only
    # OR
    'https://www.googleapis.com/auth/drive'  # For writes
]
```

---

## Security Checklist

**Before deployment:**
- [ ] Using Drive API (not filesystem/CLI/MCP)
- [ ] Service account authentication
- [ ] Hardcoded `drive.readonly` scope initially
- [ ] Vault folder ID validated
- [ ] No volume mounts in Docker config
- [ ] No shell execution (`exec` tool)
- [ ] Follows same pattern as Gmail skill

**If adding writes:**
- [ ] Using `drive` scope (NOT `drive.file`)
- [ ] Explicit confirmation for write operations
- [ ] Path validation (stays within vault)
- [ ] Tested in non-production first
- [ ] Backup strategy verified (see backup-strategies.md)
- [ ] Called `verify_backup_exists()` before first write

---

**Last updated:** 2026-02-21
**Related:** api-operations.md, security-model.md, backup-strategies.md
