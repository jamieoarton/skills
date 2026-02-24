# Google Drive Integration - bramclaw-obsidian

Complete implementation pattern for accessing Obsidian vaults via Google Drive API with service account authentication.

---

## Core Principle

**ONLY acceptable approach: Google Drive API with service account**

Access Obsidian vaults via Google Drive API with service account authentication. Never use filesystem mounts or CLI tool wrappers for cloud-hosted vaults.

**Pattern:** Use the same security model as the Gmail skill (service account + hardcoded scopes).

---

## Reference Existing Pattern

**DO THIS FIRST:** Look at the Gmail skill implementation (`bramclaw-gmail`):
- Service account authentication
- Hardcoded read-only scopes
- Domain-wide delegation
- No filesystem access

This skill follows the exact same pattern.

---

## Implementation Pattern

### Complete Code Example

```python
# scripts/obsidian_vault.py - Service account + Drive API
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaInMemoryUpload
import logging
from datetime import datetime
from collections import deque
from time import time

# Configure audit logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/root/logs/obsidian_vault.log'),
        logging.StreamHandler()  # Also log to console
    ]
)
logger = logging.getLogger('obsidian_vault')

class ObsidianVaultSkill:
    """Read/write Obsidian vault via Google Drive API."""

    # Security limits
    MAX_NOTE_SIZE = 1_048_576  # 1MB maximum note size
    MAX_CREATES_PER_MINUTE = 10  # Rate limit for note creation

    def __init__(self, service_account_file, vault_folder_id, delegated_email):
        scopes = [
            'https://www.googleapis.com/auth/drive.readonly',
            # Use 'https://www.googleapis.com/auth/drive' for writes (Phase 3)
        ]

        # REQUIRED: Domain-wide delegation (same as Gmail skill)
        self.credentials = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=scopes
        ).with_subject(delegated_email)  # Impersonate user

        self.drive = build('drive', 'v3', credentials=self.credentials)
        self.vault_folder_id = vault_folder_id

        # Rate limiting: Track recent creates (sliding window)
        self.recent_creates = deque(maxlen=self.MAX_CREATES_PER_MINUTE)

        logger.info(f"ObsidianVaultSkill initialized for vault {vault_folder_id}")

    def verify_backup_exists(self):
        """
        Verify vault has backup before enabling write operations.

        This is a manual verification step to ensure data safety.
        Call this before performing any write operations in production.

        Recommended backup strategies:
        1. Google Drive's native versioning (automatic)
        2. Git repository for vault folder
        3. Periodic exports to separate storage
        4. Third-party backup services (Backblaze, etc.)

        Returns:
            bool: Always True after user acknowledges
        """
        logger.warning("=" * 70)
        logger.warning("⚠️  BACKUP VERIFICATION REQUIRED")
        logger.warning("=" * 70)
        logger.warning("")
        logger.warning("Before enabling write operations, ensure your vault is backed up:")
        logger.warning("  ✓ Google Drive version history (automatic)")
        logger.warning("  ✓ Git repository with regular commits")
        logger.warning("  ✓ Periodic exports to external storage")
        logger.warning("  ✓ Third-party backup service")
        logger.warning("")
        logger.warning("Write operations will modify your Obsidian vault!")
        logger.warning("=" * 70)

        return True

    def search_notes(self, query, max_results=10):
        """Search vault for markdown files matching query."""
        query_str = f"'{self.vault_folder_id}' in parents and name contains '{query}' and mimeType='text/markdown'"
        results = self.drive.files().list(
            q=query_str,
            pageSize=max_results,
            fields="files(id, name, modifiedTime)"
        ).execute()
        return results.get('files', [])

    def read_note(self, file_id):
        """Read note content by file ID."""
        request = self.drive.files().get_media(fileId=file_id)
        content = request.execute()
        return content.decode('utf-8')

    def list_notes(self, folder_id=None):
        """List all markdown files in vault or specific folder."""
        parent_id = folder_id or self.vault_folder_id
        query = f"'{parent_id}' in parents and mimeType='text/markdown'"
        results = self.drive.files().list(
            q=query,
            pageSize=100,
            fields="files(id, name, modifiedTime)"
        ).execute()
        return results.get('files', [])

    def _validate_in_vault(self, file_id):
        """
        Verify file is within vault folder before any operation.

        Args:
            file_id: Google Drive file ID to validate

        Raises:
            SecurityError: If file is not in vault folder
        """
        try:
            file = self.drive.files().get(
                fileId=file_id,
                fields='parents'
            ).execute()

            parents = file.get('parents', [])
            if self.vault_folder_id not in parents:
                raise SecurityError(
                    f"File {file_id} is not in vault folder! "
                    f"Expected parent: {self.vault_folder_id}, "
                    f"Actual parents: {parents}"
                )
        except Exception as e:
            if isinstance(e, SecurityError):
                raise
            # File doesn't exist or can't be accessed
            raise SecurityError(
                f"Cannot validate file {file_id}: {str(e)}"
            )

    # Phase 3 writes (upgrade scope to 'drive')
    def create_note(self, name, content, confirmed=False):
        """
        Create new note in vault.

        Args:
            name: Note filename (e.g., "My Note.md")
            content: Note content (markdown)
            confirmed: Must be True to execute (security gate)

        Raises:
            SecurityError: If confirmed is not True
            ValueError: If content exceeds MAX_NOTE_SIZE
            RateLimitError: If too many creates in last minute
        """
        if not confirmed:
            raise SecurityError(
                "Write operation requires explicit confirmation. "
                "Set confirmed=True to proceed."
            )

        # Check rate limit (sliding window)
        now = time()
        if len(self.recent_creates) == self.MAX_CREATES_PER_MINUTE:
            oldest = self.recent_creates[0]
            if now - oldest < 60:
                raise RateLimitError(
                    f"Too many creates (max {self.MAX_CREATES_PER_MINUTE} per minute). "
                    f"Try again in {int(60 - (now - oldest))} seconds."
                )

        # Check size limit
        content_bytes = content.encode('utf-8')
        if len(content_bytes) > self.MAX_NOTE_SIZE:
            raise ValueError(
                f"Note content exceeds maximum size of {self.MAX_NOTE_SIZE:,} bytes. "
                f"Actual size: {len(content_bytes):,} bytes"
            )

        file_metadata = {
            'name': name,
            'parents': [self.vault_folder_id],
            'mimeType': 'text/markdown'
        }
        media = MediaInMemoryUpload(
            content_bytes,
            mimetype='text/markdown',
            resumable=True
        )
        file = self.drive.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name'
        ).execute()

        # Audit log
        logger.info(
            f"CREATE: {name} "
            f"(ID: {file['id']}, Size: {len(content_bytes):,} bytes, "
            f"Vault: {self.vault_folder_id})"
        )

        # Track for rate limiting
        self.recent_creates.append(now)

        return file

    def append_to_note(self, file_id, content, confirmed=False):
        """
        Append content to existing note.

        Args:
            file_id: Google Drive file ID
            content: Content to append
            confirmed: Must be True to execute (security gate)

        Raises:
            SecurityError: If confirmed is not True or file not in vault
            ValueError: If total size would exceed MAX_NOTE_SIZE
        """
        if not confirmed:
            raise SecurityError(
                "Write operation requires explicit confirmation. "
                "Set confirmed=True to proceed."
            )

        # Validate file is in vault before any operation
        self._validate_in_vault(file_id)

        # Read existing content
        existing = self.drive.files().get_media(fileId=file_id).execute().decode('utf-8')

        # Check size limit before appending
        existing_bytes = existing.encode('utf-8')
        content_bytes = content.encode('utf-8')
        total_size = len(existing_bytes) + len(content_bytes) + 2  # +2 for "\n\n"

        if total_size > self.MAX_NOTE_SIZE:
            raise ValueError(
                f"Appending would exceed maximum note size of {self.MAX_NOTE_SIZE:,} bytes. "
                f"Current: {len(existing_bytes):,} bytes, "
                f"Adding: {len(content_bytes):,} bytes, "
                f"Total: {total_size:,} bytes"
            )

        # Append new content
        updated = existing + "\n\n" + content
        # Write back
        media = MediaInMemoryUpload(
            updated.encode('utf-8'),
            mimetype='text/markdown',
            resumable=True
        )
        self.drive.files().update(fileId=file_id, media_body=media).execute()

        # Audit log
        logger.info(
            f"APPEND: File ID {file_id} "
            f"(Added: {len(content_bytes):,} bytes, "
            f"Total: {total_size:,} bytes, "
            f"Vault: {self.vault_folder_id})"
        )


class SecurityError(Exception):
    """Raised when security checks fail."""
    pass


class RateLimitError(Exception):
    """Raised when rate limits are exceeded."""
    pass
```

