# K-Dense Agent Capability Evaluation

**Original record date:** 2026-08-28  
**Classification:** FUTURE EVALUATION — not Fleet 1.0 requirements

This note preserves the durable conclusions from a 2026-08-28 review of K-Dense Scientific Agent Skills and K-Dense BYOK. It does not promote either project, Agent Skills, Agent Plugins, MCP packaging, Pi, or any specific implementation into current Fleet architecture.

Current Fleet authority already establishes the relevant accepted boundaries: Codex is the first replaceable agent runtime, Vincent owns agent-independent execution control, CIC Station owns managed orchestration authority, and Fleet preserves versioned worker/project capability and skill-package boundaries. This document records only additional implementation/evaluation lessons worth revisiting later.

## Scientific Agent Skills

K-Dense Scientific Agent Skills is not a CIC Station/Vincent substitute. It is a capability library that teaches compatible agents how to perform specialized work and may bundle instructions, scripts, references, and assets.

### FUTURE EVALUATION: standards-based capability packaging

When Fleet implements portable worker/project capability packages, evaluate the open Agent Skills and Agent Plugins ecosystems before creating a Fleet-specific skill format.

Potential benefits to evaluate:

- portable capability descriptions across multiple agent runtimes;
- progressive loading of skill instructions instead of embedding all specialist knowledge in Vincent;
- reuse of existing host/install tooling where practical;
- separation of machine software installation from agent-facing procedural knowledge;
- packaging that can coexist with MCP-based external tools/services.

A possible future responsibility split to evaluate is:

- CIC Station authorizes/selects required capabilities and policy;
- Vincent retrieves, validates, installs/activates, isolates, and reports the effective capability set;
- the selected agent runtime consumes the skill/plugin/MCP interfaces it supports.

This remains evaluation material. Current Fleet contracts, not an external skill/plugin specification, remain authoritative.

### FUTURE EVALUATION: capability supply-chain security

Treat agent skills/plugins as executable or behavior-changing supply-chain content rather than passive documentation.

Before Fleet distributes third-party capability packages, evaluate a lifecycle such as:

`requested -> retrieved -> scanned -> approved -> pinned -> assigned`

Useful controls to evaluate include:

- exact source/version/commit/hash provenance;
- structural/schema validation;
- static/behavioral scanning of bundled scripts and instructions;
- prompt-injection and unexpected credential/network-access review;
- isolated tests for bundled executable tooling;
- explicit approval/revocation state;
- reporting the exact capability provenance actually used by a worker.

K-Dense's use of automated skill scanning and isolated tests is a useful donor pattern, not an accepted Fleet implementation.

### FUTURE EVALUATION: license at package/skill granularity

Do not assume that every skill/plugin in a permissively licensed repository inherits the repository-level license. Some collections include components with separate terms.

If Fleet later imports, mirrors, redistributes, or automatically provisions third-party capability packages, evaluate per-package/per-skill license metadata and compatibility checks. Fleet's existing rule to record provenance and licensing for imported implementations remains authoritative.

## K-Dense BYOK / Kady

K-Dense BYOK is closer to the worker-runtime side of Fleet than Scientific Agent Skills, but it is primarily a local single-workstation AI environment rather than a distributed enrolled-worker control plane.

### FUTURE EVALUATION: donor areas

If/when Fleet reaches the relevant implementation stage, perform a code-level donor review of K-Dense BYOK rather than adopting it wholesale. Areas worth evaluating include:

- multi-provider runtime/authentication adapters;
- local/hosted model selection boundaries;
- Agent Skills and MCP integration;
- durable project/session/job state and restart recovery;
- resource monitoring;
- optional remote-compute job handling;
- subagent delegation;
- project/workspace persistence and artifact handling.

Any borrowed code or design must stay behind Fleet-owned contracts and pass normal provenance/license/security review.

### FUTURE EVALUATION: subagent ownership boundary

K-Dense BYOK demonstrates local logical subagents under one agent environment. Fleet should evaluate keeping such provider/runtime-internal delegation below the Vincent/CIC scheduling boundary unless a concrete cross-worker requirement justifies exposing it.

Conceptually, CIC Station should schedule/manage durable worker attempts; an agent runtime may internally use subagents without forcing CIC Station to model every internal reasoning/delegation process.

This is not yet an accepted requirement.

### CURRENT compatibility with existing Fleet direction

The following conclusions from the review are already represented by current Fleet authority and therefore require no new decision:

- Vincent should not become a new AI-agent implementation; agent runtimes remain replaceable behind adapters.
- Codex is first, not permanent architecture.
- provider-specific authentication and execution behavior stays outside the Vincent machine core and CIC domain core.
- capability/skill packages belong behind versioned replaceable boundaries.
- imported projects are donors/implementations, not architectural authorities.

## Promotion rule

Nothing in this evaluation should alter Fleet 1.0 scope by itself. Promotion requires a current Fleet/component ADR, requirement, roadmap item, issue/PR with clear authority, or implementation-backed decision in the owning repository.
