# bramclaw-github Skill

GitHub operations skill for OpenClaw agents.

## Quick Start

```bash
# Set authentication
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Test connection
python3 scripts/github_agent.py whoami

# List issues
python3 scripts/github_agent.py list-issues owner/repo

# Get issue details
python3 scripts/github_agent.py get-issue owner/repo 123
```

## Installation

```bash
pip install -r requirements.txt
```

## Documentation

- **SKILL.md** - Main skill documentation, quick reference
- **references/api-reference.md** - Complete API method documentation
- **references/common-queries.md** - Frequent use cases and examples
- **references/security-model.md** - Authentication, authorization, rate limits
- **references/error-handling.md** - Common errors and troubleshooting

## Agent Integration

This skill is used by the `bram-github` worker agent.

**Agent contract:** `config/agent-contracts/bram-github/AGENTS.md`

**Authorization:** All write operations require explicit confirmation tokens per `docs/agent-action-governance.md`

## Features

**Read operations (no authorization):**
- List issues by repository
- Get issue details
- List pull requests
- Get PR details
- Search issues across repositories

**Write operations (authorization required):**
- Create issues
- Update issues
- Close issues

## Configuration

**Required:** `GITHUB_TOKEN` environment variable

**Token scopes:**
- `repo` - Full access (private repositories)
- `public_repo` - Public repositories only

Generate token at: https://github.com/settings/tokens

## Development Status

**Version:** 1.0.0 MVP
**Status:** Production-ready for basic operations

**Limitations:**
- No PR creation/updates
- No comments management
- No labels/milestones admin
- No rate limit handling
- No retry logic

**Future enhancements tracked in:** `docs/plans/` (pending)

## Testing

**Manual testing:**
```bash
# Test authentication
./scripts/github_agent.py whoami

# Test read operations
./scripts/github_agent.py list-issues octocat/Hello-World

# Test search
./scripts/github_agent.py search-issues "is:issue is:open repo:octocat/Hello-World"
```

**Automated tests:** Not yet implemented (see bramclaw-clickup for test pattern)

## Support

**Issues:** File in main bram-claw repository
**Documentation:** Progressive disclosure pattern - start with SKILL.md, deep-dive in references/
