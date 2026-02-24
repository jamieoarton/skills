#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VALIDATOR="${VALIDATOR:-$SKILL_DIR/../scripts/quick_validate_skill.py}"

echo "== Skill Quality Gate =="
echo "Skill dir: $SKILL_DIR"

echo "[1/4] Structural validation"
python3 "$VALIDATOR" "$SKILL_DIR"

echo "[2/4] Reference integrity"
refs="$(cd "$SKILL_DIR" && rg -o '`(references|assets|scripts|tests)/[A-Za-z0-9._/-]+`|\((references|assets|scripts|tests)/[A-Za-z0-9._/-]+\)' SKILL.md references/*.md tests/*.md 2>/dev/null | tr -d '`()' | cut -d: -f2 | sort -u)"
missing=""
if [[ -n "$refs" ]]; then
  while IFS= read -r p; do
    [[ -z "$p" ]] && continue
    if [[ ! -e "$SKILL_DIR/$p" ]]; then
      missing+="$p"$'\n'
    fi
  done <<< "$refs"
fi
if [[ -n "$missing" ]]; then
  echo "Missing referenced files:"
  printf '%s' "$missing"
  exit 2
fi
echo "Reference integrity: PASS"

echo "[3/4] Python syntax checks"
find "$SKILL_DIR/scripts" "$SKILL_DIR/tests" -maxdepth 1 -type f -name '*.py' -print0 | xargs -0 -I{} python3 -m py_compile {}
echo "Syntax checks: PASS"

echo "[4/4] Test runner"
RUN_LIVE="${RUN_LIVE:-0}" "$SKILL_DIR/tests/run-all-tests.sh"

echo "Quality gate: PASS"
