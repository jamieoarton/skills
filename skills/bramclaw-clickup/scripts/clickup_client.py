#!/usr/bin/env python3
"""
ClickUp API Client for bram-claw
Direct API access (no third-party proxy)

Security-first implementation with read-only default operations.
Write operations included but should require human approval.
"""

import os
import requests
from typing import Optional, Dict, List, Any


class ClickUpClient:
    """
    ClickUp API client with security-first design.

    Uses direct API access via CLICK_UP_API_KEY (no third-party proxy).
    Read operations are safe for agent use.
    Write operations should require human approval.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize ClickUp client.

        Args:
            api_key: ClickUp API key (defaults to CLICK_UP_API_KEY env var)

        Raises:
            ValueError: If API key not found
        """
        self.api_key = api_key or os.environ.get('CLICK_UP_API_KEY')
        if not self.api_key:
            raise ValueError(
                "ClickUp API key not found. Set CLICK_UP_API_KEY environment variable."
            )

        self.base_url = 'https://api.clickup.com/api/v2'
        self.headers = {
            'Authorization': self.api_key,  # ClickUp uses API key directly (no Bearer)
            'Content-Type': 'application/json'
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make HTTP request to ClickUp API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., '/team')
            **kwargs: Additional requests parameters (params, json, etc.)

        Returns:
            JSON response dict (or empty dict for DELETE)

        Raises:
            requests.HTTPError: On 4xx/5xx responses
        """
        url = f'{self.base_url}{endpoint}'

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            **kwargs
        )

        response.raise_for_status()  # Raise exception for 4xx/5xx

        # DELETE operations may return empty responses
        if method == 'DELETE':
            return {} if not response.content else response.json()

        return response.json()

    # ========================================================================
    # WORKSPACES (TEAMS) - Read-Only
    # ========================================================================

    def get_workspaces(self) -> List[Dict[str, Any]]:
        """
        Get authorized workspaces (teams).

        Returns:
            List of workspace dicts with 'id', 'name', 'members', etc.

        Example:
            >>> client = ClickUpClient()
            >>> workspaces = client.get_workspaces()
            >>> print(workspaces[0]['name'])
            'My Workspace'
        """
        data = self._request('GET', '/team')
        return data.get('teams', [])

    # ========================================================================
    # SPACES - Read-Only
    # ========================================================================

    def get_spaces(self, team_id: str, archived: bool = False) -> List[Dict[str, Any]]:
        """
        Get spaces in a workspace.

        Args:
            team_id: Workspace (team) ID
            archived: Include archived spaces

        Returns:
            List of space dicts

        Example:
            >>> spaces = client.get_spaces(team_id='1234567')
            >>> print(spaces[0]['name'])
            'Engineering'
        """
        params = {'archived': str(archived).lower()}
        data = self._request('GET', f'/team/{team_id}/space', params=params)
        return data.get('spaces', [])

    def get_space(self, space_id: str) -> Dict[str, Any]:
        """
        Get space details.

        Args:
            space_id: Space ID

        Returns:
            Space dict with details
        """
        return self._request('GET', f'/space/{space_id}')

    # ========================================================================
    # FOLDERS - Read-Only
    # ========================================================================

    def get_folders(self, space_id: str, archived: bool = False) -> List[Dict[str, Any]]:
        """
        Get folders in a space.

        Args:
            space_id: Space ID
            archived: Include archived folders

        Returns:
            List of folder dicts
        """
        params = {'archived': str(archived).lower()}
        data = self._request('GET', f'/space/{space_id}/folder', params=params)
        return data.get('folders', [])

    def get_folder(self, folder_id: str) -> Dict[str, Any]:
        """Get folder details."""
        return self._request('GET', f'/folder/{folder_id}')

    # ========================================================================
    # LISTS - Read-Only
    # ========================================================================

    def get_lists(self, folder_id: str, archived: bool = False) -> List[Dict[str, Any]]:
        """
        Get lists in a folder.

        Args:
            folder_id: Folder ID
            archived: Include archived lists

        Returns:
            List of list dicts
        """
        params = {'archived': str(archived).lower()}
        data = self._request('GET', f'/folder/{folder_id}/list', params=params)
        return data.get('lists', [])

    def get_folderless_lists(self, space_id: str, archived: bool = False) -> List[Dict[str, Any]]:
        """
        Get lists not in any folder (directly in space).

        Args:
            space_id: Space ID
            archived: Include archived lists

        Returns:
            List of list dicts
        """
        params = {'archived': str(archived).lower()}
        data = self._request('GET', f'/space/{space_id}/list', params=params)
        return data.get('lists', [])

    def get_list(self, list_id: str) -> Dict[str, Any]:
        """
        Get list details.

        Args:
            list_id: List ID

        Returns:
            List dict with details
        """
        return self._request('GET', f'/list/{list_id}')

    # ========================================================================
    # TASKS - Read-Only Operations
    # ========================================================================

    def get_tasks(
        self,
        list_id: str,
        archived: bool = False,
        page: int = 0,
        include_closed: bool = False,
        assignees: Optional[List[int]] = None,
        statuses: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Get tasks in a list.

        Args:
            list_id: List ID
            archived: Include archived tasks
            page: Page number (0-indexed, 100 tasks per page)
            include_closed: Include closed tasks
            assignees: Filter by assignee user IDs
            statuses: Filter by status names

        Returns:
            List of task dicts

        Example:
            >>> tasks = client.get_tasks(list_id='901234', include_closed=True)
            >>> for task in tasks:
            ...     print(f"{task['name']} - {task['status']['status']}")
        """
        params = {
            'archived': str(archived).lower(),
            'page': page,
            'include_closed': str(include_closed).lower()
        }

        if assignees:
            params['assignees[]'] = assignees
        if statuses:
            params['statuses[]'] = statuses

        data = self._request('GET', f'/list/{list_id}/task', params=params)
        return data.get('tasks', [])

    def get_task(self, task_id: str, include_subtasks: bool = False) -> Dict[str, Any]:
        """
        Get task details.

        Args:
            task_id: Task ID
            include_subtasks: Include subtasks in response

        Returns:
            Task dict with full details

        Example:
            >>> task = client.get_task(task_id='abc123')
            >>> print(f"{task['name']}: {task['description']}")
        """
        params = {'include_subtasks': str(include_subtasks).lower()}
        return self._request('GET', f'/task/{task_id}', params=params)

    def search_tasks(
        self,
        team_id: str,
        page: int = 0,
        order_by: str = 'created',
        assignees: Optional[List[int]] = None,
        statuses: Optional[List[str]] = None,
        list_ids: Optional[List[str]] = None,
        space_ids: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Search tasks across entire workspace.

        Args:
            team_id: Workspace (team) ID
            page: Page number
            order_by: Sort field (created, updated, due_date)
            assignees: Filter by assignee user IDs
            statuses: Filter by status names
            list_ids: Filter by list IDs
            space_ids: Filter by space IDs

        Returns:
            List of task dicts matching filters

        Example:
            >>> tasks = client.search_tasks(
            ...     team_id='1234567',
            ...     assignees=[123],
            ...     statuses=['in progress']
            ... )
        """
        params = {
            'page': page,
            'order_by': order_by
        }

        if assignees:
            params['assignees[]'] = assignees
        if statuses:
            params['statuses[]'] = statuses
        if list_ids:
            params['list_ids[]'] = list_ids
        if space_ids:
            params['space_ids[]'] = space_ids

        data = self._request('GET', f'/team/{team_id}/task', params=params)
        return data.get('tasks', [])

    # ========================================================================
    # TASKS - Write Operations (REQUIRE APPROVAL)
    # ========================================================================

    def create_task(
        self,
        list_id: str,
        name: str,
        description: Optional[str] = None,
        assignees: Optional[List[int]] = None,
        status: Optional[str] = None,
        priority: Optional[int] = None,
        due_date: Optional[int] = None,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Create a task.

        ⚠️ SECURITY: This writes data. Require human approval before calling.

        Args:
            list_id: List ID to create task in
            name: Task name (required)
            description: Task description (markdown supported)
            assignees: List of assignee user IDs
            status: Status name (must match a status in the list)
            priority: 1=urgent, 2=high, 3=normal, 4=low, None=no priority
            due_date: Unix timestamp in milliseconds
            tags: List of tag names

        Returns:
            Created task dict

        Example:
            >>> task = client.create_task(
            ...     list_id='901234',
            ...     name='Complete API integration',
            ...     description='Integrate with payment API',
            ...     priority=2,
            ...     assignees=[123]
            ... )
        """
        task_data = {'name': name}

        if description:
            task_data['description'] = description
        if assignees:
            task_data['assignees'] = assignees
        if status:
            task_data['status'] = status
        if priority is not None:
            task_data['priority'] = priority
        if due_date:
            task_data['due_date'] = due_date
        if tags:
            task_data['tags'] = tags

        return self._request('POST', f'/list/{list_id}/task', json=task_data)

    def update_task(
        self,
        task_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[int] = None,
        assignees: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        """
        Update a task.

        ⚠️ SECURITY: This modifies data. Require human approval before calling.

        Args:
            task_id: Task ID
            name: New task name
            description: New description
            status: New status
            priority: New priority (use None to clear)
            assignees: New assignees list

        Returns:
            Updated task dict

        Example:
            >>> client.update_task(
            ...     task_id='abc123',
            ...     status='complete',
            ...     priority=None  # Clear priority
            ... )
        """
        update_data = {}

        if name:
            update_data['name'] = name
        if description is not None:
            update_data['description'] = description
        if status:
            update_data['status'] = status
        if priority is not None:
            update_data['priority'] = priority
        if assignees is not None:
            update_data['assignees'] = assignees

        return self._request('PUT', f'/task/{task_id}', json=update_data)

    def delete_task(self, task_id: str) -> None:
        """
        Delete a task.

        ⚠️ SECURITY: HIGH RISK - permanent deletion.
        Require explicit approval and confirmation.

        Args:
            task_id: Task ID to delete
        """
        self._request('DELETE', f'/task/{task_id}')

    # ========================================================================
    # USERS - Read-Only
    # ========================================================================

    def get_current_user(self) -> Dict[str, Any]:
        """
        Get current authenticated user info.

        Returns:
            User dict with id, username, email, etc.

        Example:
            >>> user = client.get_current_user()
            >>> print(f"Logged in as: {user['username']} ({user['email']})")
        """
        data = self._request('GET', '/user')
        return data.get('user', {})


# ============================================================================
# EXAMPLE USAGE / TESTING
# ============================================================================

def main():
    """Example usage of ClickUp client."""
    print("=" * 80)
    print("ClickUp API Client Test")
    print("=" * 80)

    try:
        client = ClickUpClient()
        print("✓ Client initialized\n")

        # Get current user
        print("Fetching current user...")
        user = client.get_current_user()
        print(f"✓ Logged in as: {user.get('username')} ({user.get('email')})\n")

        # Get workspaces
        print("Fetching workspaces...")
        workspaces = client.get_workspaces()
        print(f"✓ Found {len(workspaces)} workspace(s):")
        for workspace in workspaces:
            print(f"  - {workspace['name']} (ID: {workspace['id']})")

        if not workspaces:
            print("\nNo workspaces found!")
            return

        # Get spaces in first workspace
        team_id = workspaces[0]['id']
        print(f"\nFetching spaces in workspace '{workspaces[0]['name']}'...")
        spaces = client.get_spaces(team_id)
        print(f"✓ Found {len(spaces)} space(s):")
        for space in spaces:
            print(f"  - {space['name']} (ID: {space['id']})")

        print("\n" + "=" * 80)
        print("✓ All tests passed!")
        print("=" * 80)

    except ValueError as e:
        print(f"✗ Configuration error: {e}")
        print("\nMake sure CLICK_UP_API_KEY is set in your .env file")
    except requests.HTTPError as e:
        print(f"✗ API error: {e}")
        print("\nCheck that your ClickUp API key is valid")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


if __name__ == '__main__':
    main()
