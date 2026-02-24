#!/usr/bin/env python3
"""
GitHub API client for OpenClaw bramclaw-github skill.
Provides simple interface to GitHub REST API using personal access token.
"""

import os
import requests
from typing import Dict, List, Optional


class GitHubClient:
    """GitHub API client with personal access token authentication."""

    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub client.

        Args:
            token: GitHub personal access token. If not provided, reads from GITHUB_TOKEN env var.
        """
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GITHUB_TOKEN is not set")

        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make authenticated request to GitHub API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json() if response.content else {}

    def get_current_user(self) -> Dict:
        """Get authenticated user information."""
        return self._request("GET", "/user")

    def list_issues(self, repo: str, state: str = "open", **filters) -> List[Dict]:
        """
        List issues in a repository.

        Args:
            repo: Repository in format "owner/repo"
            state: Issue state (open, closed, all)
            **filters: Additional query parameters (assignee, labels, etc.)
        """
        params = {"state": state, **filters}
        return self._request("GET", f"/repos/{repo}/issues", params=params)

    def get_issue(self, repo: str, issue_number: int) -> Dict:
        """Get details of a specific issue."""
        return self._request("GET", f"/repos/{repo}/issues/{issue_number}")

    def create_issue(self, repo: str, title: str, body: Optional[str] = None,
                     assignees: Optional[List[str]] = None,
                     labels: Optional[List[str]] = None) -> Dict:
        """
        Create a new issue.

        Args:
            repo: Repository in format "owner/repo"
            title: Issue title
            body: Issue description
            assignees: List of usernames to assign
            labels: List of label names
        """
        data = {"title": title}
        if body:
            data["body"] = body
        if assignees:
            data["assignees"] = assignees
        if labels:
            data["labels"] = labels

        return self._request("POST", f"/repos/{repo}/issues", json=data)

    def update_issue(self, repo: str, issue_number: int, **updates) -> Dict:
        """
        Update an existing issue.

        Args:
            repo: Repository in format "owner/repo"
            issue_number: Issue number
            **updates: Fields to update (title, body, state, labels, assignees)
        """
        return self._request("PATCH", f"/repos/{repo}/issues/{issue_number}", json=updates)

    def list_pull_requests(self, repo: str, state: str = "open", **filters) -> List[Dict]:
        """
        List pull requests in a repository.

        Args:
            repo: Repository in format "owner/repo"
            state: PR state (open, closed, all)
            **filters: Additional query parameters
        """
        params = {"state": state, **filters}
        return self._request("GET", f"/repos/{repo}/pulls", params=params)

    def get_pull_request(self, repo: str, pr_number: int) -> Dict:
        """Get details of a specific pull request."""
        return self._request("GET", f"/repos/{repo}/pulls/{pr_number}")

    def search_issues(self, query: str, **filters) -> List[Dict]:
        """
        Search issues across GitHub.

        Args:
            query: Search query (e.g., "is:issue is:open repo:owner/repo")
            **filters: Additional query parameters
        """
        params = {"q": query, **filters}
        result = self._request("GET", "/search/issues", params=params)
        return result.get("items", [])


if __name__ == "__main__":
    # Quick test
    client = GitHubClient()
    user = client.get_current_user()
    print(f"Authenticated as: {user['login']} ({user.get('name', 'No name set')})")
