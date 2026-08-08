#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return rows


def score_case(case: dict, output: str) -> tuple[bool, list[str]]:
    text = output.lower()
    failures = []
    required_all = [str(item).lower() for item in case.get("required_all", [])]
    required_any = [str(item).lower() for item in case.get("required_any", [])]
    forbidden = [str(item).lower() for item in case.get("forbidden", [])]
    missing_all = [item for item in required_all if item not in text]
    if missing_all:
        failures.append("missing required concepts: " + ", ".join(missing_all))
    if required_any and not any(item in text for item in required_any):
        failures.append("missing any-of concepts: " + ", ".join(required_any))
    present_forbidden = [item for item in forbidden if item in text]
    if present_forbidden:
        failures.append("forbidden claims present: " + ", ".join(present_forbidden))
    return not failures, failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Score externally generated Ventura Pro outputs.")
    parser.add_argument("--cases", type=Path, default=Path("evals/semantic_cases.jsonl"))
    parser.add_argument("--outputs", type=Path, required=True)
    args = parser.parse_args()
    cases = {row["id"]: row for row in load_jsonl(args.cases)}
    outputs = {row["id"]: str(row.get("output", "")) for row in load_jsonl(args.outputs)}
    missing = sorted(set(cases) - set(outputs))
    if missing:
        print("SEMANTIC EVALS: FAIL")
        print("missing outputs: " + ", ".join(missing))
        return 2
    failures = []
    for case_id, case in cases.items():
        ok, reasons = score_case(case, outputs[case_id])
        print(f"{case_id}: {'PASS' if ok else 'FAIL'}")
        failures.extend(f"{case_id}: {reason}" for reason in reasons)
    if failures:
        print("SEMANTIC EVALS: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"SEMANTIC EVALS: PASS ({len(cases)} externally supplied outputs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
