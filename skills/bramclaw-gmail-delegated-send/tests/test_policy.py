import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.policy import (
    PolicyError,
    load_policy,
    validate_send_request,
)


class PolicyTests(unittest.TestCase):
    def test_load_policy_reads_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "policy.json"
            path.write_text(
                json.dumps(
                    {
                        "va_to_boss": {
                            "va@example.com": ["boss@example.com"],
                        },
                        "recipient_rules": {
                            "mode": "allow_domains",
                            "domains": ["example.com"],
                        },
                    }
                ),
                encoding="utf-8",
            )
            policy = load_policy(path)
            self.assertEqual(policy["va_to_boss"]["va@example.com"], ["boss@example.com"])

    def test_validate_send_request_allows_valid_mapping_and_recipient(self):
        policy = {
            "va_to_boss": {
                "va@example.com": ["boss@example.com"],
            },
            "recipient_rules": {
                "mode": "allow_domains",
                "domains": ["example.com"],
            },
        }

        result = validate_send_request(
            policy=policy,
            va_email="va@example.com",
            boss_email="boss@example.com",
            recipients=["client@example.com"],
        )
        self.assertTrue(result.allowed)
        self.assertEqual(result.decision, "allow")

    def test_validate_send_request_rejects_unauthorized_delegate_pair(self):
        policy = {
            "va_to_boss": {
                "va@example.com": ["boss@example.com"],
            }
        }

        result = validate_send_request(
            policy=policy,
            va_email="va@example.com",
            boss_email="otherboss@example.com",
            recipients=["client@example.com"],
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.decision, "deny")
        self.assertIn("not authorized", result.reason)

    def test_validate_send_request_rejects_blocked_recipient_domain(self):
        policy = {
            "va_to_boss": {
                "va@example.com": ["boss@example.com"],
            },
            "recipient_rules": {
                "mode": "allow_domains",
                "domains": ["example.com"],
            },
        }

        result = validate_send_request(
            policy=policy,
            va_email="va@example.com",
            boss_email="boss@example.com",
            recipients=["client@evil.com"],
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.decision, "deny")
        self.assertIn("not allowed", result.reason)

    def test_validate_send_request_requires_non_empty_recipients(self):
        policy = {
            "va_to_boss": {
                "va@example.com": ["boss@example.com"],
            }
        }

        with self.assertRaises(PolicyError):
            validate_send_request(
                policy=policy,
                va_email="va@example.com",
                boss_email="boss@example.com",
                recipients=[],
            )

    def test_external_on_behalf_send_requires_approval_token(self):
        policy = {
            "va_to_boss": {
                "va@example.com": ["boss@example.com"],
            },
            "approval_rules": {
                "require_external_on_behalf_approval": True,
                "internal_domains": ["example.com"],
                "required_token": "CONFIRM_SEND_ON_BEHALF",
            },
        }

        denied = validate_send_request(
            policy=policy,
            va_email="va@example.com",
            boss_email="boss@example.com",
            recipients=["person@external.com"],
            approval_token=None,
        )
        self.assertFalse(denied.allowed)
        self.assertIn("requires explicit approval token", denied.reason)

        allowed = validate_send_request(
            policy=policy,
            va_email="va@example.com",
            boss_email="boss@example.com",
            recipients=["person@external.com"],
            approval_token="CONFIRM_SEND_ON_BEHALF",
        )
        self.assertTrue(allowed.allowed)


if __name__ == "__main__":
    unittest.main()
