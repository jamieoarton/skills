#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running bramclaw-clickup tests..."
echo "[1/2] Syntax checks"
python3 -m py_compile scripts/clickup_agent.py scripts/clickup_client.py

if [[ "${RUN_LIVE:-0}" == "1" ]]; then
  echo "[2/2] Live ClickUp checks"
  python3 scripts/clickup_agent.py whoami
  python3 scripts/clickup_agent.py workspaces
else
  echo "[2/2] Live ClickUp checks skipped (set RUN_LIVE=1 to enable)"
fi

echo "All tests passed"
