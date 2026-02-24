"""Delegated Gmail outbound send helper with preflight and audit hooks."""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import time
import uuid
from dataclasses import asdict, dataclass
from email import policy as email_policy
from email.parser import BytesParser
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import formataddr, parseaddr
from pathlib import Path
from typing import Any

try:
    from .policy import PolicyDecision, load_policy, validate_send_request
except ImportError:  # pragma: no cover - script execution fallback
    from policy import PolicyDecision, load_policy, validate_send_request


class AliasPreflightError(RuntimeError):
    """Raised when sendAs alias checks fail."""


@dataclass(frozen=True)
class SendResult:
    dry_run: bool
    policy: PolicyDecision
    recipients: list[str]
    bcc_recipients: list[str]
    boss_email: str
    va_email: str
    subject: str
    from_display_used: str
    sendas_alias: dict[str, Any]
    message_id: str | None
    thread_id: str | None
    source_message_id: str | None
    in_reply_to: str | None
    references: str | None
    request_id: str


def build_raw_message(
    *,
    from_display: str,
    from_email: str,
    sender_email: str,
    to: list[str],
    bcc: list[str] | None,
    subject: str,
    text_body: str,
    html_body: str | None = None,
    in_reply_to: str | None = None,
    references: str | None = None,
) -> str:
    # Prevent awkward hard-wrapping in plain text bodies.
    msg = EmailMessage(policy=SMTP.clone(max_line_length=998))
    msg["From"] = formataddr((from_display, from_email))
    msg["Sender"] = sender_email
    msg["X-Google-Sender-Delegation"] = f"{sender_email};"
    msg["To"] = ", ".join(to)
    if bcc:
        msg["Bcc"] = ", ".join(bcc)
    msg["Subject"] = subject
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
    if references:
        msg["References"] = references

    if html_body:
        msg.set_content(text_body)
        msg.add_alternative(html_body, subtype="html")
    else:
        # Keep plain text + lightweight HTML so clients render clean paragraphs.
        paragraphs = [html.escape(p).replace("\n", "<br>") for p in text_body.split("\n\n")]
        fallback_html = "".join(f"<p>{p}</p>" for p in paragraphs if p)
        msg.set_content(text_body)
        if fallback_html:
            msg.add_alternative(fallback_html, subtype="html")

    return base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")


def normalize_text_body(text: str) -> str:
    """
    Convert accidental escaped newlines from agent-generated CLI strings into real newlines.
    Example: "Hi\\n\\nThanks" -> "Hi\n\nThanks"
    """
    return (
        text.replace("\\r\\n", "\n")
        .replace("\\n", "\n")
        .replace("\\t", "\t")
    )


def unwrap_hard_wrapped_text(text: str) -> str:
    """
    Collapse accidental hard wraps inside paragraphs while preserving
    deliberate paragraph breaks, signature blocks, and quoted text.
    """
    paragraphs = [p for p in normalize_text_body(text).split("\n\n")]
    normalized: list[str] = []
    for para in paragraphs:
        lines = para.split("\n")
        if len(lines) <= 1:
            normalized.append(para)
            continue
        stripped = [line.strip() for line in lines]
        if any(line.startswith(">") for line in stripped):
            normalized.append("\n".join(lines))
            continue
        if len(lines) == 2 and (stripped[0].endswith(",") or len(stripped[1].split()) <= 4):
            normalized.append("\n".join(lines))
            continue
        normalized.append(" ".join(x for x in stripped if x))
    return "\n\n".join(normalized).strip()


def _header_map(payload: dict[str, Any]) -> dict[str, str]:
    return {
        str(h.get("name", "")).lower(): str(h.get("value", ""))
        for h in (payload.get("headers") or [])
        if h.get("name")
    }


def fetch_source_reply_headers(service: Any, source_message_id: str) -> tuple[str | None, str | None, str | None]:
    """Get thread + RFC5322 reply headers from source message."""
    source = service.users().messages().get(
        userId="me",
        id=source_message_id,
        format="metadata",
        metadataHeaders=["Message-ID", "References"],
    ).execute()
    headers = _header_map(source.get("payload") or {})
    in_reply_to = (headers.get("message-id") or "").strip() or None
    references = (headers.get("references") or "").strip() or None
    if in_reply_to:
        references = f"{references} {in_reply_to}".strip() if references else in_reply_to
    thread_id = (source.get("threadId") or "").strip() or None
    return thread_id, in_reply_to, references


