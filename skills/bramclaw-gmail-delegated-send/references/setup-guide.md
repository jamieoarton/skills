# Setup Guide

## Prerequisites

1. Gmail API enabled in the Google Cloud project.
2. Service account created with domain-wide delegation enabled.
3. Admin console grants Gmail send scope to that service account client ID.
4. VA mailbox can send as Boss alias in Gmail settings.

## Required Scope

- `https://www.googleapis.com/auth/gmail.send`
- `https://www.googleapis.com/auth/gmail.settings.basic` (required for `sendAs` alias preflight checks)

Keep this scope isolated from read/search skill scope.

## Environment Variables

```bash
export SERVICE_ACCOUNT_FILE="/secure/path/service-account.json"
export GMAIL_VA_EMAIL="va@company.com"
export GMAIL_BOSS_EMAIL="boss@company.com"
export GMAIL_DELEGATED_POLICY_FILE="/secure/path/delegated-policy.json"
export GMAIL_SEND_MODE="dry-run"
export GMAIL_AUDIT_LOG_FILE=".claude/skills/bramclaw-gmail-delegated-send/logs/audit.jsonl"
export GMAIL_BOSS_DISPLAY_NAME="Boss Name"
```

Seed policy template:

```bash
cp config/gmail-delegated-policy.example.json /secure/path/delegated-policy.json
```

## First-Run Operator Checklist

1. Run in `dry-run` mode.
2. Confirm alias preflight passes for Boss email.
3. Confirm policy allows expected VA→Boss pair.
4. Confirm blocked recipients are denied.
5. Switch to `live` only after dry-run output is correct.
6. For external on-behalf sends, pass `--approval-token CONFIRM_SEND_ON_BEHALF` when approval gate is enabled.

## Manual Live Validation

1. Send to a test mailbox.
2. Inspect received headers for `From`, `Sender`, and `X-Google-Sender-Delegation`.
3. Confirm audit log contains success result with message id.
4. Roll back to dry-run if header behavior is not as expected.
