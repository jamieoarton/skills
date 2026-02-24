# Security Guardrails

## Core Controls

1. Default `GMAIL_SEND_MODE=dry-run` in CI and new environments.
2. Enforce VA→Boss allowlist mapping before any send.
3. Optionally enforce recipient rules (`allow_domains`, `deny_domains`, etc.).
4. Require sendAs alias preflight success for Boss identity.
5. Keep secrets in environment/secret store only.
6. Log every attempt (allow/deny/failure) to audit stream.

## Deny Conditions

Reject send on any of:

1. Missing or invalid policy mapping.
2. Recipient not permitted by policy rules.
3. Boss alias missing from Gmail `sendAs`.
4. Alias exists but verification status not accepted (unless explicitly allowed).
5. Missing required environment variables.

## Operational Safety

1. Keep delegated-send and read-only Gmail skills separate.
2. Do not expand read-only skill scopes to include send.
3. Restrict service account key distribution.
4. Rotate service account credentials periodically.
5. Review audit logs for anomalous recipients or spikes.

## Incident Response (Minimal)

1. Set `GMAIL_SEND_MODE=dry-run`.
2. Disable DWD grant for service account if unauthorized sends are suspected.
3. Rotate key material and review policy file integrity.
4. Re-enable live mode only after controls are re-validated.
