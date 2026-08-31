#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/PROGRAM_ROADMAP.md",
    "docs/STATUS.md",
    "docs/GOVERNANCE.md",
    "docs/decisions/README.md",
]
FORBIDDEN = [
    "PROJECT_START_HERE.md",
    "CONTINUATION_HANDOFF.md",
    "PLANNED_FEATURES.md",
]

def main() -> int:
    failures: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required file: {rel}")
    for rel in FORBIDDEN:
        if (ROOT / rel).exists() or (ROOT / "docs" / rel).exists():
            failures.append(f"retired planning file present: {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
    if "logrusbox/vincent" not in readme or "logrusbox/cic-station" not in readme:
        failures.append("README must identify both component repositories")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Fleet repository validation: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
