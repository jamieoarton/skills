---
name: bramclaw-gmail-delegated-send
description: Use when users ask to send outbound Gmail messages on behalf of another identity with delegated authority, including dry-run validation, sendAs alias preflight checks, allowlist policy enforcement, and auditable send decisions.
---

# bramclaw-gmail-delegated-send

Delegated outbound Gmail send workflow with explicit guardrails.

## Boundary

- Use this skill for outbound delegated send only.
- Do not use this skill for inbox read/search workflows; use `bramclaw-gmail` for read-only tasks.

## Trigger Guidance

Trigger when requests include:
- "send this email on behalf of ..."
- "send as boss from VA account"
- "delegated Gmail send"
- "dry-run before sending email"

Do not trigger for:
- inbox reads/search
- label/archive/delete workflows
- generic Google Workspace admin automation

## Required Environment

- `SERVICE_ACCOUNT_FILE`
- `GMAIL_VA_EMAIL`
- `GMAIL_BOSS_EMAIL`
- `GMAIL_DELEGATED_POLICY_FILE`
- `GMAIL_SEND_MODE` (`dry-run` or `live`)

Optional:
- `GMAIL_AUDIT_LOG_FILE`
- `GMAIL_BOSS_DISPLAY_NAME` (recommended boss display name for `From`, e.g. `Jamie Oarton`)

## Policy Contract

Policy file is JSON and must include `va_to_boss` mapping.

Minimal example:

```json
{
  "va_to_boss": {
    "va@company.com": ["boss@company.com"]
  },
  "recipient_rules": {
    "mode": "allow_domains",
    "domains": ["company.com", "client.com"]
  }
}
```

Supported recipient rules modes:
- `allow_all`
- `allow_domains`
- `deny_domains`
- `allow_addresses`
- `deny_addresses`

Optional approval gate:

```json
"approval_rules": {
  "require_external_on_behalf_approval": true,
  "internal_domains": ["bramforth.ai"],
  "required_token": "CONFIRM_SEND_ON_BEHALF"
}
```

When enabled, external recipients require `--approval-token CONFIRM_SEND_ON_BEHALF`.

## Execution Steps

1. Load policy from `GMAIL_DELEGATED_POLICY_FILE`.
2. Build delegated Gmail credentials with subject `GMAIL_VA_EMAIL`.
3. Validate VA→Boss mapping and recipient constraints.
4. Preflight `users.settings.sendAs.list(userId='me')` for Boss alias.
5. Build MIME with:
   - `From: Boss Display <boss@...>`
   - `Sender: va@...`
   - `X-Google-Sender-Delegation: va@...;`
6. If `GMAIL_SEND_MODE=dry-run`, do not send; output decision payload.
7. If `GMAIL_SEND_MODE=live`, send via `users.messages.send(userId='me')`.
8. Write audit event for every attempt.

## CLI Usage

```bash
python3 scripts/gmail_delegated_send.py \
  --to recipient@example.com \
  --subject "Project update" \
  --text-body "Plain text body" \
  --html-body "<p>Plain text body</p>" \
  --from-display "Boss Name"
```

## Files

- `scripts/gmail_delegated_send.py`: delegated send orchestration, alias preflight, MIME build, audit logging
- `scripts/policy.py`: policy loading + enforcement
- `tests/test_policy.py`: policy allow/deny coverage
- `tests/test_delegated_send.py`: MIME and alias preflight coverage
- `references/setup-guide.md`: setup and operator checks
- `references/sender-from-behavior.md`: `From`/`Sender` behavior notes
- `references/security-guardrails.md`: controls and incident response checklist