def fetch_source_message(service: Any, source_message_id: str) -> dict[str, Any]:
    return service.users().messages().get(userId="me", id=source_message_id, format="raw").execute()


def _extract_text_from_email_message(msg: Any) -> tuple[str | None, str | None]:
    text_part = None
    html_part = None
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain" and text_part is None:
                text_part = part.get_content().strip()
            elif content_type == "text/html" and html_part is None:
                html_part = part.get_content().strip()
    else:
        ctype = msg.get_content_type()
        payload = msg.get_content().strip()
        if ctype == "text/plain":
            text_part = payload
        elif ctype == "text/html":
            html_part = payload
    return text_part, html_part


def fetch_source_details(
    service: Any,
    source_message_id: str,
) -> dict[str, str | None]:
    source = fetch_source_message(service, source_message_id)
    raw_b64 = source.get("raw", "")
    raw_bytes = base64.urlsafe_b64decode(raw_b64 + "=" * (-len(raw_b64) % 4))
    parsed = BytesParser(policy=email_policy.default).parsebytes(raw_bytes)

    from_raw = parsed.get("From", "")
    sender_name, sender_email = parseaddr(from_raw)
    date_raw = parsed.get("Date", "")
    subject_raw = parsed.get("Subject", "")
    message_id_raw = parsed.get("Message-ID", "")
    refs_raw = parsed.get("References", "")
    text_part, html_part = _extract_text_from_email_message(parsed)

    return {
        "from_name": sender_name or None,
        "from_email": sender_email or None,
        "date": date_raw or None,
        "subject": subject_raw or None,
        "message_id": message_id_raw or None,
        "references": refs_raw or None,
        "text_body": text_part or None,
        "html_body": html_part or None,
    }


def build_default_reply_text(*, source_subject: str | None, signature_name: str) -> str:
    topic = (source_subject or "your message").strip()
    return (
        f"Hi,\n\n"
        f"Thanks for your message regarding \"{topic}\". I have received this and will follow up shortly.\n\n"
        f"Best regards,\n"
        f"{signature_name}"
    )


def append_quoted_context_text(
    *,
    text_body: str,
    source_from: str | None,
    source_date: str | None,
    source_text: str | None,
) -> str:
    src = (source_text or "").strip()
    if not src:
        return text_body
    quote_lines = "\n".join(f"> {line}" if line else ">" for line in src.splitlines())
    header = f"On {source_date or 'earlier'}, {source_from or 'the sender'} wrote:"
    return f"{text_body}\n\n{header}\n{quote_lines}"


def append_quoted_context_html(
    *,
    html_body: str,
    source_from: str | None,
    source_date: str | None,
    source_html: str | None,
    source_text: str | None,
) -> str:
    source_block = (source_html or "").strip()
    if not source_block and source_text:
        source_block = "<br>".join(html.escape(line) for line in source_text.splitlines())
    if not source_block:
        return html_body
    header = html.escape(f"On {source_date or 'earlier'}, {source_from or 'the sender'} wrote:")
    return (
        f"{html_body}"
        f"<hr><p>{header}</p>"
        f"<blockquote style=\"margin:0 0 0 .8ex;border-left:1px solid #ccc;padding-left:1ex\">"
        f"{source_block}</blockquote>"
    )


def try_fetch_source_reply_headers(
    service: Any,
    source_message_id: str,
) -> tuple[str | None, str | None, str | None]:
    """Best-effort source lookup; failures should not block sends."""
    try:
        return fetch_source_reply_headers(service, source_message_id)
    except Exception:
        return None, None, None


def assert_sendas_alias(
    *,
    service: Any,
    boss_email: str,
    allow_unverified_alias: bool = False,
) -> dict[str, Any]:
    payload = service.users().settings().sendAs().list(userId="me").execute()
    entries = payload.get("sendAs", [])

    for entry in entries:
        if entry.get("sendAsEmail", "").lower() != boss_email.lower():
            continue
        status = (entry.get("verificationStatus") or "").lower()
        if allow_unverified_alias or status in {"accepted", "verified"}:
            return entry
        raise AliasPreflightError(
            f"alias found for '{boss_email}' but verificationStatus='{status}'"
        )

    raise AliasPreflightError(f"boss alias '{boss_email}' missing from sendAs list")


