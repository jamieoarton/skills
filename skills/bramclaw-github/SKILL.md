---
name: bramclaw-github
description: Use when users ask to read, search, create, or update GitHub issues and pull requests, including status, assignee, and label workflows.
---

**Version:** 1.0.0 | **Status:** ✅ Production

---

# GitHub Operations Skill

Systematic interface for GitHub issues and pull requests via GitHub REST API.

## When This Skill Should Trigger

**✅ Should trigger for:**
- "List GitHub issues for X repository"
- "Create a GitHub issue for Y"
- "What are the open PRs in Z repo?"
- "Update issue #123 in my repo"
- "Search for issues with label 'bug'"

**❌ Should NOT trigger for:**
- Git operations (commits, branches, etc.) - use git CLI
- GitHub Actions workflow management - different domain
- Repository administration (settings, webhooks) - out of scope

---

## Quick Reference

### Read Operations (No Authorization Required)

```bash
# List issues
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py list-issues owner/repo

# Get specific issue
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py get-issue owner/repo 123

# List pull requests
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py list-prs owner/repo

# Get specific PR
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py get-pr owner/repo 456

# Search issues
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py search-issues "is:issue is:open label:bug"
```

### Write Operations (Require Authorization)

```bash
# Create issue
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py create-issue owner/repo "Bug title" --body "Description"

# Update issue
python3 /root/.openclaw/skills/bramclaw-github/scripts/github_agent.py update-issue owner/repo 123 --state closed
```

---

## Authorization Model

**GitHub is NOT a trusted internal system.**

All write operations require explicit confirmation tokens:
- CREATE issue → requires `CONFIRM_WRITE:<id>`
- UPDATE issue → requires `CONFIRM_WRITE:<id>`
- DELETE/close → requires `CONFIRM_WRITE:<id>` or `CONFIRM_HIGH_IMPACT:<id>`

See: @docs/agent-action-governance.md

---

## Authentication

**Required environment variable:** `GITHUB_TOKEN`

**Token type:** GitHub Personal Access Token (classic or fine-grained)

**Required scopes:**
- `repo` - Full control of private repositories (includes issues, PRs)
- `public_repo` - Access to public repositories (if only working with public repos)

**Setup:**
```bash
# Generate token at: https://github.com/settings/tokens
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

See: @.env.example for configuration template

---

## Progressive Documentation

**For detailed information, see:**

- **API Reference:** @references/api-reference.md - Complete GitHub API method documentation
- **Common Queries:** @references/common-queries.md - Frequent use cases and examples
- **Security Model:** @references/security-model.md - Authentication, authorization, rate limits
- **Error Handling:** @references/error-handling.md - Common errors and troubleshooting

---

## Implementation

**Primary client:** `scripts/github_client.py` - Python wrapper for GitHub REST API
**CLI interface:** `scripts/github_agent.py` - Command-line tool for agent operations

**Dependencies:**
- `requests` - HTTP library for API calls
- `GITHUB_TOKEN` environment variable

---

## Limitations

**Current scope (MVP):**
- Issues: list, get, create, update
- Pull requests: list, get (read-only)
- Search: basic issue search

**Not yet implemented:**
- PR creation/updates
- Comments on issues/PRs
- Labels, milestones management
- Repository operations
- Webhook support
- GitHub Apps integration

**Rate limits:**
- Authenticated: 5,000 requests/hour
- Unauthenticated: 60 requests/hour

See: @references/security-model.md for rate limit handling

---

## Example Usage

**Read issues:**
```bash
# List open issues
bram-github list-issues owner/repo

# Filter by state
bram-github list-issues owner/repo --state closed

# Get full issue details
bram-github get-issue owner/repo 42
```

**Create issue (with authorization):**
```
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: CREATE
CONFIRMATION_TOKEN: CONFIRM_WRITE:abc123

Create issue in owner/repo with title "Bug in login flow"
```

**Search across repositories:**
```bash
bram-github search-issues "is:issue is:open repo:owner/repo label:bug"
```

---

**Status:** ✅ Production MVP
**Security:** All writes require explicit authorization tokens
**Last updated:** 2026-02-23
