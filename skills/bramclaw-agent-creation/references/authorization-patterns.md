# Authorization Governance Patterns

Quick reference for implementing authorization gates in worker agents.

**Source:** @docs/agent-action-governance.md

---

## Standard Header Format

**Every delegated task to a worker must include:**

```text
MODE: observe|propose|execute|execute_high_impact
ACTION_CLASS: READ|WRITE|HIGH_IMPACT
ACTION_TYPE: CREATE|UPDATE|DELETE|SEND|OTHER
CONFIRMATION_TOKEN: <optional for READ, required for WRITE/HIGH_IMPACT as per policy>
```

**For account-bound systems, add:**

```text
ACCOUNT_SCOPE: principal|assistant|auto
```

---

## Action Classes

| Class | Examples | Default Behavior |
|-------|----------|------------------|
| **READ** | List tasks, search emails, get database records | Execute directly, no token required |
| **WRITE** | Create task, update record, draft email | Require token OR trusted system exception |
| **HIGH_IMPACT** | Delete task, send email, drop database table | Always require token, no exceptions |

---

## Execution Modes

| Mode | Meaning | When to Use |
|------|---------|-------------|
| `observe` | Read-only, gather data | Default for all requests |
| `propose` | Create plan/draft, don't execute | WRITE actions without token |
| `execute` | Run approved WRITE actions | WRITE with token OR trusted system exception |
| `execute_high_impact` | Run HIGH_IMPACT actions | HIGH_IMPACT with correct token only |

---

## Token Requirements

| Action Class | Action Type | Token Required? | Exception |
|--------------|-------------|-----------------|-----------|
| READ | Any | No | - |
| WRITE | CREATE, UPDATE | **No** if trusted system* | bram-clickup, bram-obsidian |
| WRITE | CREATE, UPDATE | **Yes** otherwise | All other workers |
| WRITE | DELETE, SEND | **Yes, always** | No exceptions |
| HIGH_IMPACT | Any | **Yes, always** | No exceptions |

**Trusted internal systems:** `bram-clickup`, `bram-obsidian`

---

## Token Formats

| Purpose | Token Format |
|---------|--------------|
| WRITE actions | `CONFIRM_WRITE:<short-id>` |
| HIGH_IMPACT actions | `CONFIRM_HIGH_IMPACT:<short-id>` |
| External on-behalf email | `CONFIRM_SEND_ON_BEHALF` |

**Short ID:** 4-8 character random string, single-use per operation

---

## Implementation Pattern (Workers)

**In AGENTS.md, include this section:**

```markdown
## Authorization Gates (Strict)

You must parse task headers when present:

1. `MODE: observe|propose|execute|execute_high_impact`
2. `ACTION_CLASS: READ|WRITE|HIGH_IMPACT`
3. `ACTION_TYPE: CREATE|UPDATE|DELETE|SEND|OTHER`
4. `CONFIRMATION_TOKEN: ...` (required only when policy says so)
5. `ACCOUNT_SCOPE: principal|assistant|auto` (for account-bound systems)

Enforcement:

1. If `ACTION_CLASS` is `READ`, execute read-only lookup/reporting.
2. If `ACTION_CLASS` is `WRITE` and `ACTION_TYPE` is `CREATE` or `UPDATE` in `MODE: execute`:
   {IF_TRUSTED}: you may execute without token
   {IF_NOT_TRUSTED}: require `CONFIRM_WRITE:<id>`; otherwise return proposal only
3. If `ACTION_CLASS` is `WRITE` and `ACTION_TYPE` is `DELETE` or `SEND`, require token; otherwise return proposal only
4. If `ACTION_CLASS` is `HIGH_IMPACT`, require `CONFIRM_HIGH_IMPACT:<id>`; otherwise return proposal only
5. If headers are missing/ambiguous, default to read-only
```

---

## Dispatcher Pattern (Sending to Workers)

**When dispatcher (bram-router) delegates to worker:**

```markdown
MODE: {mode}
ACTION_CLASS: {class}
ACTION_TYPE: {type}
CONFIRMATION_TOKEN: {token if required}
ACCOUNT_SCOPE: {scope if account-bound}

{Task description with context}
```

**Example - READ operation:**

```
MODE: observe
ACTION_CLASS: READ
ACTION_TYPE: OTHER
ACCOUNT_SCOPE: principal

Check email inbox for unread messages from Supabase
```

**Example - Trusted WRITE operation (ClickUp):**

```
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: CREATE
ACCOUNT_SCOPE: assistant

Create task "Follow up with client XYZ" in list 901519828747, assigned to Jamie, due tomorrow, priority high
```

**Example - Non-trusted WRITE operation (requires token):**

```
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: SEND
CONFIRMATION_TOKEN: CONFIRM_SEND_ON_BEHALF
ACCOUNT_SCOPE: principal

Send email reply to john@example.com with subject "Re: Q2 Roadmap" and body...
```

**Example - HIGH_IMPACT operation:**

