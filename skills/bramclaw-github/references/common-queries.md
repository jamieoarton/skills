# Common GitHub Queries

Frequent use cases and examples for bramclaw-github skill.

## Issue Management

### List My Open Issues

```bash
# In a specific repo
python3 scripts/github_agent.py list-issues owner/repo

# Assigned to specific user
python3 scripts/github_agent.py list-issues owner/repo --assignee username
```

### Find All Bugs

```bash
# Using search across repos
python3 scripts/github_agent.py search-issues "is:issue is:open label:bug repo:owner/repo"

# In specific repo
python3 scripts/github_agent.py list-issues owner/repo --labels bug
```

### Check Issue Status

```bash
# Get full issue details
python3 scripts/github_agent.py get-issue owner/repo 123
```

### Create Bug Report

**Authorization required:** `MODE: execute`, `ACTION_CLASS: WRITE`, `CONFIRMATION_TOKEN`

```bash
python3 scripts/github_agent.py create-issue owner/repo "Login button doesn't work" \
  --body "Steps to reproduce: 1. Go to login page, 2. Click login button, 3. Nothing happens" \
  --labels bug,priority-high
```

### Close Resolved Issue

**Authorization required:** `MODE: execute`, `ACTION_CLASS: WRITE`, `CONFIRMATION_TOKEN`

```bash
python3 scripts/github_agent.py update-issue owner/repo 123 --state closed
```

---

## Pull Request Queries

### List Open PRs

```bash
python3 scripts/github_agent.py list-prs owner/repo
```

### Check PR Details

```bash
python3 scripts/github_agent.py get-pr owner/repo 456
```

### Find PRs by Author

```bash
python3 scripts/github_agent.py search-issues "is:pr is:open author:username repo:owner/repo"
```

---

## Search Patterns

### Issues Modified Recently

```bash
python3 scripts/github_agent.py search-issues "is:issue updated:>2026-02-01 repo:owner/repo"
```

### High Priority Items

```bash
python3 scripts/github_agent.py search-issues "is:issue is:open label:priority-high repo:owner/repo"
```

### Issues Without Assignee

```bash
python3 scripts/github_agent.py search-issues "is:issue is:open no:assignee repo:owner/repo"
```

### Closed Issues This Week

```bash
python3 scripts/github_agent.py search-issues "is:issue is:closed closed:>2026-02-17 repo:owner/repo"
```

---

## Workflow Integration

### Daily Standup Report

```bash
# What's assigned to me?
python3 scripts/github_agent.py search-issues "is:issue is:open assignee:@me"

# What did I close yesterday?
python3 scripts/github_agent.py search-issues "is:issue is:closed assignee:@me closed:>2026-02-22"
```

### Sprint Planning

```bash
# Unassigned bugs
python3 scripts/github_agent.py search-issues "is:issue is:open label:bug no:assignee repo:owner/repo"

# Feature requests
python3 scripts/github_agent.py search-issues "is:issue is:open label:enhancement repo:owner/repo"
```

### Release Checklist

```bash
# Open issues in milestone
python3 scripts/github_agent.py search-issues "is:issue is:open milestone:v1.0 repo:owner/repo"

# Merged PRs in milestone
python3 scripts/github_agent.py search-issues "is:pr is:merged milestone:v1.0 repo:owner/repo"
```

---

## Authorization Patterns

### Read-Only Query (No Authorization)

```
MODE: observe
ACTION_CLASS: READ

List all open issues in owner/repo
```

Agent executes read immediately without token.

### Propose Write Operation

```
MODE: propose
ACTION_CLASS: WRITE
ACTION_TYPE: CREATE

Create issue "Bug report" in owner/repo
```

Agent returns plan but doesn't execute. User must upgrade to `MODE: execute` with token.

### Execute Write Operation

```
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: CREATE
CONFIRMATION_TOKEN: CONFIRM_WRITE:abc123

Create issue "Bug report" in owner/repo with body "..."
```

Agent executes create operation with authorization.

### High Impact Operation

```
MODE: execute_high_impact
ACTION_CLASS: HIGH_IMPACT
ACTION_TYPE: DELETE
CONFIRMATION_TOKEN: CONFIRM_HIGH_IMPACT:xyz789

Delete issue #123 in owner/repo
```

Requires highest authorization level.

---

## Python API Examples

### Check Daily Activity

```python
from github_client import GitHubClient

client = GitHubClient()

# My activity today
user = client.get_current_user()
username = user['login']

# Issues I created today
created = client.search_issues(f"is:issue author:{username} created:>2026-02-23")
print(f"Created {len(created)} issues today")

# Issues assigned to me
assigned = client.search_issues(f"is:issue is:open assignee:{username}")
print(f"{len(assigned)} issues assigned to me")
```

### Automated Triage

```python
# Find untriaged bugs (no label, no assignee)
untriaged = client.search_issues(
    "is:issue is:open label:bug no:label no:assignee repo:owner/repo"
)

for issue in untriaged:
    print(f"#{issue['number']}: {issue['title']}")
    # Note: Auto-assignment would require WRITE authorization
```

### Report Generation

```python
# Sprint summary
closed_this_week = client.search_issues(
    "is:issue is:closed closed:>2026-02-17 repo:owner/repo"
)

by_label = {}
for issue in closed_this_week:
    for label in issue.get('labels', []):
        name = label['name']
        by_label[name] = by_label.get(name, 0) + 1

print("Issues closed this week by label:")
for label, count in sorted(by_label.items()):
    print(f"  {label}: {count}")
```

---

## Search Query Syntax

**GitHub search qualifiers:**

- `is:issue` / `is:pr` - Type filter
- `is:open` / `is:closed` - State filter
- `repo:owner/repo` - Repository scope
- `author:username` - Creator filter
- `assignee:username` - Assignee filter (use `@me` for self)
- `label:name` - Label filter
- `no:label` / `no:assignee` - Negative filter
- `created:>YYYY-MM-DD` - Creation date
- `updated:>YYYY-MM-DD` - Last update date
- `closed:>YYYY-MM-DD` - Close date
- `milestone:name` - Milestone filter
- `sort:created` / `sort:updated` - Sorting

**Full syntax:** https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests

---

**Last updated:** 2026-02-23
