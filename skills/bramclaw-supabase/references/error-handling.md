# Error Handling and Best Practices

Error handling patterns, rate limits, and monitoring for `bramclaw-supabase`.

---

## Error Handling Patterns

### Basic Error Handling

```python
import requests
from scripts.supabase_client import SupabaseClient

try:
    client = SupabaseClient()
    projects = client.get_projects()
except requests.HTTPError as e:
    if e.response.status_code == 401:
        print("Authentication failed - check SUPABASE_ACCESS_TOKEN")
    elif e.response.status_code == 404:
        print("Resource not found")
    elif e.response.status_code == 429:
        print("Rate limited - wait before retrying")
    elif e.response.status_code >= 500:
        print(f"Supabase server error: {e.response.status_code}")
    else:
        print(f"API error: {e}")
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Common Error Codes

### 401 Unauthorized

**Cause:** Invalid or missing access token

**Solution:**
```python
# Check environment variable is set
import os
token = os.environ.get("SUPABASE_ACCESS_TOKEN")
if not token:
    raise ValueError("SUPABASE_ACCESS_TOKEN not set in environment")

# Verify token format (should start with "sbp_")
if not token.startswith("sbp_"):
    raise ValueError("Invalid token format (should start with 'sbp_')")
```

**Fix:**
1. Verify `SUPABASE_ACCESS_TOKEN` is set
2. Check token hasn't expired or been revoked
3. Generate new token at https://supabase.com/dashboard/account/tokens

---

### 404 Not Found

**Cause:** Project doesn't exist or you don't have access

**Solution:**
```python
try:
    advisors = client.get_security_advisors('invalid_project_id')
except requests.HTTPError as e:
    if e.response.status_code == 404:
        print("Project not found. Check:")
        print("- Project ID is correct")
        print("- Project hasn't been deleted")
        print("- Token has access to this project")
```

**Debug Steps:**
1. List all projects: `client.get_projects()`
2. Verify project ID matches
3. Check project status (not paused or deleted)

---

### 429 Rate Limited

**Cause:** Exceeded API rate limits

**Supabase Rate Limits:**
- Management API: Per-user, per-scope rate limiting
- Exact limits not publicly documented
- Typical: ~100 requests per minute

**Solution with exponential backoff:**
```python
import time
import requests