```
MODE: execute_high_impact
ACTION_CLASS: HIGH_IMPACT
ACTION_TYPE: DELETE
CONFIRMATION_TOKEN: CONFIRM_HIGH_IMPACT:a7f3
ACCOUNT_SCOPE: principal

Delete ClickUp task 86c8d0twh after confirming it's a duplicate
```

---

## Account Scope Patterns

**For account-bound systems (ClickUp, Gmail, etc.):**

### Principal Scope

```text
ACCOUNT_SCOPE: principal
```

**Use when:**
- User asks about "my tasks", "my inbox", "my email"
- Reading/writing principal's data
- Operations on behalf of the user

**Credentials:** Principal API key/OAuth token

### Assistant Scope

```text
ACCOUNT_SCOPE: assistant
```

**Use when:**
- User asks about "your tasks", "Pepper's inbox", "do you have..."
- Creating tasks FOR principal (assigned to principal, created by assistant)
- Operations by the assistant's account

**Credentials:** Assistant API key/OAuth token

### Auto Scope

```text
ACCOUNT_SCOPE: auto
```

**Use when:**
- Scope genuinely ambiguous
- Falls back to configured default (typically principal)

**Note:** Prefer explicit principal/assistant over auto

---

## Confirmation Workflow

### Read-Only (No Confirmation Needed)

```
User: "Check my email for messages from Supabase"

Dispatcher → Worker:
MODE: observe
ACTION_CLASS: READ
ACTION_TYPE: OTHER

Worker: Executes immediately, returns results
```

### Trusted WRITE (No Token Needed)

```
User: "Create a ClickUp task for following up with client XYZ"

Dispatcher → Worker:
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: CREATE

Worker: Executes immediately (trusted system exception)
```

### Non-Trusted WRITE (Token Required)

```
User: "Draft an email reply to john@example.com"

Dispatcher → Worker (Step 1 - Draft):
MODE: propose
ACTION_CLASS: WRITE
ACTION_TYPE: SEND

Worker: Returns draft, does NOT send

Dispatcher → User: Shows draft, asks for confirmation

User: "Send it"

Dispatcher → Worker (Step 2 - Send):
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: SEND
CONFIRMATION_TOKEN: CONFIRM_SEND_ON_BEHALF

Worker: Sends email, returns confirmation
```

### HIGH_IMPACT (Always Requires Token)

```
User: "Actually delete that duplicate task"

Dispatcher → Worker (Step 1 - Proposal):
MODE: propose
ACTION_CLASS: HIGH_IMPACT
ACTION_TYPE: DELETE

Worker: Returns what will be deleted, does NOT delete

Dispatcher → User: Shows preflight, asks for HIGH_IMPACT confirmation

User: "Yes, delete it - confirm: a7f3"

Dispatcher → Worker (Step 2 - Execute):
MODE: execute_high_impact
ACTION_CLASS: HIGH_IMPACT
ACTION_TYPE: DELETE
CONFIRMATION_TOKEN: CONFIRM_HIGH_IMPACT:a7f3

Worker: Deletes task, returns confirmation
```

---

## Error Handling

**If headers missing:**
- Default to `MODE: observe`, `ACTION_CLASS: READ`
- Never assume write permission
- Ask dispatcher for clarification

**If token invalid:**
- Downgrade to `propose` mode
- Return plan without executing
- State: "Missing/invalid confirmation token - returning proposal only"

**If mode/class conflict:**
- Example: `MODE: execute` but `ACTION_CLASS: READ`
- Use most restrictive interpretation
- Log warning about header inconsistency

---

## Security Principles

1. **Default deny** - Read-only unless explicitly authorized
2. **Least privilege** - Minimal permissions per worker
3. **Explicit approval** - No inferred permissions
4. **Audit trail** - Log all authorization decisions
5. **No shortcuts** - Never bypass gates due to convenience

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Assuming WRITE permission | Always check MODE and ACTION_CLASS |
| Skipping token validation | Validate token format and presence |
| Treating all workers as trusted | Only bram-clickup and bram-obsidian are trusted |
| Executing HIGH_IMPACT without token | HIGH_IMPACT ALWAYS requires token |
| Using auto scope everywhere | Prefer explicit principal/assistant |
| No preflight for HIGH_IMPACT | Show what will happen before executing |

---

## Testing Authorization Gates

**Test each worker with:**

1. **READ without headers** → Should execute
2. **WRITE without headers** → Should default to read-only
3. **CREATE with MODE: execute, no token, TRUSTED SYSTEM** → Should execute
4. **CREATE with MODE: execute, no token, NON-TRUSTED** → Should propose only
5. **DELETE with MODE: execute, no token** → Should propose only
6. **DELETE with MODE: execute, valid token** → Should execute
7. **HIGH_IMPACT without token** → Should propose only
8. **HIGH_IMPACT with invalid token** → Should propose only
9. **HIGH_IMPACT with valid token** → Should execute

---

**Reference complete.** Use this pattern for all bramclaw worker agents.

**Full specification:** @docs/agent-action-governance.md
