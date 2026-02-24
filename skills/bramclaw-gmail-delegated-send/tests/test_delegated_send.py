import base64
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.gmail_delegated_send import (
    AliasPreflightError,
    assert_sendas_alias,
    build_raw_message,
    run_delegated_send,
)


class FakeSendAsListCall:
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        return self._payload


class FakeSendAsResource:
    def __init__(self, payload):
        self._payload = payload

    def list(self, userId):  # noqa: N803
        if userId != "me":
            raise AssertionError("expected userId='me'")
        return FakeSendAsListCall(self._payload)


class FakeSettings:
    def __init__(self, payload):
        self._payload = payload

    def sendAs(self):  # noqa: N802
        return FakeSendAsResource(self._payload)


class FakeUsers:
    def __init__(self, payload):
        self._payload = payload

    def settings(self):
        return FakeSettings(self._payload)


class FakeService:
    def __init__(self, payload):
        self._payload = payload

    def users(self):
        return FakeUsers(self._payload)


class DelegatedSendTests(unittest.TestCase):
    def test_build_raw_message_sets_from_and_sender(self):
        raw = build_raw_message(
            from_display="Boss Person",
            from_email="boss@example.com",
            sender_email="va@example.com",
            to=["client@example.com"],
            subject="Status update",
            text_body="Plain body",
            html_body="<p>HTML body</p>",
        )
        decoded = base64.urlsafe_b64decode(raw.encode("utf-8")).decode("utf-8")

        self.assertIn("From: Boss Person <boss@example.com>", decoded)
        self.assertIn("Sender: va@example.com", decoded)
        self.assertIn("X-Google-Sender-Delegation: va@example.com;", decoded)
        self.assertIn("To: client@example.com", decoded)
        self.assertIn("Subject: Status update", decoded)
        self.assertIn("multipart/alternative", decoded)

    def test_assert_sendas_alias_raises_when_missing_alias(self):
        service = FakeService(
            {
                "sendAs": [
                    {"sendAsEmail": "different@example.com", "verificationStatus": "accepted"},
                ]
            }
        )

        with self.assertRaises(AliasPreflightError):
            assert_sendas_alias(service=service, boss_email="boss@example.com")

    def test_assert_sendas_alias_allows_verified_alias(self):
        service = FakeService(
            {
                "sendAs": [
                    {"sendAsEmail": "boss@example.com", "verificationStatus": "accepted"},
                ]
            }
        )

        alias = assert_sendas_alias(service=service, boss_email="boss@example.com")
        self.assertEqual(alias["sendAsEmail"], "boss@example.com")

    def test_run_delegated_send_uses_boss_email_when_from_display_missing(self):
        service = FakeService(
            {
                "sendAs": [
                    {
                        "sendAsEmail": "boss@example.com",
                        "verificationStatus": "accepted",
                        "displayName": "Boss Person",
                    },
                ]
            }
        )
        policy = {"va_to_boss": {"va@example.com": ["boss@example.com"]}}

        result = run_delegated_send(
            service=service,
            policy=policy,
            va_email="va@example.com",
            boss_email="boss@example.com",
            from_display=None,
            recipients=["client@example.com"],
            subject="Status update",
            text_body="Plain body",
            html_body=None,
            send_mode="dry-run",
            allow_unverified_alias=False,
        )
        self.assertEqual(result.from_display_used, "boss@example.com")


if __name__ == "__main__":
    unittest.main()
