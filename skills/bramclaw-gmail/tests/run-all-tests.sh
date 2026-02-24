#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running bramclaw-gmail tests..."
echo "[1/3] Syntax checks"
python3 -m py_compile scripts/gmail_agent.py tests/gmail_test.py

echo "[2/3] Unit tests"
python3 -m unittest discover -s tests -p 'test_*.py' -v

if [[ "${RUN_LIVE:-0}" == "1" ]]; then
  echo "[3/3] Live Gmail checks"
  python3 tests/gmail_test.py
  python3 scripts/gmail_agent.py subjects 1 >/tmp/bramclaw-gmail-test.out
  grep -Eq '^[0-9]+\. ' /tmp/bramclaw-gmail-test.out
else
  echo "[3/3] Live Gmail checks skipped (set RUN_LIVE=1 to enable)"
fi

echo "All tests passed"
