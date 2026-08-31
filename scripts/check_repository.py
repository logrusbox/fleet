#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

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
CURRENT_BRANDING_FILES = [
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/README.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/cross-product.yml",
    ".github/ISSUE_TEMPLATE/quick-capture.yml",
]
ESCAPED_NEWLINE_FILES = [
    "docs/PROGRAM_ROADMAP.md",
    "docs/STATUS.md",
    "docs/decisions/README.md",
]


def read(rel: str) -> str:
    path = ROOT / rel
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def main() -> int:
    failures: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required file: {rel}")
    for rel in FORBIDDEN:
        if (ROOT / rel).exists() or (ROOT / "docs" / rel).exists():
            failures.append(f"retired planning file present: {rel}")

    readme = read("README.md")
    if "logrusbox/vincent" not in readme or "logrusbox/cic-station" not in readme:
        failures.append("README must identify both component repositories")

    for rel in CURRENT_BRANDING_FILES:
        text = read(rel)
        if "VINCENT Program" in text or "VINCENT program" in text:
            failures.append(f"obsolete VINCENT Program branding present: {rel}")

    for rel in ESCAPED_NEWLINE_FILES:
        if "\\n" in read(rel):
            failures.append(f"literal escaped newline present: {rel}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Fleet repository validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
