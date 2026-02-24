# Gmail API Operations Reference

## Available Operations (Read-Only)

### List Messages

```python
service.users().messages().list(
    userId='me',
    q='search query',
    maxResults=20,
    labelIds=['INBOX'],
    includeSpamTrash=False
).execute()
```

**Returns:**
```python
{
    'messages': [
        {'id': '18d...', 'threadId': '18d...'},
        ...
    ],
    'resultSizeEstimate': 42
}
```

### Get Message

```python
# Full message (headers + body)
service.users().messages().get(
    userId='me',
    id=message_id,
    format='full'
).execute()

# Metadata only (faster)
service.users().messages().get(
    userId='me',
    id=message_id,
    format='metadata',
    metadataHeaders=['From', 'Subject', 'Date']
).execute()

# Minimal (just ID and threadId)
service.users().messages().get(
    userId='me',
    id=message_id,
    format='minimal'
).execute()
```

### Get Thread

```python
service.users().threads().get(
    userId='me',
    id=thread_id,
    format='full'
).execute()
```

### Get Attachment

```python
service.users().messages().attachments().get(
    userId='me',
    messageId=message_id,
    id=attachment_id
).execute()
```

**Returns:** Base64-encoded attachment data

### List Labels

```python
service.users().labels().list(userId='me').execute()
```

## Response Formats

### Message Object (Full)

```python
{
    'id': '18d...',
    'threadId': '18d...',
    'labelIds': ['INBOX', 'UNREAD'],
    'snippet': 'Preview text...',
    'payload': {
        'headers': [
            {'name': 'From', 'value': 'sender@example.com'},
            {'name': 'Subject', 'value': 'Email subject'},
            {'name': 'Date', 'value': 'Fri, 21 Feb 2026 10:00:00 +0000'}
        ],
        'body': {
            'size': 1234,
            'data': 'base64-encoded-content'
        },
        'parts': [...]  # For multipart messages
    },
    'sizeEstimate': 12345,
    'historyId': '123456',
    'internalDate': '1708509600000'
}
```

### Metadata Format

More efficient - only headers you request:

```python
{
    'id': '18d...',
    'threadId': '18d...',
    'payload': {
        'headers': [
            {'name': 'From', 'value': 'sender@example.com'},
            {'name': 'Subject', 'value': 'Email subject'},
            {'name': 'Date', 'value': 'Fri, 21 Feb 2026 10:00:00 +0000'}
        ]
    }
}
```

## Write Operations (NOT IMPLEMENTED)

These are intentionally not implemented for security:

- `messages().send()` - Send email
- `messages().modify()` - Add/remove labels
- `messages().trash()` - Move to trash
- `messages().delete()` - Permanent delete
- `drafts().create()` - Create draft

Even though the skill has `gmail.readonly` scope (which allows some writes), we don't expose write operations.

## Rate Limits

Gmail API quotas (per project):
- 1 billion quota units per day
- 250 quota units per user per second

Quota costs:
- `messages().list()` - 5 units
- `messages().get()` (full) - 5 units
- `messages().get()` (metadata) - 2 units
- `messages().get()` (minimal) - 1 unit

**Best practices:**
- Use metadata format when you don't need body
- Use minimal format for ID-only operations
- Batch requests when possible
- Cache results when appropriate

## Dependencies

```python
pip install google-api-python-client google-auth
```

**Versions:**
- google-api-python-client >= 2.0
- google-auth >= 2.0

## Reference

- Gmail API: https://developers.google.com/gmail/api
- Python Client: https://github.com/googleapis/google-api-python-client
- Auth Guide: https://developers.google.com/gmail/api/auth/about-auth
