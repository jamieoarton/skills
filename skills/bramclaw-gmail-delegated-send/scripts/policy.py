"""Policy checks for delegated Gmail sending."""

from __future__ import annotations

import json
from dataclasses import dataclass
from email.utils import parseaddr
from pathlib import Path
from typing import Any


class PolicyError(ValueError):
    """Raised when policy input is malformed."""


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    decision: str
    reason: str


def load_policy(path: str | Path) -> dict[str, Any]:
    policy_path = Path(path)
    if not policy_path.exists():
        raise PolicyError(f"policy file not found: {policy_path}")
    try:
        return json.loads(policy_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise PolicyError(f"policy file is not valid JSON: {policy_path}") from exc


def _normalize_email(value: str) -> str:
    _name, addr = parseaddr(value)
    return addr.strip().lower()


def _recipient_allowed(recipient: str, rules: dict[str, Any] | None) -> bool:
    if not rules:
        return True

    mode = rules.get("mode", "allow_all")
    normalized = _normalize_email(recipient)
    if not normalized:
        return False

    if mode == "allow_all":
        return True

    domain = normalized.split("@")[-1]
    domains = {d.lower() for d in rules.get("domains", []) if isinstance(d, str)}
    addresses = {a.lower() for a in rules.get("addresses", []) if isinstance(a, str)}

    if mode == "allow_domains":
        return domain in domains
    if mode == "deny_domains":
        return domain not in domains
    if mode == "allow_addresses":
        return normalized in addresses
    if mode == "deny_addresses":
        return normalized not in addresses

    raise PolicyError(f"unsupported recipient_rules mode: {mode}")


def _is_external_recipient(recipient: str, internal_domains: set[str]) -> bool:
    domain = recipient.split("@")[-1].lower()
    return domain not in internal_domains


def validate_send_request(
    *,
    policy: dict[str, Any],
    va_email: str,
    boss_email: str,
    recipients: list[str],
    approval_token: str | None = None,
) -> PolicyDecision:
    va = _normalize_email(va_email)
    boss = _normalize_email(boss_email)
    normalized_recipients = [_normalize_email(r) for r in recipients if _normalize_email(r)]

    if not va or not boss:
        raise PolicyError("va_email and boss_email must be valid emails")
    if not normalized_recipients:
        raise PolicyError("at least one valid recipient is required")

    va_to_boss = policy.get("va_to_boss", {})
    allowed_bosses = {
        _normalize_email(candidate)
        for candidate in va_to_boss.get(va, [])
        if isinstance(candidate, str)
    }

    if boss not in allowed_bosses:
        return PolicyDecision(
            allowed=False,
            decision="deny",
            reason=f"va '{va}' not authorized to send on behalf of '{boss}'",
        )

    rules = policy.get("recipient_rules")
    for recipient in normalized_recipients:
        if not _recipient_allowed(recipient, rules):
            return PolicyDecision(
                allowed=False,
                decision="deny",
                reason=f"recipient '{recipient}' is not allowed by recipient_rules",
            )

    approval_rules = policy.get("approval_rules", {})
    require_external_approval = bool(
        approval_rules.get("require_external_on_behalf_approval", False)
    )
    internal_domains = {
        d.lower()
        for d in approval_rules.get("internal_domains", ["bramforth.ai"])
        if isinstance(d, str) and d.strip()
    }
    required_token = str(
        approval_rules.get("required_token", "CONFIRM_SEND_ON_BEHALF")
    ).strip()

    has_external = any(
        _is_external_recipient(recipient, internal_domains)
        for recipient in normalized_recipients
    )
    if require_external_approval and has_external:
        provided = (approval_token or "").strip()
        if not provided or provided != required_token:
            return PolicyDecision(
                allowed=False,
                decision="deny",
                reason="external on-behalf send requires explicit approval token",
            )

    return PolicyDecision(allowed=True, decision="allow", reason="policy checks passed")
