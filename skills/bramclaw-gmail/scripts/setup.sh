#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "[bramclaw-gmail] Installing dependencies"
"$PYTHON_BIN" -m pip install -r "$SKILL_DIR/requirements.txt"

if [[ "${RUN_LIVE:-0}" == "1" ]]; then
  missing=()
  for v in SERVICE_ACCOUNT_FILE EMAIL_ACCOUNT; do
    [[ -n "${!v:-}" ]] || missing+=("$v")
  done
  if [[ ${#missing[@]} -gt 0 ]]; then
    echo "[bramclaw-gmail] Missing env vars for live checks: ${missing[*]}" >&2
    exit 2
  fi
fi

echo "[bramclaw-gmail] Setup complete"