def api_call_with_retry(func, *args, max_retries=3, **kwargs):
    """Call API with exponential backoff on rate limit."""
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except requests.HTTPError as e:
            if e.response.status_code == 429:
                # Exponential backoff: 2s, 4s, 8s
                wait_time = 2 ** (attempt + 1)
                print(f"Rate limited. Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            else:
                raise
    raise Exception(f"Rate limit exceeded after {max_retries} retries")

# Usage
projects = api_call_with_retry(client.get_projects)
```

---

### 500/503 Server Errors

**Cause:** Supabase API experiencing issues

**Solution:**
```python
import time
import requests

def api_call_with_server_retry(func, *args, max_retries=3, **kwargs):
    """Call API with retry on server errors."""
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except requests.HTTPError as e:
            if e.response.status_code >= 500:
                wait_time = 5  # Wait 5 seconds before retry
                print(f"Supabase server error. Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            else:
                raise
    raise Exception(f"Supabase server unavailable after {max_retries} retries")
```

---

## Rate Limit Best Practices

### 1. Cache Project IDs

**Bad (re-fetches every time):**
```python
def check_security():
    projects = client.get_projects()  # API call
    for project in projects:
        advisors = client.get_security_advisors(project['id'])  # API call per project
```

**Good (cache project IDs):**
```python
# Store in config or environment
PROJECT_IDS = ['ovrxdoyvkyrczsxhvada', 'abc123def456']

def check_security():
    for project_id in PROJECT_IDS:
        advisors = client.get_security_advisors(project_id)  # Only these API calls
```

**Savings:** N+1 API calls → N API calls

---

### 2. Filter Results Server-Side

Management API doesn't support extensive filtering, but use available parameters:

```python
# Get specific project logs with time range
logs = client.get_logs(
    'ovrxdoyvkyrczsxhvada',
    service='postgres',
    iso_timestamp_start='2026-02-21T00:00:00Z',
    iso_timestamp_end='2026-02-21T01:00:00Z'  # Narrow time range
)
```

**Don't:**
```python
# Get all logs then filter client-side
all_logs = client.get_logs('project', 'postgres', '2026-01-01', '2026-02-21')
recent = [l for l in all_logs if l['timestamp'] > '2026-02-21']
```

---

### 3. Batch Operations Efficiently

**Bad (sequential calls):**
```python
project_ids = ['abc', 'def', 'ghi']
for pid in project_ids:
    security = client.get_security_advisors(pid)  # Sequential
    performance = client.get_performance_advisors(pid)  # Sequential
```

**Good (parallel execution where possible):**
```python
from concurrent.futures import ThreadPoolExecutor

def get_all_advisors(project_id):
    return {
        'project_id': project_id,
        'security': client.get_security_advisors(project_id),
        'performance': client.get_performance_advisors(project_id)
    }

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(get_all_advisors, project_ids))
```

**Note:** Use reasonable worker count to avoid rate limits

---

### 4. Rate Limit Tracking

Track API usage to stay under limits:

```python
import time
from collections import deque

class RateLimitTracker:
    def __init__(self, max_per_minute=100):
        self.max_per_minute = max_per_minute
        self.calls = deque()  # Timestamps of API calls

    def check_and_wait(self):
        """Wait if approaching rate limit."""
        now = time.time()

        # Remove calls older than 1 minute
        while self.calls and self.calls[0] < now - 60:
            self.calls.popleft()

        # If at limit, wait
        if len(self.calls) >= self.max_per_minute:
            wait_time = 60 - (now - self.calls[0])
            print(f"Rate limit: waiting {wait_time:.1f}s")
            time.sleep(wait_time)

        # Record this call
        self.calls.append(now)

# Usage
tracker = RateLimitTracker()

for project_id in project_ids:
    tracker.check_and_wait()
    advisors = client.get_security_advisors(project_id)
```

---

## Monitoring

### Logging Setup

```python
import logging
import json
import time

# Configure logging
logging.basicConfig(
    filename='/var/log/bramclaw/supabase.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_operation(operation, details):
    """Log Supabase operation with structured data."""
    log_entry = {
        'timestamp': time.time(),
        'operation': operation,
        'details': details
    }
    logging.info(json.dumps(log_entry))

# Usage
log_operation('GET_PROJECTS', {'count': 5})
log_operation('GET_SECURITY_ADVISORS', {'project_id': 'abc123', 'errors': 10})
```

---

### What to Log

**Always log:**
- All write operations (create/pause/restore/migrate)
- Resource IDs affected
- Operation result (success/failure)
- Error codes
- Rate limit hits

**Example log entries:**
```json
{"timestamp": 1708551045, "operation": "GET_PROJECTS", "details": {"count": 5}}
{"timestamp": 1708551046, "operation": "GET_SECURITY_ADVISORS", "details": {"project_id": "abc123", "errors": 10, "warnings": 3}}
{"timestamp": 1708551047, "operation": "CREATE_PROJECT", "details": {"name": "my-project", "region": "us-east-1", "project_id": "def456"}}
{"timestamp": 1708551048, "operation": "ERROR", "details": {"code": 429, "message": "Rate limited"}}
```

**Never log:**
- Access tokens
- Database passwords
- Sensitive query results
- Personal information (PII)

---

### Log Monitoring Script

```python
#!/usr/bin/env python3
# monitor_supabase_logs.py

import json
from collections import Counter

def analyze_logs(log_file='/var/log/bramclaw/supabase.log'):
    """Analyze Supabase API usage from logs."""
    operations = Counter()
    errors = []
    rate_limits = 0

    with open(log_file, 'r') as f:
        for line in f:
            try:
                # Parse log entry
                parts = line.split(' - ')
                if len(parts) < 3:
                    continue

                json_data = json.loads(parts[2].strip())

                # Count operations
                op = json_data.get('operation', 'UNKNOWN')
                operations[op] += 1

                # Track errors
                if op == 'ERROR':
                    errors.append(json_data)
                    if json_data.get('details', {}).get('code') == 429:
                        rate_limits += 1

            except json.JSONDecodeError:
                continue

    # Report
    print("Supabase API Usage Summary")
    print("=" * 40)
    print(f"Total operations: {sum(operations.values())}")
    print(f"\nTop operations:")
    for op, count in operations.most_common(10):
        print(f"  {op}: {count}")

    print(f"\nErrors: {len(errors)}")
    print(f"Rate limits hit: {rate_limits}")

    if rate_limits > 0:
        print("\n⚠️  WARNING: Rate limit hit. Consider:")
        print("  - Caching project IDs")
        print("  - Reducing check frequency")
        print("  - Adding delays between calls")

if __name__ == '__main__':
    analyze_logs()
```

**Run:**
```bash
python3 monitor_supabase_logs.py
```

---

### Alerts

Configure alerts for:

**High Priority:**
- **Any write operations** (create/pause/restore)
- **Failed authentication** (401 errors)
- **>3 rate limit hits in 1 hour**

**Medium Priority:**
- **>50 API calls in 1 minute**
- **Server errors** (500/503)
- **Project security errors > 50**

**Alert script example:**
```python
def check_for_alerts(log_file='/var/log/bramclaw/supabase.log'):
    """Check logs for alert conditions."""
    now = time.time()
    one_hour_ago = now - 3600

    rate_limit_count = 0
    write_operations = []

    with open(log_file, 'r') as f:
        for line in f:
            try:
                parts = line.split(' - ')
                json_data = json.loads(parts[2].strip())

                timestamp = json_data.get('timestamp', 0)
                if timestamp < one_hour_ago:
                    continue

                # Check for rate limits
                if json_data.get('operation') == 'ERROR' and \
                   json_data.get('details', {}).get('code') == 429:
                    rate_limit_count += 1

                # Check for write operations
                if json_data.get('operation') in ['CREATE_PROJECT', 'PAUSE_PROJECT', 'RESTORE_PROJECT', 'EXECUTE_MIGRATION']:
                    write_operations.append(json_data)

            except (json.JSONDecodeError, IndexError):
                continue

    # Send alerts
    if rate_limit_count >= 3:
        send_alert(f"⚠️ Rate limit hit {rate_limit_count} times in last hour")

    if write_operations:
        send_alert(f"⚠️ {len(write_operations)} write operations in last hour")

def send_alert(message):
    """Send alert (implement with Slack, email, etc.)."""
    print(f"ALERT: {message}")
    # TODO: Integrate with Slack/PagerDuty/Email
```

---

## Debugging Tips

### Enable Verbose Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Now API calls will show detailed info
client = SupabaseClient()
projects = client.get_projects()  # Will log request/response details
```

### Test Access Token

```bash
# Quick test
python3 scripts/supabase_agent.py whoami

# Expected output:
# Organizations: 2

# If error:
# Error: Supabase access token not found. Set SUPABASE_ACCESS_TOKEN environment variable.
```

### Verify Environment Variable

```bash
# Check if set
printenv | grep SUPABASE_ACCESS_TOKEN

# Should show:
# SUPABASE_ACCESS_TOKEN=sbp_...
```

---

## Resources

- **Supabase Status:** https://status.supabase.com/
- **Management API:** https://supabase.com/docs/reference/api/introduction
- **Support:** support@supabase.io

---

**Last updated:** 2026-02-21
