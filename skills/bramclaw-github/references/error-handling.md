# GitHub Error Handling

Common errors and troubleshooting for bramclaw-github skill.

## Connection Errors

### Network Timeout

**Error:**
```
requests.exceptions.ConnectionError: ('Connection aborted.', timeout('timed out'))
```

**Causes:**
- Network connectivity issues
- GitHub API outage
- Firewall blocking GitHub API

**Solutions:**
1. Check internet connection
2. Verify GitHub status: https://www.githubstatus.com/
3. Check firewall rules allow `api.github.com`
4. Retry with exponential backoff

---

### SSL/TLS Errors

**Error:**
```
requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]
```

**Causes:**
- Corporate proxy with SSL inspection
- System SSL certificates outdated
- Python `certifi` package needs update

**Solutions:**
```bash
# Update certificates
pip install --upgrade certifi

# Or use system certificates
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

---

## Authentication Errors

### Missing Token

**Error:**
```
ValueError: GITHUB_TOKEN is not set
```

**Solution:**
```bash
# Set token in environment
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Verify it's set
echo $GITHUB_TOKEN

# Make persistent (add to ~/.bashrc or ~/.zshrc)
echo 'export GITHUB_TOKEN="ghp_xxx..."' >> ~/.bashrc
```

---

### Invalid Token

**Error:**
```
requests.exceptions.HTTPError: 401 Client Error: Unauthorized
```

**Response body:**
```json
{
  "message": "Bad credentials",
  "documentation_url": "https://docs.github.com/rest"
}
```

**Causes:**
- Token is expired
- Token was revoked
- Token has typo/corruption
- Using old token after regeneration

**Solutions:**
1. Regenerate token at https://github.com/settings/tokens
2. Update GITHUB_TOKEN environment variable
3. Verify with: `curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user`

---

### Insufficient Permissions

**Error:**
```
requests.exceptions.HTTPError: 403 Client Error: Forbidden
```

**Response body:**
```json
{
  "message": "Resource not accessible by integration",
  "documentation_url": "https://docs.github.com/rest/reference/issues"
}
```

**Causes:**
- Token lacks required scope (`repo` or `public_repo`)
- Fine-grained token doesn't have Issues permission
- Repository is private and token can't access org

**Solutions:**
1. Regenerate token with correct scopes
2. For classic PAT: enable `repo` scope
3. For fine-grained PAT: enable "Issues: Read and write"
4. Verify org/repo access granted to token

---

## Rate Limit Errors

### Rate Limit Exceeded

**Error:**
```
requests.exceptions.HTTPError: 403 Client Error: Forbidden
```

**Response headers:**
```
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1708704000
```

**Response body:**
```json
{
  "message": "API rate limit exceeded for user ID 12345.",
  "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"
}
```

**Solutions:**
1. **Wait for reset:**
   ```python
   import time
   reset_time = int(response.headers['X-RateLimit-Reset'])
   wait_seconds = reset_time - time.time()
   print(f"Waiting {wait_seconds} seconds for rate limit reset")
   time.sleep(wait_seconds)
   ```

2. **Use conditional requests** (if-modified-since headers)
3. **Batch operations** to reduce API calls
4. **Cache responses** locally

---

### Secondary Rate Limit

**Error:**
```
requests.exceptions.HTTPError: 403 Client Error: Forbidden
```

**Response body:**
```json
{
  "message": "You have exceeded a secondary rate limit. Please wait a few minutes before you try again.",
  "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits"
}
```

**Causes:**
- Too many rapid writes (creating issues, updating in quick succession)
- Concurrent requests to same resource
- CPU-intensive operations (large searches)

**Solutions:**
1. Add delays between write operations (1-2 seconds)
2. Reduce concurrency
3. Wait 1-5 minutes before retrying
4. Implement exponential backoff

---

## Resource Errors

### Repository Not Found

**Error:**
```
requests.exceptions.HTTPError: 404 Client Error: Not Found
```

**Causes:**
- Repository doesn't exist
- Typo in owner/repo format
- Repository is private and token can't access
- Repository was deleted or moved

**Debug:**
```python
# Check repository exists
import requests

response = requests.get(
    f"https://api.github.com/repos/{owner}/{repo}",
    headers={"Authorization": f"Bearer {token}"}
)

if response.status_code == 404:
    print(f"Repository {owner}/{repo} not found or not accessible")
elif response.status_code == 200:
    data = response.json()
    print(f"Found: {data['full_name']} (private: {data['private']})")
