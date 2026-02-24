#!/usr/bin/env python3
"""
Gmail API Test Script
Tests service account authentication and lists recent emails
"""

import os
import sys
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from read_policy import resolve_read_mailbox

# Configuration from environment variables
SERVICE_ACCOUNT_FILE = os.environ.get(
    'SERVICE_ACCOUNT_FILE',
    '/root/.openclaw/credentials/service-account.json'
)
DELEGATED_EMAIL = os.environ.get('EMAIL_ACCOUNT', 'jamie@bramforth.ai')
READ_POLICY_FILE = os.environ.get('GMAIL_READ_POLICY_FILE', '').strip()
ALLOWED_READ_MAILBOXES = os.environ.get('GMAIL_ALLOWED_READ_MAILBOXES', '').strip()
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly'
]


def resolve_mailbox_target(requested_mailbox=None):
    return resolve_read_mailbox(
        default_mailbox=DELEGATED_EMAIL,
        requested_mailbox=requested_mailbox,
        policy_path=READ_POLICY_FILE or None,
        allowed_csv=ALLOWED_READ_MAILBOXES or None,
    )


def get_gmail_service(delegated_email=None):
    """Create and return Gmail API service with domain-wide delegation."""
    target_mailbox = resolve_mailbox_target(delegated_email)

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    delegated_credentials = credentials.with_subject(target_mailbox)
    service = build('gmail', 'v1', credentials=delegated_credentials)
    return service


def get_recent_emails(service, max_results=5):
    """
    Get recent emails from inbox (clean output for agent use).

    Returns list of dicts with: from, subject, date, id
    """
    try:
        results = service.users().messages().list(
            userId='me',
            maxResults=max_results,
            labelIds=['INBOX']
        ).execute()

        messages = results.get('messages', [])

        emails = []
        for msg in messages:
            message = service.users().messages().get(
                userId='me',
                id=msg['id'],
                format='metadata',
                metadataHeaders=['From', 'Subject', 'Date']
            ).execute()

            headers = {h['name']: h['value'] for h in message['payload']['headers']}

            emails.append({
                'from': headers.get('From', 'N/A'),
                'subject': headers.get('Subject', 'N/A'),
                'date': headers.get('Date', 'N/A'),
                'id': msg['id']
            })

        return emails

    except HttpError as error:
        raise Exception(f'Gmail API error: {error}')


def list_recent_emails(service, max_results=5):
    """List recent emails from the inbox (verbose test output)."""
    try:
        emails = get_recent_emails(service, max_results)

        if not emails:
            print('No messages found.')
            return

        print(f'\n✓ Found {len(emails)} recent emails:\n')

        for email in emails:
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Date: {email['date']}")
            print("-" * 80)

    except Exception as error:
        print(f'✗ An error occurred: {error}')
        raise


def main():
    print("=" * 80)
    print("Gmail API Service Account Test")
    print("=" * 80)
    print(f"\nService Account: {SERVICE_ACCOUNT_FILE}")
    print(f"Default Delegated Email: {DELEGATED_EMAIL}")
    print(f"Scopes: {', '.join(SCOPES)}\n")

    try:
        target_mailbox = resolve_mailbox_target()
        print(f"Target mailbox: {target_mailbox}")

        print("Authenticating...")
        service = get_gmail_service()
        print("✓ Authentication successful!\n")

        print("Fetching recent emails...")
        list_recent_emails(service)

        print("\n" + "=" * 80)
        print("✓ Test completed successfully!")
        print("=" * 80)

    except Exception as e:
        print("\n" + "=" * 80)
        print(f"✗ Test failed: {str(e)}")
        print("=" * 80)
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
