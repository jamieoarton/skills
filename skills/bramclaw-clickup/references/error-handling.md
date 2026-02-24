# Error Handling and Best Practices

Error handling patterns, rate limits, and monitoring for `bramclaw-clickup`.

## Error Handling Patterns

### Basic Error Handling

```python
import requests
from scripts.clickup_client import ClickUpClient

try:
    client = ClickUpClient()
    tasks = client.get_tasks(list_id='901234')
except requests.HTTPError as e:
    if e.response.status_code == 401:
        print("Authentication failed - check CLICK_UP_API_KEY")
    elif e.response.status_code == 404:
        print("List not found - verify list_id is correct")
    elif e.response.status_code == 429:
        print("Rate limited - wait before retrying")
    elif e.response.status_code >= 500:
        print(f"ClickUp server error: {e.response.status_code}")
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

**Cause:** Invalid or missing API key

**Solution:**
```python
# Check environment variable is set
import os
api_key = os.environ.get("CLICK_UP_API_KEY")
if not api_key:
    raise ValueError("CLICK_UP_API_KEY not set in environment")

# Verify key format (should start with "pk_")
if not api_key.startswith("pk_"):
    raise ValueError("Invalid API key format (should start with 'pk_')")
```

**Fix:**
1. Verify `CLICK_UP_API_KEY` is set in container environment
2. Check key hasn't expired or been revoked
3. Generate new key in ClickUp settings if needed

---

### 404 Not Found

**Cause:** Resource doesn't exist or you don't have access

**Solutions:**
```python
# Verify resource ID is correct
try:
    task = client.get_task(task_id='abc123')
except requests.HTTPError as e:
    if e.response.status_code == 404:
        print(f"Task {task_id} not found. Check:")
        print("- Task ID is correct")
        print("- Task hasn't been deleted")
        print("- You have access to this task's workspace")
```

**Debug steps:**
1. Double-check resource ID (list_id, task_id, space_id, etc.)
2. Verify resource hasn't been archived or deleted
3. Confirm API key has access to that workspace

---

### 429 Rate Limited

**Cause:** Exceeded API rate limits

**ClickUp Rate Limits:**
- **100 requests per minute** per API key
- **10 requests per second** per API key

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
                raise  # Re-raise non-rate-limit errors
    raise Exception(f"Rate limit exceeded after {max_retries} retries")

# Usage
tasks = api_call_with_retry(client.get_tasks, list_id='901234')
```

---

### 500/503 Server Errors

