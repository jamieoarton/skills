# GitHub API Reference

Complete documentation for bramclaw-github skill API methods.

## GitHubClient Class

### Initialization

```python
from github_client import GitHubClient

# Uses GITHUB_TOKEN from environment
client = GitHubClient()

# Or provide token explicitly
client = GitHubClient(token="ghp_xxx...")
```

---

## Read Methods (No Authorization Required)

### get_current_user()

Get authenticated user information.

**Returns:** User object with login, name, email, etc.

**Example:**
```python
user = client.get_current_user()
print(f"Authenticated as: {user['login']}")
```

---

### list_issues(repo, state="open", **filters)

List issues in a repository.

**Parameters:**
- `repo` (str): Repository in format "owner/repo"
- `state` (str): "open", "closed", or "all" (default: "open")
- `**filters`: Additional query parameters
  - `assignee` (str): Filter by assignee username
  - `labels` (str): Comma-separated label names
  - `sort` (str): "created", "updated", "comments"
  - `direction` (str): "asc" or "desc"

**Returns:** List of issue objects

**Example:**
```python
# Open issues
issues = client.list_issues("owner/repo")

# Closed bugs assigned to user
issues = client.list_issues("owner/repo",
    state="closed",
    assignee="username",
    labels="bug"
)
```

---

### get_issue(repo, issue_number)

Get details of a specific issue.

**Parameters:**
- `repo` (str): Repository in format "owner/repo"
- `issue_number` (int): Issue number

**Returns:** Complete issue object with body, labels, assignees, etc.

**Example:**
```python
issue = client.get_issue("owner/repo", 123)
print(f"Title: {issue['title']}")
print(f"State: {issue['state']}")
print(f"Body: {issue['body']}")
```

---

### list_pull_requests(repo, state="open", **filters)

List pull requests in a repository.

**Parameters:**
- `repo` (str): Repository in format "owner/repo"
- `state` (str): "open", "closed", or "all" (default: "open")
- `**filters`: Additional query parameters

**Returns:** List of PR objects

**Example:**
```python
prs = client.list_pull_requests("owner/repo", state="open")
```

---

### get_pull_request(repo, pr_number)

Get details of a specific pull request.

**Parameters:**
- `repo` (str): Repository in format "owner/repo"
- `pr_number` (int): PR number

**Returns:** Complete PR object

**Example:**
```python
pr = client.get_pull_request("owner/repo", 456)
print(f"Title: {pr['title']}")
print(f"Mergeable: {pr['mergeable']}")
```

---

### search_issues(query, **filters)

Search issues across GitHub.

**Parameters:**
- `query` (str): GitHub search query syntax
- `**filters`: Additional parameters (sort, order, per_page)

**Returns:** List of matching issue objects

**Example:**
```python
# Search for open bugs in specific repo
results = client.search_issues("is:issue is:open label:bug repo:owner/repo")

# Search across all repos in org
results = client.search_issues("is:issue org:myorg label:enhancement")
```

**Query syntax:** See https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests

---

## Write Methods (Require Authorization)

### create_issue(repo, title, body=None, assignees=None, labels=None)

Create a new issue.

**Authorization required:** `CONFIRM_WRITE:<id>` token

**Parameters:**
- `repo` (str): Repository in format "owner/repo"
- `title` (str): Issue title (required)
- `body` (str): Issue description/body (optional)
- `assignees` (list): List of username strings to assign (optional)
- `labels` (list): List of label name strings (optional)

**Returns:** Created issue object with `number`, `html_url`, etc.

**Example:**
```python
issue = client.create_issue(
    "owner/repo",
    "Bug in login flow",
    body="When user clicks login button, form doesn't submit",
    labels=["bug", "priority-high"],
    assignees=["developer1"]
)
print(f"Created issue #{issue['number']}: {issue['html_url']}")
```

---

### update_issue(repo, issue_number, **updates)

Update an existing issue.

**Authorization required:** `CONFIRM_WRITE:<id>` token

**Parameters:**
- `repo` (str): Repository in format "owner/repo"
- `issue_number` (int): Issue number to update
- `**updates`: Fields to update
  - `title` (str): New title
  - `body` (str): New body
  - `state` (str): "open" or "closed"
  - `labels` (list): Replace labels
  - `assignees` (list): Replace assignees

**Returns:** Updated issue object

**Example:**
```python
# Close an issue
issue = client.update_issue("owner/repo", 123, state="closed")

# Update title and add label
issue = client.update_issue(
    "owner/repo",
    123,
    title="Updated title",
    labels=["bug", "resolved"]
)
```

---

## Error Handling

All methods raise `requests.HTTPError` on API errors.

**Common status codes:**
- `401 Unauthorized` - Invalid or missing GITHUB_TOKEN
- `403 Forbidden` - Token lacks required scope or rate limit exceeded
- `404 Not Found` - Repository or issue doesn't exist
- `422 Unprocessable Entity` - Validation error (invalid parameters)

**Example:**
```python
try:
    issue = client.get_issue("owner/repo", 999)
except requests.HTTPError as e:
    if e.response.status_code == 404:
        print("Issue not found")
    else:
        raise
```

See: @error-handling.md for detailed error scenarios

---

## Rate Limiting

GitHub API rate limits:
- **Authenticated:** 5,000 requests/hour
- **Unauthenticated:** 60 requests/hour

**Check rate limit:**
```python
response = requests.get(
    "https://api.github.com/rate_limit",
    headers={"Authorization": f"Bearer {token}"}
)
data = response.json()
print(f"Remaining: {data['rate']['remaining']}/{data['rate']['limit']}")
```

See: @security-model.md for rate limit handling strategies

---

**API Version:** GitHub REST API v3 (2022-11-28)
**Documentation:** https://docs.github.com/en/rest