def write_audit_log(path: str | Path, event: dict[str, Any]) -> None:
    log_path = Path(path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")


def run_delegated_send(
    *,
    service: Any,
    policy: dict[str, Any],
    va_email: str,
    boss_email: str,
    from_display: str | None,
    recipients: list[str],
    bcc_recipients: list[str] | None,
    subject: str,
    text_body: str,
    html_body: str | None,
    send_mode: str,
    allow_unverified_alias: bool,
    source_lookup_service: Any | None = None,
    source_message_id: str | None = None,
    approval_token: str | None = None,
) -> SendResult:
    request_id = str(uuid.uuid4())
    policy_decision = validate_send_request(
        policy=policy,
        va_email=va_email,
        boss_email=boss_email,
        recipients=recipients,
        approval_token=approval_token,
    )

    if not policy_decision.allowed:
        raise PermissionError(policy_decision.reason)

    alias = assert_sendas_alias(
        service=service,
        boss_email=boss_email,
        allow_unverified_alias=allow_unverified_alias,
    )

    # Do not default to alias displayName, which can render as "Pepper on behalf of Jamie".
    # Default to explicit boss identity so Gmail UI shows "Jamie ... (sent by pepper@...)".
    effective_from_display = (from_display or "").strip() or boss_email
    source_id = (source_message_id or "").strip() or None
    thread_id = None
    in_reply_to = None
    references = None
    if source_id:
        lookup_service = source_lookup_service or service
        thread_id, in_reply_to, references = try_fetch_source_reply_headers(
            lookup_service,
            source_id,
        )

    raw = build_raw_message(
        from_display=effective_from_display,
        from_email=boss_email,
        sender_email=va_email,
        to=recipients,
        bcc=bcc_recipients or None,
        subject=subject,
        text_body=normalize_text_body(text_body),
        html_body=html_body,
        in_reply_to=in_reply_to,
        references=references,
    )

    if send_mode == "live":
        body: dict[str, Any] = {"raw": raw}
        if thread_id:
            body["threadId"] = thread_id
        try:
            response = service.users().messages().send(userId="me", body=body).execute()
        except Exception as exc:
            # Cross-mailbox thread ids can 404; retry once without threadId.
            if thread_id and "404" in str(exc):
                response = service.users().messages().send(userId="me", body={"raw": raw}).execute()
                thread_id = None
            else:
                raise
        message_id = response.get("id")
        dry_run = False
    else:
        message_id = None
        dry_run = True

    return SendResult(
        dry_run=dry_run,
        policy=policy_decision,
        recipients=recipients,
        bcc_recipients=bcc_recipients or [],
        boss_email=boss_email,
        va_email=va_email,
        subject=subject,
        from_display_used=effective_from_display,
        sendas_alias=alias,
        message_id=message_id,
        thread_id=thread_id,
        source_message_id=source_id,
        in_reply_to=in_reply_to,
        references=references,
        request_id=request_id,
    )


def build_service_account_service(service_account_file: str, delegated_user: str) -> Any:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    scopes = [
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.settings.basic",
    ]
    creds = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=scopes,
    ).with_subject(delegated_user)
    return build("gmail", "v1", credentials=creds)


def build_readonly_service(service_account_file: str, delegated_user: str) -> Any:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    creds = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=["https://www.googleapis.com/auth/gmail.readonly"],
    ).with_subject(delegated_user)
    return build("gmail", "v1", credentials=creds)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send Gmail on behalf of principal with guardrails.")
    parser.add_argument("--to", nargs="+", required=False, help="Recipient email(s)")
    parser.add_argument("--subject", required=False)
    parser.add_argument("--text-body", required=False)
    parser.add_argument("--html-body")
    parser.add_argument("--from-display")
    parser.add_argument(
        "--source-message-id",
        help="Original Gmail message id to thread this reply against",
    )
    parser.add_argument(
        "--approval-token",
        help="Required when policy requires explicit external on-behalf send approval",
    )
    parser.add_argument(
        "--send-mode",
        choices=["on_behalf", "as_pa"],
        help="Legacy compatibility flag from older contracts",
    )
    parser.add_argument(
        "--sign-as",
        choices=["principal", "assistant"],
        help="Legacy compatibility flag from older contracts",
    )
    parser.add_argument(
        "--signature-name",
        help="Legacy compatibility flag used to set explicit display/signature name",
    )
    parser.add_argument("--allow-unverified-alias", action="store_true")
    return parser.parse_args()


def _required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"missing required environment variable: {name}")
    return value


