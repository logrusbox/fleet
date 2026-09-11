# Fleet Handoffs

This directory is for active, scoped handoffs that are useful during a bounded transition between people/agents/workstreams.

Handoffs are not a second project-memory system.

## Rules

- A handoff must link the authoritative issue/PR/workstream and owning repository.
- It may summarize unfinished context needed to resume work, but must not duplicate permanent requirements/ADRs/source truth.
- Durable decisions discovered during a handoff must be moved into the proper authoritative document.
- Close/remove stale handoffs after their useful context has been integrated.
- Do not store raw chat transcripts here.
- Never let an old handoff override newer accepted Git.

For general project re-entry, use the top-level spine: `PROJECT.md`, `CURRENT_STATE.md`, `DECISIONS.md`, and `REPOSITORIES.md`.