#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "[bramclaw-supabase] Installing dependencies"
"$PYTHON_BIN" -m pip install -r "$SKILL_DIR/requirements.txt"

if [[ "${RUN_LIVE:-0}" == "1" && -z "${SUPABASE_ACCESS_TOKEN:-}" ]]; then
  echo "[bramclaw-supabase] Missing env var for live checks: SUPABASE_ACCESS_TOKEN" >&2
  exit 2
fi

echo "[bramclaw-supabase] Setup complete"
