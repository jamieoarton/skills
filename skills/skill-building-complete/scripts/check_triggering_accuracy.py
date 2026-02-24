#!/usr/bin/env python3
"""Measure skill triggering accuracy from labeled test results."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

TRUE_VALUES = {"1", "true", "yes", "y", "trigger", "should_trigger"}
FALSE_VALUES = {"0", "false", "no", "n", "skip", "should_not_trigger"}


def parse_bool(value: str) -> bool:
    v = value.strip().lower()
    if v in TRUE_VALUES:
        return True
    if v in FALSE_VALUES:
        return False
    raise ValueError(f"Unsupported boolean value: {value!r}")


def sniff_dialect(path: Path) -> csv.Dialect:
    sample = path.read_text(encoding="utf-8")[:4096]
    try:
        return csv.Sniffer().sniff(sample, delimiters=",|\t;")
    except csv.Error:
        return csv.excel


def run(path: Path, expected_col: str, actual_col: str, fail_under: float, as_json: bool) -> int:
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {path}")

    tp = tn = fp = fn = 0
    rows = 0

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, dialect=sniff_dialect(path))
        if not reader.fieldnames:
            raise ValueError("Input file has no header row")
        required = {expected_col, actual_col}
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing))}. "
                f"Found: {', '.join(reader.fieldnames)}"
            )

        for row in reader:
            rows += 1
            expected = parse_bool(row[expected_col])
            actual = parse_bool(row[actual_col])
            if expected and actual:
                tp += 1
            elif (not expected) and (not actual):
                tn += 1
            elif (not expected) and actual:
                fp += 1
            else:
                fn += 1

    if rows == 0:
        raise ValueError("Input file has zero data rows")

    accuracy = ((tp + tn) / rows) * 100.0
    trigger_recall = (tp / (tp + fn) * 100.0) if (tp + fn) else 0.0
    skip_recall = (tn / (tn + fp) * 100.0) if (tn + fp) else 0.0

    result = {
        "rows": rows,
        "accuracy_pct": round(accuracy, 2),
        "trigger_recall_pct": round(trigger_recall, 2),
        "skip_recall_pct": round(skip_recall, 2),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "pass": accuracy >= fail_under,
        "target_pct": fail_under,
    }

    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Rows: {rows}")
        print(f"Accuracy: {accuracy:.2f}% (target: {fail_under:.2f}%)")
        print(f"Should-trigger hit rate: {trigger_recall:.2f}%")
        print(f"Should-not-trigger hit rate: {skip_recall:.2f}%")
        print(f"Confusion counts: TP={tp}, TN={tn}, FP={fp}, FN={fn}")
        print("Status: PASS" if result["pass"] else "Status: FAIL")

    return 0 if result["pass"] else 2


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Calculate skill triggering accuracy from a CSV/TSV file with expected and actual columns."
        )
    )
    parser.add_argument("results", type=Path, help="Path to results CSV/TSV")
    parser.add_argument(
        "--expected-col",
        default="expected",
        help="Column containing expected labels (default: expected)",
    )
    parser.add_argument(
        "--actual-col",
        default="actual",
        help="Column containing actual trigger labels (default: actual)",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=90.0,
        help="Minimum accuracy percentage required to pass (default: 90)",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON output")

    args = parser.parse_args()
    try:
        return run(args.results, args.expected_col, args.actual_col, args.fail_under, args.json)
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