```

**Solutions:**
1. Verify repository name spelling
2. Check owner/repo format: "owner/repo" not "owner:repo"
3. Ensure token has access to private repos
4. Check repository wasn't archived or deleted

---

### Issue/PR Not Found

**Error:**
```
requests.exceptions.HTTPError: 404 Client Error: Not Found
```

**Causes:**
- Issue/PR number doesn't exist
- Using PR number with `/issues/` endpoint (PRs are issues, but not vice versa)
- Issue was deleted (rare)

**Solutions:**
1. Verify issue/PR number exists
2. Use `list_issues()` to find valid numbers
3. Note: GitHub issue numbers are sequential and never reused

---

## Validation Errors

### Missing Required Field

**Error:**
```
requests.exceptions.HTTPError: 422 Client Error: Unprocessable Entity
```

**Response body:**
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

**Causes:**
- Missing required parameter (title for create_issue)
- Empty string for required field

**Solutions:**
```python
# Always provide required fields
issue = client.create_issue(
    "owner/repo",
    title="This is required",  # Can't be empty
    body="Body is optional"
)
```

---

### Invalid Field Value

**Error:**
```
requests.exceptions.HTTPError: 422 Client Error: Unprocessable Entity
```

**Response body:**
```json
{
  "message": "Validation Failed",
  "errors": [
    {
      "resource": "Issue",
      "field": "labels",
      "code": "invalid",
      "value": "invalid-label-name"
    }
  ]
}
```

**Causes:**
- Label doesn't exist in repository
- Invalid assignee username
- Invalid state value (not "open" or "closed")
- Title too long (>256 characters)

**Solutions:**
1. **Validate labels exist:**
   ```python
   # Get repository labels first
   response = requests.get(
       f"https://api.github.com/repos/{repo}/labels",
       headers=headers
   )
   valid_labels = [l['name'] for l in response.json()]
   ```

2. **Validate assignees exist:**
   ```python
   # Check collaborator exists
   response = requests.get(
       f"https://api.github.com/repos/{repo}/collaborators/{username}",
       headers=headers
   )
   if response.status_code == 404:
       print(f"{username} is not a collaborator")
   ```

3. **Validate field lengths:**
   ```python
   if len(title) > 256:
       title = title[:253] + "..."
   ```

---

## API-Specific Errors

### Issue is Locked

**Error:**
```
requests.exceptions.HTTPError: 422 Client Error: Unprocessable Entity
```

**Response:**
```json
{
  "message": "Issue is locked",
  "documentation_url": "https://docs.github.com/rest/reference/issues#update-an-issue"
}
```

**Cause:** Issue is locked for off-topic, too heated, resolved, or spam

**Solution:** Can't update locked issues unless you have admin permissions

---

### Pull Request Can't Be Updated

**Cause:** PRs have additional constraints compared to issues

**Solution:** Use `/repos/{owner}/{repo}/pulls/{number}` endpoint, not `/issues/`

---

## Client Errors

### Invalid Repository Format

**Error:**
```
KeyError: 'owner'
```

**Cause:** Repository parameter not in "owner/repo" format

**Solution:**
```python
# Validate format before API call
def validate_repo(repo):
    if '/' not in repo:
        raise ValueError(f"Repository must be in 'owner/repo' format, got: {repo}")
    owner, name = repo.split('/', 1)
    if not owner or not name:
        raise ValueError(f"Invalid repository format: {repo}")
    return owner, name

# Usage
owner, repo_name = validate_repo("owner/repo")
```

---

## Debugging Strategies

### Enable Request Logging

```python
import logging
import http.client as http_client

# Enable debug logging
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig(level=logging.DEBUG)
```

### Inspect Full Response

```python
try:
    client.create_issue("owner/repo", "Title")
except requests.HTTPError as e:
    print(f"Status: {e.response.status_code}")
    print(f"Headers: {e.response.headers}")
    print(f"Body: {e.response.text}")
    print(f"URL: {e.response.url}")
```

### Check API Status

Before debugging, verify GitHub isn't experiencing issues:
- Status page: https://www.githubstatus.com/
- Incidents: https://www.githubstatus.com/history

---

## Error Recovery Patterns

### Retry with Exponential Backoff

```python
import time

def retry_with_backoff(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except requests.HTTPError as e:
            if e.response.status_code in [429, 403, 500, 502, 503]:
                wait = 2 ** attempt  # 1s, 2s, 4s
                print(f"Retry {attempt + 1}/{max_retries} after {wait}s")
                time.sleep(wait)
            else:
                raise
    raise Exception("Max retries exceeded")
```

### Graceful Degradation

```python
def get_issue_safe(repo, number):
    try:
        return client.get_issue(repo, number)
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return None  # Issue doesn't exist
        elif e.response.status_code == 403:
            # Rate limited or forbidden
            print("Access denied, returning cached data")
            return get_from_cache(repo, number)
        else:
            raise  # Unexpected error
```

---

**Last updated:** 2026-02-23
**See also:** @security-model.md for authentication errors
