#!/usr/bin/env python3
"""Lightweight MCP integration preflight validator."""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict


@dataclass
class CheckResult:
    kind: str
    target: str
    ok: bool
    detail: str


def run_command(command: str, timeout: int) -> CheckResult:
    args = shlex.split(command)
    if not args:
        return CheckResult("smoke_command", command, False, "Empty command")
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        if proc.returncode == 0:
            return CheckResult("smoke_command", command, True, proc.stdout.strip()[:300] or "OK")
        msg = (proc.stderr or proc.stdout or "non-zero exit").strip()[:300]
        return CheckResult("smoke_command", command, False, msg)
    except FileNotFoundError:
        return CheckResult("smoke_command", command, False, f"Executable not found: {args[0]}")
    except subprocess.TimeoutExpired:
        return CheckResult("smoke_command", command, False, f"Timed out after {timeout}s")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate MCP integration prerequisites (required env vars, command availability, "
            "and optional smoke commands)."
        )
    )
    parser.add_argument("--required-env", action="append", default=[], help="Environment variable that must be set")
    parser.add_argument(
        "--required-command",
        action="append",
        default=[],
        help="Executable that must exist on PATH (example: node, npx, uvx)",
    )
    parser.add_argument(
        "--smoke-command",
        action="append",
        default=[],
        help="Command to execute for integration smoke testing",
    )
    parser.add_argument("--timeout", type=int, default=15, help="Timeout in seconds per smoke command")
    parser.add_argument("--json", action="store_true", help="Print machine-readable output")

    args = parser.parse_args()

    results: list[CheckResult] = []

    for key in args.required_env:
        value = os.environ.get(key)
        if value:
            results.append(CheckResult("required_env", key, True, "set"))
        else:
            results.append(CheckResult("required_env", key, False, "missing"))

    for command in args.required_command:
        path = shutil.which(command)
        if path:
            results.append(CheckResult("required_command", command, True, path))
        else:
            results.append(CheckResult("required_command", command, False, "not found on PATH"))

    for command in args.smoke_command:
        results.append(run_command(command, args.timeout))

    passed = all(r.ok for r in results) if results else True

    if args.json:
        payload = {
            "pass": passed,
            "checks": [asdict(r) for r in results],
        }
        print(json.dumps(payload, indent=2))
    else:
        print("MCP integration preflight")
        if not results:
            print("- No checks configured. Pass by default.")
        for r in results:
            status = "PASS" if r.ok else "FAIL"
            print(f"- [{status}] {r.kind}: {r.target} -> {r.detail}")
        print("Status: PASS" if passed else "Status: FAIL")

    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