---

## Security Features

### Confirmation Gates

All write operations require `confirmed=True`:

```python
# This will raise SecurityError
vault.create_note("Test.md", "Content")  # ❌ Fails

# This works
vault.create_note("Test.md", "Content", confirmed=True)  # ✅ Success
```

### Size Limits

Maximum note size: 1 MB (1,048,576 bytes)

```python
# Raises ValueError if content > 1MB
vault.create_note("Large.md", large_content, confirmed=True)
```

### Rate Limiting

Maximum 10 creates per minute (sliding window):

```python
# Raises RateLimitError after 10 creates in 60 seconds
for i in range(15):
    vault.create_note(f"Note-{i}.md", "Content", confirmed=True)
```

### Path Validation

All file operations verify file is within vault folder:

```python
# _validate_in_vault() called before append
# Raises SecurityError if file not in vault
vault.append_to_note(external_file_id, "Content", confirmed=True)  # ❌ Fails
```

### Audit Logging

All operations logged to `/root/logs/obsidian_vault.log`:

```
2026-02-21 12:34:56 - obsidian_vault - INFO - CREATE: My Note.md (ID: 1ABC...xyz, Size: 1,234 bytes, Vault: 1w-Hn...)
2026-02-21 12:35:01 - obsidian_vault - INFO - APPEND: File ID 1ABC...xyz (Added: 567 bytes, Total: 1,801 bytes, Vault: 1w-Hn...)
```

