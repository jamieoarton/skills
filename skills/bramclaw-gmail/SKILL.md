---
name: bramclaw-gmail
description: Use when users ask to read or search Gmail inbox messages, subjects, senders, dates, or attachment-related email queries via delegated service-account access.
---

**Version:** 2.0.0 | [Changelog](CHANGELOG.md) | **Status:** ✅ Production

---

# bramclaw-gmail

Read-only Gmail access for bram-claw using service account authentication.

## When This Skill Should Trigger

**✅ Should trigger for:**
- "Show me recent Gmail subjects"
- "Search my email for invoices from last week"
- "Check my inbox for unread messages"
- "Get emails from sender@example.com"
- "Find emails with attachments from February"
- Email notification: "You have new messages from..."

**❌ Should NOT trigger for:**
- "Send an email" (write operation - not implemented)
- "Create a draft" (write operation - not implemented)
- "Mark as read" (write operation - not implemented)
- "Check my calendar" (different service)
- "Check my tasks" (different service)

**⚠️ Ambiguous (ask for clarification):**
- "Check my mail" (Gmail? Local mail? Which account?)
- "Search for project alpha" (Email? Files? Code?)

## Skill Confidence

**High confidence (>90%):**
- Explicit mention of "Gmail", "email", "inbox", "messages"
- User asking to read/search/list emails
- Email alert context

**Medium confidence (50-90%):**
- Generic "mail" or "messages" (could be email or other messaging)
- Context suggests email but not explicit

**Low confidence (<50%):**
- Generic search request without email context
- Ambiguous "check" without specifying email

## Success Metrics

See: [references/success-metrics.md](references/success-metrics.md) for detailed measurement framework.

**Key Targets:**
- **Triggering accuracy:** >90% (vs. generic email queries)
- **Token reduction:** >70% (10K → <3K tokens per task)
- **API efficiency:** 1 call success (vs. 6-10 exploratory calls)
- **Error rate:** 0% unhandled errors for supported operations

**Current Performance (2026-02-21):**
- Triggering: Not yet measured (baseline needed)
- Tokens: ~2K with skill vs. ~10K without (80% reduction ✅)
- API calls: 1 vs. 6-10 (90% reduction ✅)
- Errors: 0% for valid operations ✅

## When to Use This Skill

**Decision Framework:**

```plaintext
Need Gmail access?
    ├─ Yes → Read-only operations?
    │         ├─ Yes → Use bramclaw-gmail ✅
    │         └─ No (send/modify) → Use Gmail UI or API directly ❌
    └─ No → Different service
```

**Use bramclaw-gmail when:**
- ✅ Reading email metadata (from, subject, date)
- ✅ Searching emails with filters
- ✅ Listing recent messages
- ✅ Getting specific message details
- ✅ Agent needs automated email monitoring
- ✅ Quick inbox checks without UI

**Do NOT use bramclaw-gmail when:**
- ❌ Sending emails (not implemented - security)
- ❌ Creating drafts (not implemented)
- ❌ Modifying labels/status (not implemented)
- ❌ Deleting messages (not implemented)
- ❌ Complex email threading analysis (use Gmail UI)

**Alternatives Comparison:**

| Need | bramclaw-gmail | Gmail UI | Gmail MCP | Raw API |
|------|----------------|----------|-----------|---------|
| **Read emails** | ✅ Best | ⚠️ Manual | ✅ Good | ⚠️ Complex |
| **Search with filters** | ✅ Best | ✅ Good | ✅ Good | ⚠️ Complex |
| **Send emails** | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes |
| **Automated monitoring** | ✅ Best | ❌ No | ✅ Good | ⚠️ Complex |
| **Agent-friendly** | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| **Setup complexity** | ⚠️ Medium | ✅ Easy | ⚠️ Medium | ❌ High |

**Recommendation:**
- **For agents:** Use bramclaw-gmail (clean interface, no write risk)
- **For users:** Use Gmail UI (full features, visual)
- **For complex workflows:** Consider Gmail MCP (more features than this skill)

## Testing

See: [tests/TEST-PLAN.md](tests/TEST-PLAN.md) for comprehensive test plan.

**Quick validation:**
```bash
# Test authentication
python3 tests/gmail_test.py

# Test CLI interface
python3 scripts/gmail_agent.py subjects 5
```

