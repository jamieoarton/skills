#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running bramclaw-gmail-delegated-send tests..."
echo "[1/2] Unit tests"
python3 -m unittest discover -s tests -p 'test_*.py' -v

if [[ "${RUN_LIVE:-0}" == "1" ]]; then
  echo "[2/2] Live alias/send check"
  python3 scripts/gmail_delegated_send.py \
    --to "${GMAIL_TEST_TO:-$GMAIL_BOSS_EMAIL}" \
    --subject "[live-check] delegated-send validation" \
    --text-body "Delegated send live-check" \
    --from-display "Delegated Send Check" >/tmp/bramclaw-gmail-delegated-send-live.out
else
  echo "[2/2] Live alias/send check skipped (set RUN_LIVE=1 to enable)"
fi

echo "All tests passed"
