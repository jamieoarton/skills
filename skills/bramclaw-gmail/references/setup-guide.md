# Gmail Skill Setup Guide

## Service Account Configuration

**Required environment variables:**
- `SERVICE_ACCOUNT_FILE` - Path to service account JSON key
- `EMAIL_ACCOUNT` - Default mailbox to impersonate (e.g. boss-a@bramforth.ai)

**Optional mailbox controls:**
- `GMAIL_READ_POLICY_FILE` - JSON allowlist file for readable mailboxes
- `GMAIL_ALLOWED_READ_MAILBOXES` - Comma-separated allowlist fallback

## Service Account Setup

### Step 1: Create Service Account

1. Go to Google Cloud Console → IAM & Admin → Service Accounts
2. Click "Create Service Account"
3. Name: "bramclaw-gmail"
4. Grant roles: None needed (domain-wide delegation)

### Step 2: Enable Domain-Wide Delegation

1. Click on service account
2. Navigate to "Advanced Settings"
3. Enable "Enable Google Workspace Domain-wide Delegation"
4. Note the Client ID

### Step 3: Configure Workspace Delegation

1. Go to admin.google.com → Security → API Controls
2. Click "Manage Domain-wide Delegation"
3. Add Client ID from Step 2
4. Scopes: `https://www.googleapis.com/auth/gmail.readonly`

### Step 4: Download Key

1. Service Accounts → Keys → Add Key → JSON
2. Save to `/root/.openclaw/credentials/service-account.json`

### Step 5: Configure Environment

Add to `.env`:
```bash
SERVICE_ACCOUNT_FILE=/root/.openclaw/credentials/service-account.json
EMAIL_ACCOUNT=boss-a@bramforth.ai
GMAIL_READ_POLICY_FILE=/root/.openclaw/gmail-read-policy.json
GMAIL_ALLOWED_READ_MAILBOXES=va@bramforth.ai,boss-a@bramforth.ai,boss-b@bramforth.ai
```

Use one skill for VA + multiple seniors by setting `EMAIL_ACCOUNT` as default and switching per call with `--mailbox`.

Seed a policy file:
```bash
cp config/gmail-read-policy.example.json config/gmail-read-policy.json
chmod 600 config/gmail-read-policy.json
```

## Verification

Test authentication:
```bash
python3 scripts/gmail_agent.py subjects 1
python3 scripts/gmail_agent.py subjects 5 --mailbox boss-b@bramforth.ai
```

Expected: Shows 1 email subject (or error if no emails)

## Troubleshooting

**Error: "Unauthorized client or scope not requested"**
- Check domain-wide delegation is enabled
- Verify scope in admin console: `gmail.readonly`

**Error: "Service account file not found"**
- Check path in `SERVICE_ACCOUNT_FILE`
- Verify file permissions (readable)

**Error: "Impersonation failed"**
- Check `EMAIL_ACCOUNT` is correct
- Verify service account has delegation for this user