def main() -> int:
    args = parse_args()

    service_account_file = _required_env("SERVICE_ACCOUNT_FILE")
    va_email = _required_env("GMAIL_VA_EMAIL")
    boss_email = _required_env("GMAIL_BOSS_EMAIL")
    policy_file = _required_env("GMAIL_DELEGATED_POLICY_FILE")
    send_mode = os.environ.get("GMAIL_SEND_MODE", "dry-run").strip().lower() or "dry-run"
    audit_log_file = os.environ.get(
        "GMAIL_AUDIT_LOG_FILE",
        ".claude/skills/bramclaw-gmail-delegated-send/logs/audit.jsonl",
    )
    boss_display_name = os.environ.get("GMAIL_BOSS_DISPLAY_NAME", "").strip()
    enforce_owner_bcc = os.environ.get("GMAIL_ENFORCE_OWNER_BCC", "true").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }
    owner_bcc_email = os.environ.get("GMAIL_OWNER_BCC_EMAIL", "").strip() or boss_email

    if send_mode not in {"dry-run", "live"}:
        raise RuntimeError("GMAIL_SEND_MODE must be 'dry-run' or 'live'")

    policy = load_policy(policy_file)
    service = build_service_account_service(service_account_file, va_email)
    source_lookup_service = build_readonly_service(service_account_file, boss_email)

    # Compatibility bridge for prior contract format.
    if not args.approval_token and args.send_mode == "on_behalf":
        args.approval_token = "CONFIRM_SEND_ON_BEHALF"
    if not args.from_display and args.signature_name:
        args.from_display = args.signature_name

    source_id = (args.source_message_id or "").strip() or None
    source_details: dict[str, str | None] = {}
    if source_id:
        try:
            source_details = fetch_source_details(source_lookup_service, source_id)
        except Exception:
            source_details = {}

    recipients = args.to or []
    if not recipients and source_details.get("from_email"):
        recipients = [str(source_details["from_email"])]

    subject = (args.subject or "").strip()
    if not subject and source_details.get("subject"):
        subject = f"Re: {source_details['subject']}"

    signature_name = (args.signature_name or args.from_display or boss_display_name or boss_email).strip()
    text_body = (args.text_body or "").strip()
    if not text_body:
        text_body = build_default_reply_text(
            source_subject=source_details.get("subject"),
            signature_name=signature_name,
        )

    html_body = (args.html_body or "").strip() or None
    if source_id:
        text_body = append_quoted_context_text(
            text_body=text_body,
            source_from=source_details.get("from_email") or source_details.get("from_name"),
            source_date=source_details.get("date"),
            source_text=source_details.get("text_body"),
        )
        if html_body:
            html_body = append_quoted_context_html(
                html_body=html_body,
                source_from=source_details.get("from_email") or source_details.get("from_name"),
                source_date=source_details.get("date"),
                source_html=source_details.get("html_body"),
                source_text=source_details.get("text_body"),
            )

    if not recipients or not subject or not text_body:
        raise RuntimeError(
            "missing required send fields: recipients, subject, or text body "
            "(provide flags directly or include --source-message-id for fallback)."
        )

    bcc_recipients: list[str] = []
    if enforce_owner_bcc and owner_bcc_email:
        to_lower = {r.strip().lower() for r in recipients if r.strip()}
        if owner_bcc_email.lower() not in to_lower:
            bcc_recipients.append(owner_bcc_email)

    started = time.time()
    result: SendResult | None = None
    error: str | None = None

    try:
        result = run_delegated_send(
            service=service,
            policy=policy,
            va_email=va_email,
            boss_email=boss_email,
            from_display=(args.from_display or boss_display_name or None),
            recipients=recipients,
            bcc_recipients=bcc_recipients,
            subject=subject,
            text_body=unwrap_hard_wrapped_text(text_body),
            html_body=html_body,
            send_mode=send_mode,
            allow_unverified_alias=args.allow_unverified_alias,
            source_lookup_service=source_lookup_service,
            source_message_id=source_id,
            approval_token=args.approval_token,
        )
        print(json.dumps(asdict(result), indent=2, default=str))
        return 0
    except Exception as exc:  # pragma: no cover - CLI safety path
        error = str(exc)
        print(json.dumps({"error": error}, indent=2))
        return 1
    finally:
        event = {
            "timestamp": int(time.time()),
            "duration_ms": int((time.time() - started) * 1000),
            "send_mode": send_mode,
            "va_email": va_email,
            "boss_email": boss_email,
            "recipients": recipients,
            "bcc_recipients": bcc_recipients,
            "subject": subject,
            "result": asdict(result) if result else None,
            "error": error,
        }
        write_audit_log(audit_log_file, event)


if __name__ == "__main__":
    raise SystemExit(main())
