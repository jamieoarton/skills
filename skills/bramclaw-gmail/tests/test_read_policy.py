import tempfile
import unittest
from pathlib import Path

import json
import sys

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from read_policy import resolve_read_mailbox  # noqa: E402


class ReadPolicyTests(unittest.TestCase):
    def test_default_mailbox_used_when_no_override(self):
        target = resolve_read_mailbox(default_mailbox="boss@example.com")
        self.assertEqual(target, "boss@example.com")

    def test_explicit_override_allowed_by_csv_allowlist(self):
        target = resolve_read_mailbox(
            default_mailbox="boss@example.com",
            requested_mailbox="va@example.com",
            allowed_csv="boss@example.com,va@example.com",
        )
        self.assertEqual(target, "va@example.com")

    def test_override_denied_when_not_in_csv_allowlist(self):
        with self.assertRaises(ValueError):
            resolve_read_mailbox(
                default_mailbox="boss@example.com",
                requested_mailbox="other@example.com",
                allowed_csv="boss@example.com,va@example.com",
            )

    def test_policy_file_allows_mailbox(self):
        with tempfile.TemporaryDirectory() as tmp:
            policy_file = Path(tmp) / "read-policy.json"
            policy_file.write_text(
                json.dumps(
                    {
                        "allowed_mailboxes": ["boss@example.com", "senior2@example.com"],
                        "default_mailbox": "boss@example.com",
                    }
                ),
                encoding="utf-8",
            )
            target = resolve_read_mailbox(
                default_mailbox="boss@example.com",
                requested_mailbox="senior2@example.com",
                policy_path=policy_file,
            )
            self.assertEqual(target, "senior2@example.com")

    def test_policy_file_denies_mailbox_not_allowlisted(self):
        with tempfile.TemporaryDirectory() as tmp:
            policy_file = Path(tmp) / "read-policy.json"
            policy_file.write_text(
                json.dumps(
                    {
                        "allowed_mailboxes": ["boss@example.com"],
                        "default_mailbox": "boss@example.com",
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                resolve_read_mailbox(
                    default_mailbox="boss@example.com",
                    requested_mailbox="other@example.com",
                    policy_path=policy_file,
                )


if __name__ == "__main__":
    unittest.main()
