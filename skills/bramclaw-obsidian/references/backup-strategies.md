# Backup Strategies - bramclaw-obsidian

Comprehensive backup strategies for Obsidian vaults before enabling write operations.

---

## CRITICAL Requirement

**Always ensure your vault is backed up before enabling write operations.**

Call `verify_backup_exists()` before first write to acknowledge backup verification.

---

## Recommended Backup Methods

### 1. Google Drive Version History (Automatic)

**Effort:** None (built-in)

**Retention:** 30 days for free accounts, longer for paid

**Recovery:** Right-click file → "Version history"

**Pros:**
- Automatic, no setup required
- Built into Google Drive
- No additional cost

**Cons:**
- Limited retention (30 days free)
- Not exportable
- Requires Google Drive access to restore

**Setup:**
```
No setup required - Google Drive automatically tracks file versions
```

---

### 2. Git Repository (Recommended)

**Effort:** Initial setup + automated commits

**Retention:** Unlimited with remote repository

**Recovery:** `git checkout <commit>`

**Pros:**
- Full history (unlimited retention)
- Works offline
- Industry standard version control
- Can push to GitHub/GitLab for remote backup

**Cons:**
- Requires git knowledge
- Manual setup required

**Setup:**
```bash
# Initialize git in vault folder
cd ~/Drive/Obsidian/MyVault
git init
git add .
git commit -m "Initial vault backup"

# Add remote repository (GitHub/GitLab)
git remote add origin https://github.com/username/vault-backup.git
git push -u origin main

# Set up daily backups (cron)
0 2 * * * cd ~/Drive/Obsidian/MyVault && git add -A && git commit -m "Daily backup $(date)" && git push
```

**Testing:**
```bash
# Verify backup works
cd ~/Drive/Obsidian/MyVault
git log  # Shows commit history
git status  # Shows current state

# Test restore (in separate directory)
cd /tmp
git clone https://github.com/username/vault-backup.git
cd vault-backup
git checkout <commit-hash>  # Restore specific version
```

---

### 3. Obsidian Git Plugin

**Effort:** Install plugin, configure schedule

**Retention:** Unlimited (pushes to GitHub/GitLab)

**Recovery:** Git tools or plugin interface

**Pros:**
- Obsidian-native (works within app)
- Automatic commits on schedule
- Visual interface for commits
- Can push to remote automatically

**Cons:**
- Requires Obsidian desktop app
- Plugin dependency

**Setup:**
1. Open Obsidian
2. Settings → Community Plugins
3. Browse → Search "Obsidian Git"
4. Install and enable
5. Configure backup schedule (e.g., every 10 minutes)
6. Add remote repository URL

**Testing:**
```
1. Open Obsidian
2. Command palette → "Obsidian Git: Open diff view"
3. Verify commits are being made
4. Check remote repository (GitHub/GitLab) for pushed commits
```

---

### 4. Periodic Exports

**Effort:** Automated script

**Retention:** As long as you keep files

**Recovery:** Unzip to restore

**Pros:**
- Simple, portable
- No git knowledge required
- Can store anywhere (external drive, cloud)

**Cons:**
- Takes storage space
- Not differential (full backup each time)
- No fine-grained version history

**Setup:**
```python
# Example: Export vault to timestamped ZIP
from datetime import datetime
import shutil
import os

vault_path = "/path/to/vault"
backup_dir = "/backups/obsidian"
backup_path = f"{backup_dir}/vault-{datetime.now().strftime('%Y%m%d')}.zip"

# Create backup directory if needed
os.makedirs(backup_dir, exist_ok=True)

# Create ZIP backup
shutil.make_archive(backup_path.replace('.zip', ''), 'zip', vault_path)
print(f"Backup created: {backup_path}")
```

**Cron schedule (daily at 2 AM):**
```bash
0 2 * * * python3 /path/to/backup_script.py
```

**Testing:**
```bash
# Verify ZIP contains vault files
unzip -l /backups/obsidian/vault-20260221.zip

# Test restore
cd /tmp
unzip /backups/obsidian/vault-20260221.zip -d restored-vault
ls -la restored-vault  # Verify files restored
```

---

### 5. Third-Party Backup Services

**Effort:** Install + configure service

**Retention:** Service-dependent

**Recovery:** Service's restore interface

**Options:**
- **Backblaze:** Continuous backup of entire Drive folder
- **Time Machine (macOS):** Built-in backup (if vault synced locally)
- **Duplicati:** Open-source, encrypted backups