**Test coverage:**
- ✅ Authentication (valid, invalid, missing credentials)
- ✅ Read operations (list, search, get, empty results)
- ✅ Error handling (rate limits, invalid IDs)
- ⬜ Trigger patterns (manual Claude testing)
- ⬜ Performance metrics (token usage, API efficiency)

## Usage

### Get Email Subjects (Clean Output)

```bash
# Get 5 most recent subjects (clean list)
python3 gmail_agent.py subjects 5
```

**Output:**
```
1. Your Pabau code: D6O72O
2. RE:[CASE 12152933122] Your Account: Close Account
3. Re: Moving today
4. Security vulnerabilities detected in your Supabase projects
5. Re: Re: Re: Company closure
```

### Get Full Email Data (JSON)

```bash
# Get emails as structured JSON
python3 gmail_agent.py json 10
```

### Python API (For Custom Queries)

```python
from gmail_test import get_gmail_service, get_recent_emails

# Get authenticated service
service = get_gmail_service()

# Get emails as structured data (no printing)
emails = get_recent_emails(service, max_results=10)

# Returns list of dicts:
# [{'from': '...', 'subject': '...', 'date': '...', 'id': '...'}, ...]
```

### Search Emails

See: [references/search-queries.md](references/search-queries.md) for complete query syntax cookbook.

**Common queries:**
- `newer_than:7d` - Recent emails
- `from:sender@example.com` - From specific sender
- `is:unread has:attachment` - Unread with attachments

**Example:**
```python
results = service.users().messages().list(
    userId='me',
    q='from:sender@example.com subject:important newer_than:7d',
    maxResults=20
).execute()
```

## Available Operations

See: [references/api-operations.md](references/api-operations.md) for detailed API reference.

**✅ Read Operations:**
- `messages().list()` - List/search messages
- `messages().get()` - Get message details (full/metadata/minimal)
- `threads().get()` - Get email threads
- `attachments().get()` - Get attachments
- `labels().list()` - List labels

**❌ Write Operations:** Not implemented by design for security.

## Setup

See: [references/setup-guide.md](references/setup-guide.md) for detailed service account configuration.

**Quick setup:**
- Set `SERVICE_ACCOUNT_FILE` and `EMAIL_ACCOUNT` env vars
- Optional: set `GMAIL_READ_POLICY_FILE` and/or `GMAIL_ALLOWED_READ_MAILBOXES` allowlist controls
- Ensure service account has domain-wide delegation
- Scope: `gmail.readonly`
- Verify: `python3 scripts/gmail_agent.py subjects 1`

## Implementation

**For agents:**
- `scripts/gmail_agent.py` - Clean interface for agent use
  - `subjects` command - List just subjects
  - `json` command - Full data as JSON
  - `--mailbox` flag - target a specific mailbox per call (if allowlisted)

**Multi-mailbox pattern (single VA, multiple seniors):**
- Keep one `bramclaw-gmail` skill.
- Use `EMAIL_ACCOUNT` as default mailbox.
- Use `--mailbox boss2@...` to switch per request.
- Enforce mailbox boundaries with `GMAIL_READ_POLICY_FILE` or `GMAIL_ALLOWED_READ_MAILBOXES`.

**For testing:**
- `tests/gmail_test.py` - Test harness with verbose output
  - `get_gmail_service()` - Authenticate and return service
  - `get_recent_emails(service, max_results)` - Get emails as data

## References

- [Setup Guide](references/setup-guide.md) - Service account configuration
- [Search Queries](references/search-queries.md) - Gmail query syntax cookbook
- [API Operations](references/api-operations.md) - Detailed API reference
- [Gmail API Docs](https://developers.google.com/gmail/api)

---

## Distribution

See: [DISTRIBUTION.md](DISTRIBUTION.md) for packaging and release instructions.

**Quick package:**
```bash
python3 ~/.claude/plugins/marketplaces/anthropic-agent-skills/skills/skill-creator/scripts/package_skill.py
# Creates: bramclaw-gmail.skill
```

**Install:**
```bash
claude skill install bramclaw-gmail.skill
```

**Latest release:** [GitHub Releases](https://github.com/bramforth/bram-claw/releases)

---

**Status:** ✅ Approved for production
**Security:** Read-only operations only
**Last audit:** 2026-02-20
