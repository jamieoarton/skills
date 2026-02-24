#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

VALIDATOR="${VALIDATOR:-/Users/jimeny/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"
TRIGGER_RESULTS="${1:-$SKILL_DIR/assets/trigger-results-sample.csv}"
PERF_RESULTS="${2:-$SKILL_DIR/assets/success-metrics-template.csv}"

echo "== Skill Quality Gate =="
echo "Skill dir: $SKILL_DIR"
echo

echo "[1/5] Structural validation"
python3 "$VALIDATOR" "$SKILL_DIR"
echo

echo "[2/5] Reference integrity check"
missing="$(cd "$SKILL_DIR" && rg -o "(references|assets|scripts)/[A-Za-z0-9._/-]+" SKILL.md references/*.md assets/* | cut -d: -f2 | sort -u | while read -r p; do [ -e "$p" ] || echo "$p"; done)"
if [[ -n "$missing" ]]; then
  echo "Missing referenced files:"
  echo "$missing"
  exit 2
fi
echo "Reference integrity: PASS"
echo

echo "[3/5] Triggering accuracy"
python3 "$SKILL_DIR/scripts/check_triggering_accuracy.py" "$TRIGGER_RESULTS" --fail-under 90
echo

echo "[4/5] Performance comparison"
python3 "$SKILL_DIR/scripts/measure_skill_performance.py" "$PERF_RESULTS"
echo

echo "[5/5] MCP integration preflight"
python3 "$SKILL_DIR/scripts/validate_mcp_integration.py" --required-command python3 --smoke-command 'python3 -c "print(123)"'
echo

echo "Quality gate: PASS"
