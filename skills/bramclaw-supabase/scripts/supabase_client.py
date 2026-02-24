#!/usr/bin/env python3
"""
Supabase Management API Client for bram-claw
Direct API access (no third-party proxy)

Security-first implementation with read-only default operations.
Write operations included but should require human approval.

API Documentation: https://supabase.com/docs/reference/api/introduction
"""

import os
import requests
from typing import Optional, Dict, List, Any
from datetime import datetime, timedelta


class SupabaseClient:
    """
    Supabase Management API client with security-first design.

    Uses direct API access via SUPABASE_ACCESS_TOKEN (Personal Access Token).
    Read operations are safe for agent use.
    Write operations should require human approval.
    """

    def __init__(self, access_token: Optional[str] = None):
        """
        Initialize Supabase client.

        Args:
            access_token: Supabase Personal Access Token
                         (defaults to SUPABASE_ACCESS_TOKEN env var)

        Raises:
            ValueError: If access token not found
        """
        self.access_token = access_token or os.environ.get('SUPABASE_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError(
                "Supabase access token not found. Set SUPABASE_ACCESS_TOKEN environment variable."
            )

        self.base_url = 'https://api.supabase.com/v1'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        Make HTTP request to Supabase Management API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            endpoint: API endpoint (without base URL)
            **kwargs: Additional arguments for requests.request()

        Returns:
            JSON response as dict

        Raises:
            requests.HTTPError: If request fails
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            **kwargs
        )
        response.raise_for_status()

        # Handle empty responses (204 No Content, etc.)
        if response.status_code == 204 or not response.content:
            return {}

        return response.json()

    # ========================================================================
    # ORGANIZATIONS - Read-Only
    # ========================================================================

    def get_organizations(self) -> List[Dict[str, Any]]:
        """
        Get all organizations user belongs to.

        Returns:
            List of organization dicts with id, name, billing_email, etc.

        Example:
            >>> orgs = client.get_organizations()
            >>> print(f"Found {len(orgs)} organizations")
        """
        return self._request('GET', '/organizations')

    # ========================================================================
    # PROJECTS - Read-Only
    # ========================================================================

    def get_projects(self) -> List[Dict[str, Any]]:
        """
        Get all projects across all organizations.

        Returns:
            List of project dicts with id, name, organization_id, region, etc.

        Example:
            >>> projects = client.get_projects()
            >>> for project in projects:
            ...     print(f"{project['name']} - {project['region']}")
        """
        return self._request('GET', '/projects')

    def get_project(self, project_ref: str) -> Dict[str, Any]:
        """
        Get details for a specific project.

        Args:
            project_ref: Project reference ID (e.g., 'ovrxdoyvkyrczsxhvada')

        Returns:
            Project dict with detailed information

        Example:
            >>> project = client.get_project('ovrxdoyvkyrczsxhvada')
            >>> print(f"Project: {project['name']} ({project['status']})")
        """
        return self._request('GET', f'/projects/{project_ref}')

    def get_project_api_keys(self, project_ref: str) -> List[Dict[str, Any]]:
        """
        Get API keys for a project (anon, service_role).

        Args:
            project_ref: Project reference ID

        Returns:
            List of API key dicts with name and api_key

        Example:
            >>> keys = client.get_project_api_keys('abc123')
            >>> anon_key = [k for k in keys if k['name'] == 'anon'][0]
        """
        return self._request('GET', f'/projects/{project_ref}/api-keys')

    # ========================================================================
    # SECURITY ADVISOR - Read-Only
    # ========================================================================

    def get_security_advisors(self, project_ref: str) -> List[Dict[str, Any]]:
        """
        Get security advisor recommendations for a project.

        This is the endpoint for handling email alerts like:
        "We detected security vulnerabilities in 1 of your projects..."

        Args:
            project_ref: Project reference ID

        Returns:
            List of security lint findings with:
            - name: Lint rule name (e.g., 'rls_disabled_in_public')
            - title: Human-readable title
            - level: ERROR, WARNING, or INFO
            - categories: List of categories (e.g., ['SECURITY'])
            - description: What the issue is
            - detail: Specific details about this finding
            - remediation: URL to fix documentation
            - metadata: Additional context (table name, schema, etc.)

        Example:
            >>> advisors = client.get_security_advisors('ovrxdoyvkyrczsxhvada')
            >>> errors = [a for a in advisors if a['level'] == 'ERROR']
            >>> print(f"Found {len(errors)} ERROR-level issues")
        """
        response = self._request('GET', f'/projects/{project_ref}/advisors/security')
        # Extract the lints array from the response
        return response.get('lints', [])

    def get_performance_advisors(self, project_ref: str) -> List[Dict[str, Any]]:
        """
        Get performance advisor recommendations for a project.

        Similar to security advisors but focuses on performance issues like
        missing indexes, slow queries, inefficient table structures.

        Args:
            project_ref: Project reference ID

        Returns:
            List of performance lint findings with same structure as security advisors:
            - name, title, level, categories, description, detail, remediation, metadata

        Example:
            >>> advisors = client.get_performance_advisors('ovrxdoyvkyrczsxhvada')
            >>> errors = [a for a in advisors if a['level'] == 'ERROR']
            >>> missing_indexes = [a for a in advisors if 'index' in a.get('name', '').lower()]
        """
        response = self._request('GET', f'/projects/{project_ref}/advisors/performance')
        # Extract the lints array from the response
        return response.get('lints', [])

    # ========================================================================
    # LOGS - Read-Only
    # ========================================================================

    def get_logs(
        self,
        project_ref: str,
        service: str = 'postgres',
        iso_timestamp_start: Optional[str] = None,
        iso_timestamp_end: Optional[str] = None,
        query: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get logs for a project service.

        Args:
            project_ref: Project reference ID
            service: Service name (postgres, auth, realtime, storage, edge-function)
            iso_timestamp_start: Start timestamp (ISO format, defaults to 1 min ago)
            iso_timestamp_end: End timestamp (ISO format, defaults to now)
            query: Optional SQL query to filter logs

        Returns:
            List of log entries

        Note:
            Timestamp range must be <= 24 hours

        Example:
            >>> # Get last hour of postgres logs
            >>> logs = client.get_logs(
            ...     'abc123',
            ...     service='postgres',
            ...     iso_timestamp_start='2026-02-20T10:00:00Z',
            ...     iso_timestamp_end='2026-02-20T11:00:00Z'
            ... )
        """
        # Default to last 1 minute if not specified
        if not iso_timestamp_start:
            start = datetime.utcnow() - timedelta(minutes=1)
            iso_timestamp_start = start.isoformat() + 'Z'

        if not iso_timestamp_end:
            iso_timestamp_end = datetime.utcnow().isoformat() + 'Z'

        params = {
            'iso_timestamp_start': iso_timestamp_start,
            'iso_timestamp_end': iso_timestamp_end
        }

        if query:
            params['query'] = query

        return self._request(
            'GET',
            f'/projects/{project_ref}/analytics/endpoints/logs.{service}',
            params=params
        )

    # ========================================================================
    # DATABASE - Read-Only (Query)
    # ========================================================================

    def execute_query(self, project_ref: str, query: str) -> Dict[str, Any]:
        """
        Execute SQL query on the project database.

        Args:
            project_ref: Project reference ID
            query: SQL query to execute

        Returns:
            Query results

        ⚠️ SECURITY WARNING:
            This method accepts ANY SQL and sends it to production database.
            The API endpoint itself may have server-side restrictions.

            For agent safety, the supabase_agent.py wrapper enforces read-only
            (SELECT/EXPLAIN/SHOW/DESCRIBE only) before calling this method.

            Direct use of this client bypasses that safety check.
            Mutations (UPDATE/DELETE/INSERT/DROP/ALTER) REQUIRE human approval.

        Example:
            >>> result = client.execute_query(
            ...     'abc123',
            ...     'SELECT COUNT(*) FROM users'
            ... )
        """
        return self._request(
            'POST',
            f'/projects/{project_ref}/database/query',
            json={'query': query}
        )

    # ========================================================================
    # PROJECTS - Write Operations (Require Approval) ⚠️
    # ========================================================================

    def create_project(
        self,
        organization_id: str,
        name: str,
        db_pass: str,
        region: str = 'us-east-1',
        plan: str = 'free'
    ) -> Dict[str, Any]:
        """
        Create a new Supabase project.

        ⚠️ REQUIRES HUMAN APPROVAL - Creates billable resource

        Args:
            organization_id: Organization ID to create project in
            name: Project name
            db_pass: Database password (min 12 chars)
            region: AWS region (us-east-1, eu-west-1, ap-southeast-1, etc.)
            plan: Pricing plan (free, pro, team, enterprise)

        Returns:
            Created project dict

        Example:
            >>> project = client.create_project(
            ...     organization_id='abc123',
            ...     name='my-new-project',
            ...     db_pass='super-secret-password-123',
            ...     region='us-east-1'
            ... )
        """
        payload = {
            'organization_id': organization_id,
            'name': name,
            'db_pass': db_pass,
            'region': region,
            'plan': plan
        }
        return self._request('POST', '/projects', json=payload)

    def pause_project(self, project_ref: str) -> Dict[str, Any]:
        """
        Pause a project (stops compute, keeps data).

        ⚠️ REQUIRES HUMAN APPROVAL - Service interruption

        Args:
            project_ref: Project reference ID

        Returns:
            Updated project status
        """
        return self._request('POST', f'/projects/{project_ref}/pause')

    def restore_project(self, project_ref: str) -> Dict[str, Any]:
        """
        Restore a paused project.

        ⚠️ REQUIRES HUMAN APPROVAL - Restarts compute

        Args:
            project_ref: Project reference ID

        Returns:
            Updated project status
        """
        return self._request('POST', f'/projects/{project_ref}/restore')

    # ========================================================================
    # DATABASE - Write Operations (Require Approval) ⚠️
    # ========================================================================

    def execute_migration(
        self,
        project_ref: str,
        name: str,
        sql: str
    ) -> Dict[str, Any]:
        """
        Apply a database migration.

        ⚠️ REQUIRES HUMAN APPROVAL - DDL changes to production database

        Args:
            project_ref: Project reference ID
            name: Migration name (will be prefixed with timestamp)
            sql: SQL to execute

        Returns:
            Migration result

        Example:
            >>> result = client.execute_migration(
            ...     'abc123',
            ...     'add_users_table',
            ...     'CREATE TABLE users (id UUID PRIMARY KEY, email TEXT);'
            ... )
        """
        payload = {
            'name': name,
            'statements': [{'sql': sql}]
        }
        return self._request(
            'POST',
            f'/projects/{project_ref}/database/migrations',
            json=payload
        )

    # ========================================================================
    # UTILITY METHODS
    # ========================================================================

    def get_current_user(self) -> Dict[str, Any]:
        """
        Get current authenticated user info (implied from token).

        This endpoint doesn't exist in the API, but we can infer from organizations.
        """
        orgs = self.get_organizations()
        if orgs:
            # Return first org owner info as proxy for user
            return {
                'organizations': [org['id'] for org in orgs],
                'organization_count': len(orgs)
            }
        return {}


# ============================================================================
# EXAMPLE USAGE / TESTING
# ============================================================================

def main():
    """Example usage of Supabase client."""
    print("=" * 80)
    print("Supabase Management API Client Test")
    print("=" * 80)

    try:
        client = SupabaseClient()
        print("✓ Client initialized\n")

        # Get organizations
        print("Fetching organizations...")
        orgs = client.get_organizations()
        print(f"✓ Found {len(orgs)} organization(s):")
        for org in orgs:
            print(f"  - {org.get('name', 'Unnamed')} (ID: {org['id']})")

        # Get projects
        print("\nFetching projects...")
        projects = client.get_projects()
        print(f"✓ Found {len(projects)} project(s):")
        for project in projects:
            print(f"  - {project['name']} ({project['region']}) - ID: {project['id']}")

        if projects:
            # Check security advisors for first project
            project_ref = projects[0]['id']
            print(f"\nFetching security advisors for '{projects[0]['name']}'...")
            advisors = client.get_security_advisors(project_ref)
            print(f"✓ Found {len(advisors)} security findings")

            high_severity = [a for a in advisors if a.get('confidence') == 'HIGH']
            if high_severity:
                print(f"  ⚠️  {len(high_severity)} HIGH confidence issues found")

        print("\n" + "=" * 80)
        print("✓ All tests passed!")
        print("=" * 80)

    except ValueError as e:
        print(f"✗ Configuration error: {e}")
        print("\nMake sure SUPABASE_ACCESS_TOKEN is set in your .env file")
    except requests.HTTPError as e:
        print(f"✗ API error: {e}")
        print("\nCheck that your Supabase access token is valid")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


if __name__ == '__main__':
    main()
