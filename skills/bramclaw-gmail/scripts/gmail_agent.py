#!/usr/bin/env python3
"""Gmail Agent Interface - Clean output for OpenClaw agent use."""

import argparse
import base64
import json
import sys
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

CURRENT_DIR = Path(__file__).resolve().parent
TESTS_DIR = CURRENT_DIR.parent / "tests"
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from gmail_test import get_gmail_service, get_recent_emails
from gmail_test import SERVICE_ACCOUNT_FILE, resolve_mailbox_target


def get_subjects(max_results=5, mailbox=None):
    """Get recent email subjects (clean output)."""
    try:
        service = get_gmail_service(mailbox)
        emails = get_recent_emails(service, max_results)

        for i, email in enumerate(emails, 1):
            print(f"{i}. {email['subject']}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_emails_json(max_results=5, mailbox=None):
    """Get recent emails as JSON."""
    try:
        service = get_gmail_service(mailbox)
        emails = get_recent_emails(service, max_results)
        print(json.dumps(emails, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def _decode_b64(data: str) -> str:
    if not data:
        return ""
    pad = "=" * ((4 - len(data) % 4) % 4)
    raw = base64.urlsafe_b64decode((data + pad).encode("utf-8"))
    return raw.decode("utf-8", errors="replace")


def _collect_parts(payload: dict, out_plain: list[str], out_html: list[str]) -> None:
    mime = (payload.get("mimeType") or "").lower()
    body_data = (payload.get("body") or {}).get("data") or ""

    if body_data:
        decoded = _decode_b64(body_data)
        if mime == "text/plain":
            out_plain.append(decoded)
        elif mime == "text/html":
            out_html.append(decoded)

    for part in payload.get("parts") or []:
        _collect_parts(part, out_plain, out_html)


def get_message_json(message_id: str, mailbox=None):
    """Get one message with headers + snippet + decoded body text/html."""
    try:
        service = get_gmail_service(mailbox)
        message = service.users().messages().get(
            userId="me",
            id=message_id,
            format="full",
        ).execute()

        payload = message.get("payload") or {}
        headers = {
            h.get("name"): h.get("value")
            for h in payload.get("headers") or []
            if h.get("name")
        }

        plain_parts: list[str] = []
        html_parts: list[str] = []
        _collect_parts(payload, plain_parts, html_parts)

        marked_read, mark_read_error = _mark_read_internal(message_id, mailbox)
        result = {
            "id": message.get("id"),
            "threadId": message.get("threadId"),
            "from": headers.get("From", "N/A"),
            "to": headers.get("To", "N/A"),
            "cc": headers.get("Cc", ""),
            "subject": headers.get("Subject", "N/A"),
            "date": headers.get("Date", "N/A"),
            "snippet": message.get("snippet", ""),
            "body_text": "\n".join([p for p in plain_parts if p]).strip(),
            "body_html": "\n".join([p for p in html_parts if p]).strip(),
            "marked_read": marked_read,
            "mark_read_error": mark_read_error,
        }
        print(json.dumps(result, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def get_modify_service(mailbox=None):
    """Create Gmail service with modify scope for label/archive updates."""
    target_mailbox = resolve_mailbox_target(mailbox)
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/gmail.modify"],
    )
    delegated_credentials = credentials.with_subject(target_mailbox)
    return build("gmail", "v1", credentials=delegated_credentials)


def _mark_read_internal(message_id: str, mailbox=None):
    """Best-effort helper for removing UNREAD label from a message."""
    try:
        service = get_modify_service(mailbox)
        service.users().messages().modify(
            userId="me",
            id=message_id,
            body={"removeLabelIds": ["UNREAD"]},
        ).execute()
        return True, None
    except Exception as exc:
        return False, str(exc)


def mark_message_read(message_id: str, mailbox=None):
    """Mark a specific message as read (remove UNREAD label)."""
    try:
        service = get_modify_service(mailbox)
        response = service.users().messages().get(
            userId="me",
            id=message_id,
            format="metadata",
        ).execute()
        marked_read, mark_read_error = _mark_read_internal(message_id, mailbox)
        result = {
            "message_id": message_id,
            "thread_id": response.get("threadId"),
            "marked_read": marked_read,
            "mark_read_error": mark_read_error,
        }
        print(json.dumps(result, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def _ensure_label(service, label_name: str) -> str:
    labels = service.users().labels().list(userId="me").execute().get("labels", [])
    for label in labels:
        if (label.get("name") or "").strip().lower() == label_name.strip().lower():
            return label["id"]
    created = service.users().labels().create(
        userId="me",
        body={
            "name": label_name,
            "labelListVisibility": "labelShow",
            "messageListVisibility": "show",
        },
    ).execute()
    return created["id"]


def post_reply_cleanup(message_id: str, mailbox=None, label_name: str = "Replied by Pepper"):
    """
    Tag a source message and archive it after a successful reply.
    - Adds label if missing (creating it if needed)
    - Removes INBOX and UNREAD labels
    """
    try:
        service = get_modify_service(mailbox)
        label_id = _ensure_label(service, label_name)
        before = service.users().messages().get(
            userId="me",
            id=message_id,
            format="metadata",
        ).execute()
        before_labels = set(before.get("labelIds", []))
        add_ids = [] if label_id in before_labels else [label_id]
        remove_ids = [lid for lid in ("INBOX", "UNREAD") if lid in before_labels]

        service.users().messages().modify(
            userId="me",
            id=message_id,
            body={"addLabelIds": add_ids, "removeLabelIds": remove_ids},
        ).execute()
        result = {
            "message_id": message_id,
            "label_name": label_name,
            "label_added": bool(add_ids),
            "archived": "INBOX" in before_labels,
            "marked_read": "UNREAD" in before_labels,
        }
        print(json.dumps(result, indent=2))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Read Gmail inbox metadata")
    parser.add_argument(
        "command",
        nargs="?",
        default="subjects",
        choices=["subjects", "json", "message", "mark-read", "post-reply-cleanup"],
    )
    parser.add_argument("arg", nargs="?", default="5")
    parser.add_argument(
        "--label-name",
        default="Replied by Pepper",
        help="Label used by post-reply-cleanup command",
    )
    parser.add_argument("--mailbox", help="Target mailbox to impersonate for this call")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.command == "message":
        return get_message_json(args.arg, args.mailbox)
    if args.command == "mark-read":
        return mark_message_read(args.arg, args.mailbox)
    if args.command == "post-reply-cleanup":
        return post_reply_cleanup(args.arg, args.mailbox, args.label_name)

    try:
        max_results = int(args.arg)
    except ValueError:
        print("Error: max_results must be an integer for subjects/json commands", file=sys.stderr)
        return 1

    if args.command == "subjects":
        return get_subjects(max_results, args.mailbox)
    return get_emails_json(max_results, args.mailbox)


if __name__ == '__main__':
    sys.exit(main())
