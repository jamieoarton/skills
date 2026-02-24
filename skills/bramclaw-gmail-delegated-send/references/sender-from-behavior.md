# Sender and From Behavior

Delegated send uses distinct identity headers:

- `From`: principal identity (Boss)
- `Sender`: actual sending mailbox (VA)
- `X-Google-Sender-Delegation`: explicit delegated marker (`va@...;`)

Example:

- `From: Boss Name <boss@company.com>`
- `Sender: va@company.com`
- `X-Google-Sender-Delegation: va@company.com;`

## Why this matters

1. Preserves principal-facing identity in recipient clients.
2. Maintains standards-compliant indication of transmitting account.
3. Supports auditability and policy review.

## Caveats

1. Some downstream relays or clients may rewrite display behavior.
2. Exact rendering can differ between Gmail web, mobile, and external clients.
3. Always validate with a test send in the real receiving environment.

## Validation

After live test send, inspect raw headers in recipient mailbox and verify all three headers are present.
