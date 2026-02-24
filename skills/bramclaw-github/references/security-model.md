# GitHub Security Model

Authentication, authorization, and rate limiting for bramclaw-github skill.

## Authentication

### GitHub Personal Access Token (PAT)

**Required environment variable:** `GITHUB_TOKEN`

**Token types:**
1. **Classic PAT** - Traditional token with broad scopes
2. **Fine-grained PAT** - Granular permissions per repository (recommended)

**How to generate:**

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" (classic) or "Fine-grained tokens" (new)
3. Select required scopes (see below)
4. Generate and copy token
5. Set in environment: `export GITHUB_TOKEN="ghp_xxx..."`

### Required Scopes

**Minimum (read-only):**
- `public_repo` - Access public repositories

**Full access (read/write):**
- `repo` - Full control of private repositories
  - Includes: issues, PRs, code, releases, etc.

**Fine-grained permissions (new PAT):**
- Issues: Read and write
- Pull requests: Read and write
- Contents: Read (if searching code)

### Token Security

**Best practices:**
1. Never commit tokens to git
2. Use environment variables only
3. Rotate tokens periodically (90 days)
4. Use fine-grained tokens when possible (principle of least privilege)
5. Revoke tokens when no longer needed

**Validation:**
```bash
# Test token
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user
```

---

## Authorization Governance

**GitHub is NOT a trusted internal system.**

All write operations require explicit authorization tokens per @docs/agent-action-governance.md.

### Read Operations (No Token Required)

Execute immediately without confirmation:
- `list-issues`
- `get-issue`
- `list-prs`
- `get-pr`
- `search-issues`

### Write Operations (Token Required)

Require `CONFIRM_WRITE:<id>` token:
- `create-issue`
- `update-issue` (including state changes)
- `add-labels`
- `assign-issue`

**Example authorization:**
```
MODE: execute
ACTION_CLASS: WRITE
ACTION_TYPE: CREATE
CONFIRMATION_TOKEN: CONFIRM_WRITE:abc123
```

### High Impact Operations (High Token Required)

Require `CONFIRM_HIGH_IMPACT:<id>` token:
- Delete issue (if implemented)
- Close many issues at once
- Bulk operations affecting >10 items

---

## Rate Limiting

### GitHub API Limits

**Authenticated requests:**
- Limit: 5,000 requests/hour
- Resets: Every hour on the hour

**Unauthenticated requests:**
- Limit: 60 requests/hour
- Not applicable (we always authenticate)

**Secondary rate limits:**
- GitHub may apply additional limits for:
  - Rapid creation of content
  - Concurrent requests
  - CPU-intensive operations

### Checking Rate Limit

**Programmatically:**
```python
import requests

response = requests.get(
    "https://api.github.com/rate_limit",
    headers={"Authorization": f"Bearer {token}"}
)
data = response.json()

core = data['rate']
print(f"Used: {core['used']}/{core['limit']}")
print(f"Remaining: {core['remaining']}")
print(f"Resets at: {core['reset']}")  # Unix timestamp
```

**Via CLI:**
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/rate_limit
```

### Rate Limit Headers

GitHub includes rate limit info in every response:

```
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4999
X-RateLimit-Reset: 1708704000
X-RateLimit-Used: 1
X-RateLimit-Resource: core
```

### Handling Rate Limits

**Current implementation:** Basic (no retry logic)

**Future enhancements:**
1. **Exponential backoff** - Retry with increasing delays
2. **Rate limit awareness** - Check before expensive operations
3. **Request batching** - Combine multiple queries
4. **Caching** - Store frequent lookups locally

**When rate limited:**
```python
try:
    issues = client.list_issues("owner/repo")
except requests.HTTPError as e:
    if e.response.status_code == 403:
        reset_time = e.response.headers.get('X-RateLimit-Reset')
        print(f"Rate limited. Resets at: {reset_time}")
        # Wait or queue for retry
```

---

## Error Responses

### 401 Unauthorized

**Cause:** Missing or invalid GITHUB_TOKEN

**Fix:**
```bash
# Check token is set
echo $GITHUB_TOKEN

# Validate token
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user

# If invalid, regenerate at https://github.com/settings/tokens
```

### 403 Forbidden

**Possible causes:**
1. Rate limit exceeded
2. Token lacks required scope
3. Repository is private and token doesn't have access
4. API endpoint requires authentication

**Debug:**
```bash
# Check rate limit
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/rate_limit

# Check token scopes
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user
# Inspect 'X-OAuth-Scopes' header
```

**Fix:**
- Wait for rate limit reset
- Regenerate token with correct scopes
- Verify repository access

### 404 Not Found

**Cause:**
1. Repository doesn't exist
2. Repository is private and token can't access
3. Issue/PR number doesn't exist
4. Typo in owner/repo format

**Validation:**
```python
# Validate repo exists and is accessible
try:
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
except requests.HTTPError:
    print("Repository not found or not accessible")
```

### 422 Unprocessable Entity

**Cause:** Validation error in request parameters

**Common issues:**
- Invalid label name
- Invalid assignee username
- Issue title too long (>256 chars)
- Malformed JSON

**Example error:**
```json
{
  "message": "Validation Failed",
  "errors": [
    {
      "resource": "Issue",
      "field": "title",
      "code": "missing_field"
    }
  ]
}
```

---

## Audit Trail

**GitHub provides audit logs for:**
- Issue creation/updates
- Label changes
- Assignee changes
- State transitions (open → closed)

**View audit:**
1. Repository → Settings → Security → Audit log
2. Or via API: `GET /repos/{owner}/{repo}/events`

**Recommended:**
- Log all write operations locally
- Include timestamp, user, operation, and result
- Store in structured format (JSON, CSV)

**Example log entry:**
```json
{
  "timestamp": "2026-02-23T14:30:00Z",
  "agent": "bram-github",
  "operation": "create_issue",
  "repo": "owner/repo",
  "issue_number": 123,
  "title": "Bug in login flow",
  "authorization": "CONFIRM_WRITE:abc123",
  "status": "success"
}
```

---

## Compliance

**Data handling:**
- GitHub API responses may contain private information
- Issues/PRs may reference sensitive customer data
- Respect GitHub's Acceptable Use Policies
- Don't scrape or cache excessively

**Privacy:**
- User emails may be private (`noreply@github.com` addresses)
- Respect user notification preferences
- Don't spam issue creation or comments

**Terms of Service:**
- Comply with https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- API usage subject to rate limits and fair use
- Don't use API for competitive intelligence gathering

---

**Security review:** Pending
**Compliance check:** Pending
**Last updated:** 2026-02-23
