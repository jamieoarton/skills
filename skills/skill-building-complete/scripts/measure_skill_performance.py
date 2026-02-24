#!/usr/bin/env python3
"""Compare baseline vs with-skill workflow performance."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from pathlib import Path


def _to_float(value: str) -> float:
    return float(value.strip())


def _avg(values: list[float]) -> float:
    return statistics.mean(values) if values else 0.0


def load(path: Path) -> dict[str, dict[str, list[float]]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    groups = {
        "baseline": {"tokens": [], "tool_calls": [], "api_failures": [], "duration_seconds": []},
        "with_skill": {"tokens": [], "tool_calls": [], "api_failures": [], "duration_seconds": []},
    }

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        needed = {"run_type", "tokens", "tool_calls", "api_failures", "duration_seconds"}
        if not reader.fieldnames:
            raise ValueError("Input file has no header")
        missing = needed - set(reader.fieldnames)
        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing))}. "
                f"Found: {', '.join(reader.fieldnames)}"
            )

        for row in reader:
            run_type = row["run_type"].strip().lower()
            if run_type not in groups:
                raise ValueError(f"Invalid run_type: {run_type!r}. Use baseline or with_skill.")
            groups[run_type]["tokens"].append(_to_float(row["tokens"]))
            groups[run_type]["tool_calls"].append(_to_float(row["tool_calls"]))
            groups[run_type]["api_failures"].append(_to_float(row["api_failures"]))
            groups[run_type]["duration_seconds"].append(_to_float(row["duration_seconds"]))

    if not groups["baseline"]["tokens"] or not groups["with_skill"]["tokens"]:
        raise ValueError("Need at least one baseline row and one with_skill row")

    return groups


def summarize(groups: dict[str, dict[str, list[float]]]) -> dict[str, object]:
    b = {k: _avg(v) for k, v in groups["baseline"].items()}
    w = {k: _avg(v) for k, v in groups["with_skill"].items()}

    def reduction(before: float, after: float) -> float:
        if before == 0:
            return 0.0
        return ((before - after) / before) * 100.0

    out = {
        "baseline_avg": b,
        "with_skill_avg": w,
        "token_reduction_pct": reduction(b["tokens"], w["tokens"]),
        "tool_call_reduction_pct": reduction(b["tool_calls"], w["tool_calls"]),
        "duration_reduction_pct": reduction(b["duration_seconds"], w["duration_seconds"]),
        "api_failure_reduction_pct": reduction(b["api_failures"], w["api_failures"]),
    }
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Measure baseline vs with-skill performance from a CSV file."
    )
    parser.add_argument("results", type=Path, help="Path to CSV results")
    parser.add_argument("--min-token-reduction", type=float, default=50.0)
    parser.add_argument("--max-api-failures-with-skill", type=float, default=0.0)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    try:
        groups = load(args.results)
        report = summarize(groups)

        with_skill_failures = report["with_skill_avg"]["api_failures"]
        token_reduction = report["token_reduction_pct"]
        passed = (
            token_reduction >= args.min_token_reduction
            and with_skill_failures <= args.max_api_failures_with_skill
        )

        report["targets"] = {
            "min_token_reduction_pct": args.min_token_reduction,
            "max_api_failures_with_skill": args.max_api_failures_with_skill,
        }
        report["pass"] = passed

        if args.json:
            print(json.dumps(report, indent=2))
        else:
            b = report["baseline_avg"]
            w = report["with_skill_avg"]
            print("Averages")
            print(
                f"- Baseline: tokens={b['tokens']:.1f}, tools={b['tool_calls']:.1f}, "
                f"api_failures={b['api_failures']:.2f}, duration_s={b['duration_seconds']:.1f}"
            )
            print(
                f"- With skill: tokens={w['tokens']:.1f}, tools={w['tool_calls']:.1f}, "
                f"api_failures={w['api_failures']:.2f}, duration_s={w['duration_seconds']:.1f}"
            )
            print("Deltas")
            print(f"- Token reduction: {report['token_reduction_pct']:.2f}%")
            print(f"- Tool-call reduction: {report['tool_call_reduction_pct']:.2f}%")
            print(f"- Duration reduction: {report['duration_reduction_pct']:.2f}%")
            print(f"- API-failure reduction: {report['api_failure_reduction_pct']:.2f}%")
            print("Status: PASS" if passed else "Status: FAIL")

        return 0 if passed else 2
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