**Pros:**
- Set-and-forget
- Often encrypted
- Professional restore workflows

**Cons:**
- Cost (subscription or storage fees)
- Requires local sync (for Google Drive vaults)
- Service dependency

**Setup (Backblaze example):**
```
1. Install Backblaze client
2. Configure to back up Google Drive folder
3. Verify vault folder is included in backup
4. Wait for initial backup to complete
5. Test restore through Backblaze web interface
```

---

## Backup Verification Checklist

**Before enabling write operations:**

- [ ] Identify backup method (choose from above)
- [ ] Verify backup is active and recent
- [ ] **Test restore process** (critical!)
- [ ] Document recovery procedure
- [ ] Set calendar reminder to check backups monthly

---

## Testing Your Backup

### In Code (Before First Write)

```python
from scripts.obsidian_vault import ObsidianVaultSkill

# Call verify_backup_exists() before first write
vault = ObsidianVaultSkill(
    service_account_file='/root/.openclaw/credentials/service-account.json',
    vault_folder_id='1ABC...xyz',
    delegated_email='your-email@domain.com'
)

vault.verify_backup_exists()  # Shows warning, confirms you're aware

# Then proceed with writes
vault.create_note("Test.md", "Content", confirmed=True)
```

**Output:**
```
======================================================================
⚠️  BACKUP VERIFICATION REQUIRED
======================================================================

Before enabling write operations, ensure your vault is backed up:
  ✓ Google Drive version history (automatic)
  ✓ Git repository with regular commits
  ✓ Periodic exports to external storage
  ✓ Third-party backup service

Write operations will modify your Obsidian vault!
======================================================================
```

---

## Production Setup Workflow

1. **Choose backup method** (git recommended)
2. **Set up automated backups** (cron for git commits)
3. **Test restore process** (actually restore a file!)
4. **Document for team** (write down restore steps)
5. **Call `verify_backup_exists()`** to acknowledge
6. **Set monthly reminder** to verify backups still working

---

## Recovery Testing Examples

### Git Recovery Test

```bash
# 1. Make test change
cd ~/Drive/Obsidian/MyVault
echo "Test content" > test-file.md
git add test-file.md
git commit -m "Test change for recovery"

# 2. Intentionally "break" vault
rm test-file.md

# 3. Recover from git
git checkout HEAD -- test-file.md
cat test-file.md  # Should show "Test content"

# 4. If that worked, your backup is functional!
```

### ZIP Export Recovery Test

```bash
# 1. Create test backup
python3 backup_script.py  # Creates vault-20260221.zip

# 2. Test restore in /tmp
cd /tmp
unzip /backups/obsidian/vault-20260221.zip -d test-restore

# 3. Verify files
ls -la test-restore
cat test-restore/some-note.md

# 4. If files are correct, your backup works!
```

---

## Backup Monitoring

**Set up alerts for backup failures:**

### Git Backup Monitoring

```bash
# Add to cron script
#!/bin/bash
cd ~/Drive/Obsidian/MyVault

git add -A
git commit -m "Daily backup $(date)"

if git push; then
    echo "Backup successful" | logger
else
    echo "BACKUP FAILED!" | logger
    # Send alert (email, Slack, etc.)
fi
```

### Export Backup Monitoring

```python
import smtplib
from datetime import datetime

try:
    # Create backup
    shutil.make_archive(backup_path, 'zip', vault_path)
    print(f"Backup successful: {backup_path}")
except Exception as e:
    # Send alert email
    msg = f"Obsidian backup failed: {e}"
    # ... email sending code ...
    raise
```

---

## Backup Best Practices

1. **Multiple backups:** Use at least 2 methods (e.g., Git + Google Drive history)
2. **Test regularly:** Perform recovery test monthly
3. **Remote storage:** Keep at least one backup off-site (GitHub, external drive)
4. **Automate:** Don't rely on manual backups
5. **Monitor:** Set up alerts for backup failures
6. **Document:** Write down recovery steps for team

---

## When NOT to Enable Writes

**Do NOT enable write operations if:**
- ❌ No backup exists
- ❌ Backup is untested
- ❌ Last backup is > 1 week old
- ❌ Unsure how to restore from backup
- ❌ Only using Google Drive version history (30-day retention)

**Wait until:**
- ✅ Git repository set up with remote
- ✅ Test restore successful
- ✅ Automated backups configured
- ✅ Team knows recovery procedure

---

**Last updated:** 2026-02-21
**Related:** google-drive-integration.md, security-model.md
