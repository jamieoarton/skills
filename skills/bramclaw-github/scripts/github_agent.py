#!/usr/bin/env python3
"""
GitHub Agent CLI for OpenClaw bramclaw-github skill.
Command-line interface for GitHub operations.
"""

import sys
import json
import argparse
from github_client import GitHubClient


def main():
    parser = argparse.ArgumentParser(description="GitHub Agent CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # whoami
    subparsers.add_parser("whoami", help="Show authenticated user")

    # list-issues
    list_issues = subparsers.add_parser("list-issues", help="List repository issues")
    list_issues.add_argument("repo", help="Repository (owner/repo)")
    list_issues.add_argument("--state", default="open", choices=["open", "closed", "all"])
    list_issues.add_argument("--assignee", help="Filter by assignee")
    list_issues.add_argument("--labels", help="Filter by labels (comma-separated)")

    # get-issue
    get_issue = subparsers.add_parser("get-issue", help="Get issue details")
    get_issue.add_argument("repo", help="Repository (owner/repo)")
    get_issue.add_argument("number", type=int, help="Issue number")

    # create-issue
    create_issue = subparsers.add_parser("create-issue", help="Create new issue")
    create_issue.add_argument("repo", help="Repository (owner/repo)")
    create_issue.add_argument("title", help="Issue title")
    create_issue.add_argument("--body", help="Issue body/description")
    create_issue.add_argument("--labels", help="Labels (comma-separated)")
    create_issue.add_argument("--assignees", help="Assignees (comma-separated)")

    # update-issue
    update_issue = subparsers.add_parser("update-issue", help="Update existing issue")
    update_issue.add_argument("repo", help="Repository (owner/repo)")
    update_issue.add_argument("number", type=int, help="Issue number")
    update_issue.add_argument("--title", help="New title")
    update_issue.add_argument("--body", help="New body")
    update_issue.add_argument("--state", choices=["open", "closed"], help="Issue state")
    update_issue.add_argument("--labels", help="Labels (comma-separated)")
    update_issue.add_argument("--assignees", help="Assignees (comma-separated)")

    # list-prs
    list_prs = subparsers.add_parser("list-prs", help="List pull requests")
    list_prs.add_argument("repo", help="Repository (owner/repo)")
    list_prs.add_argument("--state", default="open", choices=["open", "closed", "all"])

    # get-pr
    get_pr = subparsers.add_parser("get-pr", help="Get pull request details")
    get_pr.add_argument("repo", help="Repository (owner/repo)")
    get_pr.add_argument("number", type=int, help="PR number")

    # search-issues
    search = subparsers.add_parser("search-issues", help="Search issues")
    search.add_argument("query", help="Search query (GitHub search syntax)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    try:
        client = GitHubClient()

        if args.command == "whoami":
            user = client.get_current_user()
            print(json.dumps({
                "login": user["login"],
                "name": user.get("name"),
                "email": user.get("email"),
                "id": user["id"]
            }, indent=2))

        elif args.command == "list-issues":
            filters = {}
            if args.assignee:
                filters["assignee"] = args.assignee
            if args.labels:
                filters["labels"] = args.labels

            issues = client.list_issues(args.repo, state=args.state, **filters)
            print(json.dumps([{
                "number": i["number"],
                "title": i["title"],
                "state": i["state"],
                "user": i["user"]["login"],
                "labels": [l["name"] for l in i.get("labels", [])],
                "assignees": [a["login"] for a in i.get("assignees", [])],
                "created_at": i["created_at"],
                "updated_at": i["updated_at"],
                "html_url": i["html_url"]
            } for i in issues], indent=2))

        elif args.command == "get-issue":
            issue = client.get_issue(args.repo, args.number)
            print(json.dumps({
                "number": issue["number"],
                "title": issue["title"],
                "body": issue.get("body"),
                "state": issue["state"],
                "user": issue["user"]["login"],
                "labels": [l["name"] for l in issue.get("labels", [])],
                "assignees": [a["login"] for a in issue.get("assignees", [])],
                "created_at": issue["created_at"],
                "updated_at": issue["updated_at"],
                "closed_at": issue.get("closed_at"),
                "comments": issue.get("comments", 0),
                "html_url": issue["html_url"]
            }, indent=2))

        elif args.command == "create-issue":
            kwargs = {"title": args.title}
            if args.body:
                kwargs["body"] = args.body
            if args.labels:
                kwargs["labels"] = [l.strip() for l in args.labels.split(",")]
            if args.assignees:
                kwargs["assignees"] = [a.strip() for a in args.assignees.split(",")]

            issue = client.create_issue(args.repo, **kwargs)
            print(json.dumps({
                "number": issue["number"],
                "title": issue["title"],
                "html_url": issue["html_url"],
                "state": issue["state"]
            }, indent=2))

        elif args.command == "update-issue":
            updates = {}
            if args.title:
                updates["title"] = args.title
            if args.body:
                updates["body"] = args.body
            if args.state:
                updates["state"] = args.state
            if args.labels:
                updates["labels"] = [l.strip() for l in args.labels.split(",")]
            if args.assignees:
                updates["assignees"] = [a.strip() for a in args.assignees.split(",")]

            issue = client.update_issue(args.repo, args.number, **updates)
            print(json.dumps({
                "number": issue["number"],
                "title": issue["title"],
                "state": issue["state"],
                "html_url": issue["html_url"]
            }, indent=2))

        elif args.command == "list-prs":
            prs = client.list_pull_requests(args.repo, state=args.state)
            print(json.dumps([{
                "number": pr["number"],
                "title": pr["title"],
                "state": pr["state"],
                "user": pr["user"]["login"],
                "created_at": pr["created_at"],
                "updated_at": pr["updated_at"],
                "html_url": pr["html_url"]
            } for pr in prs], indent=2))

        elif args.command == "get-pr":
            pr = client.get_pull_request(args.repo, args.number)
            print(json.dumps({
                "number": pr["number"],
                "title": pr["title"],
                "body": pr.get("body"),
                "state": pr["state"],
                "user": pr["user"]["login"],
                "created_at": pr["created_at"],
                "updated_at": pr["updated_at"],
                "merged_at": pr.get("merged_at"),
                "mergeable": pr.get("mergeable"),
                "comments": pr.get("comments", 0),
                "commits": pr.get("commits", 0),
                "additions": pr.get("additions", 0),
                "deletions": pr.get("deletions", 0),
                "html_url": pr["html_url"]
            }, indent=2))

        elif args.command == "search-issues":
            results = client.search_issues(args.query)
            print(json.dumps([{
                "number": r["number"],
                "title": r["title"],
                "state": r["state"],
                "repository": r["repository_url"].split("/")[-2:],
                "user": r["user"]["login"],
                "created_at": r["created_at"],
                "html_url": r["html_url"]
            } for r in results], indent=2))

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
