# ADR-0003: Define Fleet through modular, replaceable contracts

- **Status:** Accepted
- **Date:** 2026-08-29
- **Scope:** Fleet-wide architecture across CIC Station, Vincent, external agents, and imported upstream code

## Context

Fleet begins from an upstream-friendly Paperclip fork but must retain control of its product direction. It must initially operate Codex on Vincent workers while allowing future agent providers, transports, source hosts, execution environments, and user interfaces.

Deeply coupling Fleet to Paperclip internals or any single borrowed subsystem would make upstream synchronization difficult and future replacement expensive. Conversely, splitting every module into a separately deployed service would add operational and reliability costs that are unjustified for an initial personal fleet of a small number of workers.

## Decision

Fleet will be designed as a modular system whose behavior is defined by Fleet-owned interfaces, protocols, and durable data contracts. Upstream-derived, borrowed, and independently implemented components will operate behind those boundaries and remain replaceable where practical.

Modularity is a source and contract boundary, not a requirement for microservices. CIC Station should default to the smallest practical deployment topology, including a modular monolith where appropriate. A module becomes a separately deployed service only when isolation, scaling, security, failure containment, or independent lifecycle requirements justify that boundary.

## Required module boundaries

The architecture must maintain explicit boundaries for:

- CIC project, task, attempt, lease, result, and audit authority;
- Chat interfaces, beginning with ChatGPT-facing MCP;
- Vincent enrollment, worker identity, presence, capability, and work exchange;
- Vincent machine management and agent-independent execution control;
- agent-runtime adapters, beginning with Codex;
- execution providers such as host, container, sandbox, or remote compute;
- source providers, beginning with GitHub-compatible Git;
- transport, beginning with ordinary HTTPS and WebSocket;
- scheduling and lease policy;
- worker, Git, model-provider, and human authentication domains;
- operational persistence;
- approval, network, software, and project-access policy;
- web and other operator interfaces;
- versioned worker/project capability and skill packages.

The owning component repositories will define the concrete contracts and ADRs needed to implement these boundaries.

## Integration rules

1. Fleet-owned contracts define required behavior; imported projects do not become architectural authorities merely because their code is reused.
2. Prefer adapters, extension points, events, and composition over invasive modifications to upstream Paperclip.
3. Keep provider-specific behavior outside the CIC domain core and Vincent machine core.
4. Keep transport semantics separate from authoritative work-item, attempt, lease, and result semantics.
5. Separate worker identity from Git credentials, model-provider credentials, and human login.
6. Preserve durable state in implementation-neutral schemas and migrations where practical.
7. Test module contracts independently so an implementation can be replaced without silently changing Fleet behavior.
8. Record exact provenance and licensing for every imported implementation.
9. Avoid abstraction that has no identified alternate implementation, security boundary, or testable contract; modularity must reduce coupling rather than create ceremony.

## Consequences

- Fleet can adopt Paperclip quickly without making Paperclip's internal model permanently authoritative.
- Harness, Herd, Cotal, and future systems can supply selected implementations without controlling the overall architecture.
- Codex remains the first supported runtime but not a permanent hard dependency.
- The initial system can remain simple to deploy on one VPS while preserving future replacement points.
- Interface design and contract testing become early engineering work.
- Some duplicate adapter code and translation layers are accepted in exchange for reduced coupling.
- Excessive service decomposition and speculative abstraction are explicitly discouraged.