**Cause:** ClickUp API is experiencing issues

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
                print(f"ClickUp server error. Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            else:
                raise
    raise Exception(f"ClickUp server unavailable after {max_retries} retries")
```

---

## Rate Limit Best Practices

### 1. Cache Workspace/Space/List IDs

**Bad (re-fetches every time):**
```python
def get_my_tasks():
    client = ClickUpClient()
    workspaces = client.get_workspaces()  # API call
    team_id = workspaces[0]['id']
    tasks = client.search_tasks(team_id=team_id, assignees=[123])  # API call
    return tasks
```

**Good (cache IDs):**
```python
# Store in config or environment
WORKSPACE_ID = '9876'
MY_USER_ID = 123

def get_my_tasks():
    client = ClickUpClient()
    tasks = client.search_tasks(team_id=WORKSPACE_ID, assignees=[MY_USER_ID])  # 1 API call
    return tasks
```

**Savings:** 2 API calls → 1 API call (50% reduction)

---

### 2. Use Filters to Reduce Response Size

**Bad (fetches everything, filters client-side):**
```python
tasks = client.get_tasks(list_id='901234')  # Gets all tasks
open_tasks = [t for t in tasks if t['status']['status'] != 'closed']
```

**Good (filters server-side):**
```python
tasks = client.get_tasks(list_id='901234', include_closed=False)  # Smaller response
```

**Savings:** Reduces response size, faster API calls

---

### 3. Paginate Large Result Sets

**Bad (fetches all tasks at once):**
```python
# If list has 1000 tasks, this returns all 1000 in one call (slow, large response)
tasks = client.get_tasks(list_id='901234')
```

**Good (paginate):**
```python
# Get first 100 tasks
page_0 = client.get_tasks(list_id='901234', page=0)  # Tasks 0-99

# Get next 100 tasks
page_1 = client.get_tasks(list_id='901234', page=1)  # Tasks 100-199

# Process incrementally
for task in page_0:
    process_task(task)
for task in page_1:
    process_task(task)
```

**Savings:** Faster responses, better memory usage

---

### 4. Batch Operations

**Bad (multiple API calls in loop):**
```python
for task_id in task_ids:
    task = client.get_task(task_id)  # 1 API call per task
    print(task['name'])
```

**Good (use search with filters):**
```python
# Get all tasks in one call
tasks = client.search_tasks(team_id='9876', task_ids=task_ids)
for task in tasks:
    print(task['name'])
```

**Note:** ClickUp API doesn't support true batching, but you can use filters to reduce calls.

---

### 5. Rate Limit Tracking

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

for list_id in list_ids:
    tracker.check_and_wait()
    tasks = client.get_tasks(list_id=list_id)
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
    filename='/var/log/bramclaw/clickup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_operation(operation, details):
    """Log ClickUp operation with structured data."""
    log_entry = {
        'timestamp': time.time(),
        'operation': operation,
        'details': details
    }
    logging.info(json.dumps(log_entry))

# Usage
log_operation('GET_TASKS', {'list_id': '901234', 'count': 42})
log_operation('CREATE_TASK', {'list_id': '901234', 'name': 'Deploy v2.0', 'task_id': 'abc456'})
```

---

### What to Log

**Always log:**
- All write operations (create/update/delete)
- Resource IDs affected
- Operation result (success/failure)
- Error codes
- Rate limit hits

**Example log entries:**
```json
{"timestamp": 1708551045, "operation": "GET_TASKS", "details": {"list_id": "901234", "count": 42}}
{"timestamp": 1708551046, "operation": "CREATE_TASK", "details": {"list_id": "901234", "name": "Deploy v2.0", "task_id": "abc456"}}
{"timestamp": 1708551047, "operation": "UPDATE_TASK", "details": {"task_id": "abc456", "status": "in progress"}}
{"timestamp": 1708551048, "operation": "ERROR", "details": {"code": 429, "message": "Rate limited"}}
```

**Never log:**
- API keys
- Full task descriptions (may contain sensitive data)
- User passwords
- Personal information (PII)

---

### Log Monitoring Script

```python
#!/usr/bin/env python3
# monitor_clickup_logs.py

import json
from collections import Counter
from datetime import datetime, timedelta

def analyze_logs(log_file='/var/log/bramclaw/clickup.log'):
    """Analyze ClickUp API usage from logs."""
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
    print("ClickUp API Usage Summary")
    print("=" * 40)
    print(f"Total operations: {sum(operations.values())}")
    print(f"\nTop operations:")
    for op, count in operations.most_common(10):
        print(f"  {op}: {count}")

    print(f"\nErrors: {len(errors)}")
    print(f"Rate limits hit: {rate_limits}")

    if rate_limits > 0:
        print("\n⚠️  WARNING: Rate limit hit. Consider:")
        print("  - Caching workspace/list IDs")
        print("  - Using server-side filters")
        print("  - Adding delays between calls")

if __name__ == '__main__':
    analyze_logs()
```

**Run:**
```bash
python3 monitor_clickup_logs.py
```

---

### Alerts

Configure alerts for:

**High Priority:**
- **Any delete operations** (high risk)
- **Failed authentication** (401 errors)
- **>3 rate limit hits in 1 hour** (usage pattern issue)

**Medium Priority:**
- **>50 API calls in 1 minute** (approaching rate limit)
- **Server errors** (500/503)
- **Unusual bulk operations** (>20 tasks created in 5 minutes)

**Alert script example:**
```python
def check_for_alerts(log_file='/var/log/bramclaw/clickup.log'):
    """Check logs for alert conditions."""
    now = time.time()
    one_hour_ago = now - 3600

    rate_limit_count = 0
    delete_operations = []

    with open(log_file, 'r') as f:
        for line in f:
            try:
                parts = line.split(' - ')
                json_data = json.loads(parts[2].strip())

                timestamp = json_data.get('timestamp', 0)
                if timestamp < one_hour_ago:
                    continue  # Skip old entries

                # Check for rate limits
                if json_data.get('operation') == 'ERROR' and \
                   json_data.get('details', {}).get('code') == 429:
                    rate_limit_count += 1

                # Check for delete operations
                if json_data.get('operation') == 'DELETE_TASK':
                    delete_operations.append(json_data)

            except (json.JSONDecodeError, IndexError):
                continue

    # Send alerts
    if rate_limit_count >= 3:
        send_alert(f"⚠️ Rate limit hit {rate_limit_count} times in last hour")

    if delete_operations:
        send_alert(f"⚠️ {len(delete_operations)} tasks deleted in last hour")

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

# Now ClickUp API calls will show detailed info
client = ClickUpClient()
tasks = client.get_tasks(list_id='901234')  # Will log request/response details
```

### Test API Key

```bash
# Quick test
python3 scripts/clickup_agent.py whoami

# Expected output:
# Jamie Oarton (jamie@bramforth.ai)

# If error:
# Error: ClickUp API key not found. Set CLICK_UP_API_KEY environment variable.
```

### Verify Environment Variable

```bash
# Check if API key is set
printenv | grep CLICK_UP_API_KEY

# Should show:
# CLICK_UP_API_KEY=pk_...
```

---

## Resources

- **ClickUp API Status:** https://status.clickup.com/
- **Rate Limits:** https://clickup.com/api/developer-portal/rate-limits/
- **Error Codes:** https://clickup.com/api/developer-portal/errors/
- **API Support:** support@clickup.com
