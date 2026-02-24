#!/usr/bin/env python3
"""
Scrape ClickUp API documentation from developer.clickup.com/reference/

This script fetches all API endpoint documentation by appending .md to the URLs.
"""

import requests
import time
import os
from pathlib import Path
from typing import List, Dict

# Base URL for ClickUp API docs
BASE_URL = "https://developer.clickup.com/reference"

# All known endpoint slugs (from browsing the API reference)
# Organized by category for better structure
ENDPOINTS = {
    "authorization": [
        "getaccesstoken",
        "getauthorizeduser",
        "getauthorizedteams",
    ],
    "tasks": [
        "gettasks",
        "gettask",
        "createtask",
        "updatetask",
        "deletetask",
        "getfilteredteamtasks",
        "gettaskstemplates",
        "createtaskfromtemplate",
        "getbulktasksupdate",
    ],
    "lists": [
        "getlists",
        "getlist",
        "createlist",
        "updatelist",
        "deletelist",
        "addtasktolist",
        "removetaskfromlist",
        "getlistviews",
    ],
    "folders": [
        "getfolders",
        "getfolder",
        "createfolder",
        "updatefolder",
        "deletefolder",
    ],
    "spaces": [
        "getspaces",
        "getspace",
        "createspace",
        "updatespace",
        "deletespace",
        "getspacetags",
        "createspacetag",
        "editspacetag",
        "deletespacetag",
    ],
    "teams": [
        "getteams",
        "createteamworkspace",
        "getteamseats",
        "getteamplan",
    ],
    "comments": [
        "gettaskcomments",
        "getlistcomments",
        "getchatviewcomments",
        "createtaskcomment",
        "createlistcomment",
        "createchatviewcomment",
        "updatecomment",
        "deletecomment",
    ],
    "attachments": [
        "createtaskattachment",
    ],
    "checklists": [
        "createchecklist",
        "editchecklist",
        "deletechecklist",
        "createchecklistitem",
        "editchecklistitem",
        "deletechecklistitem",
    ],
    "custom_fields": [
        "getaccessiblecustomfields",
        "setcustomfieldvalue",
        "removecustomfieldvalue",
    ],
    "dependencies": [
        "adddependency",
        "deletedependency",
        "addtasklink",
        "deletetasklink",
    ],
    "members": [
        "getteammembers",
        "getlistmembers",
        "gettaskmembers",
    ],
    "goals": [
        "getgoals",
        "getgoal",
        "creategoal",
        "updategoal",
        "deletegoal",
        "createkeyresult",
        "editkeyresult",
        "deletekeyresult",
    ],
    "guests": [
        "inviteguesttoworkspace",
        "editguestonworkspace",
        "removeguestfromworkspace",
        "getguest",
        "addguesttolist",
        "removeguestfromlist",
        "addguesttofolder",
        "removeguestfromfolder",
    ],
    "custom_roles": [
        "getcustomroles",
    ],
    "sharing": [
        "sharehierarchy",
    ],
    "tags": [
        "getspacetags",
        "createspacetag",
        "editspacetag",
        "deletespacetag",
        "addtagtotask",
        "removetagfromtask",
    ],
    "time_tracking": [
        "gettimeentrieswithinadaterange",
        "getsingulartimeentry",
        "getalltagsfromtimeentries",
        "getrunningtimeentry",
        "createatimeentry",
        "removetags",
        "gettimeentryhistory",
        "updateatimeentry",
        "deleteatimeentry",
        "startatimeentry",
        "stopatimeentry",
    ],
    "views": [
        "getteamviews",
        "getspaceviews",
        "getfolderviews",
        "getlistviews",
        "getview",
        "createteamview",
        "createspaceview",
        "createfolderview",
        "createlistview",
        "updateview",
        "deleteview",
        "getviewtasks",
    ],
    "webhooks": [
        "createwebhook",
        "updatewebhook",
        "deletewebhook",
        "getwebhooks",
    ],
    "user_groups": [
        "getusergroups",
        "updateusergroup",
    ],
}


def fetch_endpoint_docs(slug: str) -> str:
    """
    Fetch markdown documentation for a specific endpoint.

    Args:
        slug: The endpoint slug (e.g., 'getaccesstoken')

    Returns:
        Markdown content as string
    """
    url = f"{BASE_URL}/{slug}.md"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {slug}: {e}")
        return None


def save_docs(category: str, slug: str, content: str, output_dir: Path):
    """
    Save documentation to organized directory structure.

    Args:
        category: Category name (e.g., 'tasks')
        slug: Endpoint slug
        content: Markdown content
        output_dir: Base output directory
    """
    category_dir = output_dir / category
    category_dir.mkdir(parents=True, exist_ok=True)

    file_path = category_dir / f"{slug}.md"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Saved: {category}/{slug}.md")


def create_index(output_dir: Path):
    """Create index file with all categories and endpoints."""

    index_content = """# ClickUp API v2 Reference Documentation

> Scraped from https://developer.clickup.com/reference/

## Categories

"""

    for category, slugs in sorted(ENDPOINTS.items()):
        category_title = category.replace('_', ' ').title()
        index_content += f"\n### {category_title}\n\n"

        for slug in sorted(slugs):
            file_path = f"{category}/{slug}.md"
            slug_title = slug.replace('get', 'Get ').replace('create', 'Create ') \
                            .replace('update', 'Update ').replace('delete', 'Delete ') \
                            .replace('edit', 'Edit ').replace('add', 'Add ') \
                            .replace('remove', 'Remove ').title()
            index_content += f"- [{slug_title}]({file_path})\n"

    index_content += f"\n---\n\n**Total endpoints:** {sum(len(v) for v in ENDPOINTS.values())}\n"
    index_content += f"**Last updated:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"

    with open(output_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"\n✓ Created index: README.md")


def main():
    """Main scraper function."""

    # Output directory
    output_dir = Path(__file__).parent.parent / "docs" / "clickup-api-reference"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("ClickUp API Documentation Scraper")
    print("=" * 80)
    print(f"Output directory: {output_dir}")
    print(f"Total endpoints to fetch: {sum(len(v) for v in ENDPOINTS.values())}\n")

    # Fetch all endpoints
    total = 0
    successful = 0
    failed = []

    for category, slugs in ENDPOINTS.items():
        print(f"\nFetching {category}...")

        for slug in slugs:
            total += 1
            content = fetch_endpoint_docs(slug)

            if content:
                save_docs(category, slug, content, output_dir)
                successful += 1
            else:
                failed.append(f"{category}/{slug}")

            # Rate limiting - be nice to the server
            time.sleep(0.5)

    # Create index
    create_index(output_dir)

    # Summary
    print("\n" + "=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"Total endpoints: {total}")
    print(f"Successfully fetched: {successful}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed endpoints:")
        for endpoint in failed:
            print(f"  - {endpoint}")

    print("\n✓ Documentation scraping complete!")
    print(f"Documentation saved to: {output_dir}")


if __name__ == '__main__':
    main()
