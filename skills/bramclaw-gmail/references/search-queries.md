# Gmail Search Queries Cookbook

## Basic Syntax

Gmail uses a powerful query language for searching. All queries work with the API's `q` parameter.

## Common Queries

### Time-Based

```
newer_than:7d          # Last 7 days
older_than:30d         # Older than 30 days
after:2026/02/01       # After specific date
before:2026/02/20      # Before specific date
```

### Sender/Recipient

```
from:sender@example.com
to:recipient@example.com
cc:person@example.com
bcc:person@example.com
```

### Content

```
subject:"Meeting Notes"        # Exact phrase in subject
subject:meeting                # Word in subject
"exact phrase anywhere"        # Exact phrase in any field
has:attachment                 # Has attachments
filename:pdf                   # Specific file type
```

### Status

```
is:unread                      # Unread emails
is:read                        # Read emails
is:starred                     # Starred
is:important                   # Marked important
```

### Combinations (AND/OR)

```
from:sender@example.com subject:invoice          # AND (both conditions)
from:alice@example.com OR from:bob@example.com   # OR (either)
subject:meeting -from:spam@example.com           # NOT (exclude)
```

## Complex Examples

### Recent unread invoices with attachments

```python
q = 'subject:invoice is:unread has:attachment newer_than:7d'
```

### Important emails from specific sender in date range

```python
q = 'from:boss@example.com is:important after:2026/02/01 before:2026/02/20'
```

### Exclude automated emails

```python
q = 'newer_than:1d -from:noreply@example.com -from:no-reply@example.com'
```

## Performance Tips

- More specific queries = faster results
- Use `maxResults` parameter to limit (default: 100)
- Time ranges significantly improve performance
- Avoid wildcard searches on large mailboxes

## Reference

Full query syntax: https://support.google.com/mail/answer/7190?hl=en
