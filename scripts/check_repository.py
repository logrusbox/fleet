#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "PROJECT.md",
    "CURRENT_STATE.md",
    "DECISIONS.md",
    "REPOSITORIES.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/README.md",
    "docs/PROGRAM_ROADMAP.md",
    "docs/STATUS.md",
    "docs/GOVERNANCE.md",
    "docs/decisions/README.md",
    "docs/history/CHAT_RECONCILIATION.md",
    "docs/evaluations/README.md",
    "docs/interfaces/AUTHORITY_BOUNDARY.md",
    "workstreams/cic-station.md",
    "workstreams/vincent.md",
    "workstreams/codex-execution.md",
    "workstreams/enrollment-identity.md",
    "workstreams/leasing-task-routing.md",
    "workstreams/deployment.md",
    "handoffs/README.md",
]
FORBIDDEN = [
    "PROJECT_START_HERE.md",
    "CONTINUATION_HANDOFF.md",
    "PLANNED_FEATURES.md",
]
CURRENT_BRANDING_FILES = [
    "README.md",
    "PROJECT.md",
    "CURRENT_STATE.md",
    "DECISIONS.md",
    "REPOSITORIES.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/README.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/cross-product.yml",
    ".github/ISSUE_TEMPLATE/quick-capture.yml",
]
ESCAPED_NEWLINE_FILES = [
    "PROJECT.md",
    "CURRENT_STATE.md",
    "DECISIONS.md",
    "REPOSITORIES.md",
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
    if "PROJECT.md" not in readme or "CURRENT_STATE.md" not in readme:
        failures.append("README must route project re-entry through the durable spine")

    project = read("PROJECT.md")
    if "Git owns durable development truth" not in project or "CIC Station owns live operational orchestration state" not in project:
        failures.append("PROJECT must preserve the Git/CIC authority boundary")

    agents = read("AGENTS.md")
    if "CHAT_RECONCILIATION.md" not in agents:
        failures.append("AGENTS must reference chat reconciliation precedence rules")

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
