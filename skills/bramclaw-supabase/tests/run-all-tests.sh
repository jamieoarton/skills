#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running bramclaw-supabase tests..."
echo "[1/2] Syntax checks"
python3 -m py_compile scripts/supabase_agent.py scripts/supabase_client.py

if [[ "${RUN_LIVE:-0}" == "1" ]]; then
  echo "[2/2] Live Supabase checks"
  python3 scripts/supabase_agent.py whoami
  python3 scripts/supabase_agent.py projects
else
  echo "[2/2] Live Supabase checks skipped (set RUN_LIVE=1 to enable)"
fi

echo "All tests passed"