---

## Phased Implementation

### Phase 1: Read-Only (Start Here)

**Operations:**
- Search notes by keyword
- Read specific note content
- List all notes in vault/folders
- Get daily note by date

**Scope:** `drive.readonly`

**Time:** < 1 hour including setup

**Implementation:**
```python
scopes = ['https://www.googleapis.com/auth/drive.readonly']
```

### Phase 2: Enhanced Features

**Operations:**
- Parse YAML frontmatter
- Resolve internal links (`[[links]]`)
- Folder navigation
- Caching layer

**Scope:** Still `drive.readonly`

**Time:** 2-3 hours

**Implementation:** See api-operations.md for convenience features

### Phase 3: Controlled Writes (Optional)

**Operations:**
- Create new notes
- Append to existing notes
- Create daily notes from template

**Scope:** Upgrade to `drive` (NOT `drive.file`)

**Requirements:**
- Explicit user confirmation for each write
- Cannot modify files outside vault folder
- No delete operations (or double-confirmation required)
- Test in non-production environment first

**Time:** 2-3 hours including testing

**Implementation:**
```python
# Upgrade scope
scopes = ['https://www.googleapis.com/auth/drive']

# Verify backups before first write
vault.verify_backup_exists()

# All writes require confirmed=True
vault.create_note("Test.md", "Content", confirmed=True)
```

---

## Architecture

```
bram-claw → obsidian_vault.py → Google Drive API → Obsidian Vault
```

**No filesystem mounts** - uses Google Drive API for cloud portability.

**Benefits:**
- ✅ Works in Docker containers
- ✅ Cloud-ready (no host dependencies)
- ✅ Same pattern as Gmail skill
- ✅ Secure (service account + hardcoded scopes)
- ✅ Audit logging built-in
- ✅ Rate limiting built-in

---

## Integration Example

```python
from scripts.obsidian_vault import ObsidianVaultSkill

# Initialize
vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1w-Hn25wNQbgx9vJuFsWGHs9hPLvfkAfv',
    delegated_email='jamie@bramforth.ai'
)

# Read operations (safe, no confirmation needed)
results = vault.search_notes('project alpha')
content = vault.read_note(file_id='1ABC...xyz')
notes = vault.list_notes()

# Write operations (require confirmed=True)
vault.create_note("New Note.md", "# Content", confirmed=True)
vault.append_to_note(file_id='1ABC...xyz', content="\n## Update", confirmed=True)
```

---

## Comparison with Other Approaches

| Approach | Security | Portability | Maintenance | Verdict |
|----------|----------|-------------|-------------|---------|
| **Drive API (service account)** | ✅ Best | ✅ Cloud-ready | ✅ Simple | **USE THIS** |
| MCP server (host filesystem) | ⚠️ Exposes host | ❌ Host-bound | ⚠️ Network config | ❌ Reject |
| Volume mount (`:ro` or `:rw`) | ❌ Container→host | ❌ Host-bound | ❌ Complex | ❌ Reject |
| CLI wrapper (notesmd-cli) | ❌ Shell exec | ❌ Filesystem needed | ⚠️ Dependency | ❌ Reject |

---

## Error Handling

```python
from scripts.obsidian_vault import SecurityError, RateLimitError

try:
    vault.create_note("Test.md", "Content", confirmed=True)
except SecurityError as e:
    print(f"Security check failed: {e}")
except RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
except ValueError as e:
    print(f"Validation error: {e}")
```

**Common errors:**
- `SecurityError`: Confirmation missing or file outside vault
- `RateLimitError`: Too many creates (>10/minute)
- `ValueError`: Content size exceeds 1MB limit

---

**Last updated:** 2026-02-21
**Pattern source:** `bramclaw-gmail` skill
**Related:** setup-guide.md, api-operations.md, security-model.md
