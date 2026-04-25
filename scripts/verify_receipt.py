#!/usr/bin/env python3
"""Verify the archived MPRD case-study receipt used by the paper."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


EXPECTED_HASH = "sha256:b83ee1178c4bea460b9c7e3c67d5ccf1d7ac330e017746236fcfc7274c459561"
EXPECTED_HYPOTHESES = 16003
EXPECTED_REACHABLE = 0
EXPECTED_GATE = "OPEN_FOR_BOUNDED_RESEARCH"


def verify(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    summary = payload.get("summary", {})
    gate_summary = payload.get("gate_summary", {})
    checks = {
        "stable_receipt_hash": payload.get("stable_receipt_hash") == EXPECTED_HASH,
        "hypotheses": summary.get("hypotheses") == EXPECTED_HYPOTHESES,
        "reachable_disaster_witnesses": summary.get("reachable_disaster_witnesses")
        == EXPECTED_REACHABLE,
        "gate": gate_summary.get("gate") == EXPECTED_GATE,
    }
    return {
        "ok": all(checks.values()),
        "receipt": str(path),
        "checks": checks,
        "expected": {
            "stable_receipt_hash": EXPECTED_HASH,
            "hypotheses": EXPECTED_HYPOTHESES,
            "reachable_disaster_witnesses": EXPECTED_REACHABLE,
            "gate": EXPECTED_GATE,
        },
        "observed": {
            "stable_receipt_hash": payload.get("stable_receipt_hash"),
            "hypotheses": summary.get("hypotheses"),
            "reachable_disaster_witnesses": summary.get("reachable_disaster_witnesses"),
            "gate": gate_summary.get("gate"),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "receipt",
        nargs="?",
        default="artifact/neuro_symbolic_case_study/neuro_symbolic_disaster_loop_latest.json",
        help="receipt JSON path",
    )
    args = parser.parse_args()
    result = verify(Path(args.receipt))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
