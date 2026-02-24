"""Mailbox targeting policy helpers for read-only Gmail skill."""

from __future__ import annotations

import json
from email.utils import parseaddr
from pathlib import Path


def normalize_email(value: str) -> str:
    _name, addr = parseaddr(value or "")
    return addr.strip().lower()


def _load_policy(path: str | Path) -> dict:
    file_path = Path(path)
    if not file_path.exists():
        raise ValueError(f"read policy file not found: {file_path}")
    try:
        return json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"read policy file is invalid JSON: {file_path}") from exc


def _parse_csv_emails(value: str | None) -> set[str]:
    if not value:
        return set()
    parsed: set[str] = set()
    for raw in value.split(","):
        email = normalize_email(raw)
        if email:
            parsed.add(email)
    return parsed


def resolve_read_mailbox(
    *,
    default_mailbox: str,
    requested_mailbox: str | None = None,
    policy_path: str | Path | None = None,
    allowed_csv: str | None = None,
) -> str:
    default_target = normalize_email(default_mailbox)
    requested_target = normalize_email(requested_mailbox or "")
    target = requested_target or default_target

    if not default_target:
        raise ValueError("default mailbox is required")
    if not target:
        raise ValueError("requested mailbox is invalid")

    allowed: set[str] = set()

    if policy_path:
        policy = _load_policy(policy_path)
        allowed.update(
            normalize_email(candidate)
            for candidate in policy.get("allowed_mailboxes", [])
            if isinstance(candidate, str)
        )

        policy_default = normalize_email(policy.get("default_mailbox", ""))
        if not requested_target and policy_default:
            target = policy_default

    allowed.update(_parse_csv_emails(allowed_csv))

    if allowed and target not in allowed:
        raise ValueError(f"mailbox '{target}' is not allowlisted for read access")

    return target
