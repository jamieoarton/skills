#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running bramclaw-obsidian tests..."
echo "[1/2] Syntax checks"
python3 -m py_compile scripts/obsidian_vault.py

if [[ "${RUN_LIVE:-0}" == "1" ]]; then
  echo "[2/2] CLI checks"
  python3 scripts/obsidian_vault.py --help >/dev/null
else
  echo "[2/2] CLI checks skipped (set RUN_LIVE=1 to enable)"
fi

echo "All tests passed"
