# ClickUp API Reference

Complete reference for `clickup_client.py` methods.

## Workspaces

### get_workspaces()

List all workspaces accessible with current API key.

**Returns:** List of workspace objects

**Example:**
```python
workspaces = client.get_workspaces()
for ws in workspaces:
    print(f"{ws['name']} (ID: {ws['id']})")
```

---

## Spaces

### get_spaces(team_id, archived=False)

List spaces in a workspace.

**Parameters:**
- `team_id` (str): Workspace ID
- `archived` (bool): Include archived spaces (default: False)

**Returns:** List of space objects

### get_space(space_id)

Get details for a specific space.

**Parameters:**
- `space_id` (str): Space ID

**Returns:** Space object

---

## Folders

### get_folders(space_id, archived=False)

List folders in a space.

**Parameters:**
- `space_id` (str): Space ID
- `archived` (bool): Include archived folders (default: False)

**Returns:** List of folder objects

### get_folder(folder_id)

Get details for a specific folder.

**Parameters:**
- `folder_id` (str): Folder ID

**Returns:** Folder object

---

## Lists

### get_lists(folder_id, archived=False)

List lists in a folder.

**Parameters:**
- `folder_id` (str): Folder ID
- `archived` (bool): Include archived lists (default: False)

**Returns:** List of list objects

### get_folderless_lists(space_id, archived=False)

List lists directly in a space (not in folders).

**Parameters:**
- `space_id` (str): Space ID
- `archived` (bool): Include archived lists (default: False)

**Returns:** List of list objects

### get_list(list_id)

Get details for a specific list.

**Parameters:**
- `list_id` (str): List ID

**Returns:** List object

---

## Tasks (Read Operations) ✅

### get_tasks(list_id, ...)

List tasks in a list with optional filtering.

**Parameters:**
- `list_id` (str): List ID
- `archived` (bool): Include archived tasks
- `page` (int): Page number for pagination
- `order_by` (str): Field to sort by
- `reverse` (bool): Reverse sort order
- `subtasks` (bool): Include subtasks
- `statuses` (list): Filter by status names
- `include_closed` (bool): Include closed tasks
- `assignees` (list): Filter by assignee IDs
- `due_date_gt` (int): Due date greater than (Unix ms)
- `due_date_lt` (int): Due date less than (Unix ms)
- `date_created_gt` (int): Created after (Unix ms)
- `date_created_lt` (int): Created before (Unix ms)
- `date_updated_gt` (int): Updated after (Unix ms)
- `date_updated_lt` (int): Updated before (Unix ms)

**Returns:** List of task objects

**Example:**
```python
# Get open tasks assigned to user 123
tasks = client.get_tasks(
    list_id='901234',
    assignees=[123],
    include_closed=False
)
```

### get_task(task_id, include_subtasks=False)

Get details for a specific task.

**Parameters:**
- `task_id` (str): Task ID
- `include_subtasks` (bool): Include subtask data

**Returns:** Task object

### search_tasks(team_id, ...)

Search tasks across entire workspace.

**Parameters:**
- `team_id` (str): Workspace ID
- All filter parameters from `get_tasks()`

**Returns:** List of task objects

**Example:**
```python
# Find all tasks assigned to user 123
tasks = client.search_tasks(
    team_id='9876',
    assignees=[123]
)
```

---

## Tasks (Write Operations) ⚠️

**IMPORTANT:** These operations require human approval before execution.

### create_task(list_id, name, ...)

Create a new task.

**Parameters:**
- `list_id` (str): List ID where task will be created
- `name` (str): Task name
- `description` (str): Task description (optional)
- `assignees` (list): Assignee user IDs (optional)
- `tags` (list): Tag names (optional)
- `status` (str): Status name (optional)
- `priority` (int): 1 (urgent) to 4 (low) (optional)
- `due_date` (int): Due date (Unix ms) (optional)
- `start_date` (int): Start date (Unix ms) (optional)

**Returns:** Created task object

**Security:** Agent should request approval before calling this.

### update_task(task_id, ...)

Update an existing task.

**Parameters:**
- `task_id` (str): Task ID to update
- Same optional parameters as `create_task()`

**Returns:** Updated task object

**Security:** Agent should request approval before calling this.

### delete_task(task_id)

Delete a task (HIGH RISK).

**Parameters:**
- `task_id` (str): Task ID to delete

**Returns:** Success response

**Security:** Agent should ALWAYS request approval before calling this. Deletion is permanent.

---

## Users

### get_current_user()

Get details for authenticated user.

**Returns:** User object with `id`, `username`, `email`, `color`, `profilePicture`

**Example:**
```python
user = client.get_current_user()
print(f"Authenticated as: {user['username']} ({user['email']})")
```

---

## Response Format

All methods return JSON objects/arrays from ClickUp API. Common fields:

**Workspace:**
- `id` (str): Workspace ID
- `name` (str): Workspace name

**Space:**
- `id` (str): Space ID
- `name` (str): Space name
- `private` (bool): Is private
- `statuses` (list): Available statuses

**Task:**
- `id` (str): Task ID
- `name` (str): Task name
- `description` (str): Task description
- `status` (obj): Current status
- `date_created` (str): Creation timestamp
- `date_updated` (str): Update timestamp
- `due_date` (str): Due date (Unix ms)
- `assignees` (list): Assigned users
- `tags` (list): Tags
- `parent` (str): Parent task ID
- `priority` (int): Priority level
- `url` (str): ClickUp URL

---

## Error Handling

All methods may raise `requests.HTTPError` for API errors:
- **401:** Authentication failed (check API key)
- **404:** Resource not found
- **429:** Rate limit exceeded
- **500:** ClickUp server error

See [error-handling.md](error-handling.md) for detailed error handling patterns.

---

## Rate Limits

- **100 requests per minute** per API key
- **10 requests per second** per API key

See [error-handling.md](error-handling.md) for rate limit best practices.

---

## External Resources

- **ClickUp API Docs:** https://clickup.com/api
- **API Reference:** https://clickup.com/api/clickupreference/operation/GetTasks/
- **Rate Limits:** https://clickup.com/api/developer-portal/rate-limits/
