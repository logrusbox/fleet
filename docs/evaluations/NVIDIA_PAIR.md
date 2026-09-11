# NVIDIA Personal AI Router (PAIR) Evaluation

**Original discussion date:** 2026-09-03  
**Reconciled:** 2026-09-11  
**Classification:** FUTURE EVALUATION  
**Decision status:** Not adopted; not a Fleet 1.0 requirement

This note preserves the durable result of evaluating NVIDIA Personal AI Router (PAIR) against Fleet. It does not change current Fleet architecture, component requirements, or roadmap scope.

## What PAIR is

NVIDIA PAIR is an Apache-2.0-licensed local inference router for compatible computers on the same local network.

Observed capabilities from NVIDIA's public repository and documentation as of 2026-09-11:

- discovers or manually connects participating nodes on a local network;
- pairs nodes into a trusted cluster;
- manages or adopts supported local inference engines, currently Ollama and LM Studio;
- exposes Ollama-compatible and OpenAI-compatible local proxy endpoints to applications;
- routes each independent inference request to one eligible node based on reachability, engine/model availability, and workload;
- encrypts node-to-node traffic inside the paired cluster;
- does **not** pool GPU memory, combine GPUs into one logical GPU, shard one model across machines, or split a single in-flight request across multiple nodes.

Canonical sources:

- <https://github.com/NVIDIA/Personal-AI-Router>
- <https://docs.nvidia.com/local-ai/nvpair/>
- <https://github.com/NVIDIA/Personal-AI-Router/blob/main/LICENSE>

## Relationship to Fleet

PAIR does not replace Fleet's accepted product boundary.

Fleet remains responsible for durable work orchestration across managed workers: CIC Station authority, Vincent worker lifecycle, explicit enrollment and authorization, work items and attempts, leases and reassignment, stale-result fencing, project/repository constraints, durable results, audit state, and remote-worker operation.

PAIR instead operates below that layer as an inference-routing mechanism. It chooses which local machine serves a model request; it does not provide Fleet's durable project/work authority or managed-worker semantics.

This distinction is already compatible with accepted Fleet architecture:

- Fleet owns modular, replaceable runtime and execution-provider boundaries.
- Vincent's core lifecycle is provider-neutral and already anticipates Ollama/local-model providers.
- CIC Station work semantics remain separate from provider-specific execution details.

The durable conclusion from the 2026-09-03 discussion is therefore:

> PAIR does not negate Fleet. If useful, it can sit behind Fleet's provider/execution boundary so Fleet orchestrates durable work while PAIR routes local inference requests.

## Potential future use

PAIR is worth evaluating later as one or more of:

1. an optional Vincent local-model backend exposed through its OpenAI-compatible or Ollama-compatible endpoint;
2. a way for one Vincent worker or local Fleet site to use several nearby inference-capable machines without Fleet itself implementing LAN model-routing logic;
3. a selective code/protocol donor for local discovery, routing, engine management, proxy compatibility, or telemetry where direct integration is insufficient.

Any source reuse must follow Fleet's normal provenance procedure and verify the exact upstream commit, file-level notices, dependency licenses, and attribution requirements before import.

## Important boundaries

Do not infer any of the following from this evaluation:

- PAIR is not selected as a required Fleet dependency.
- Fleet 1.0 does not gain a local inference cluster requirement.
- PAIR's same-LAN cluster model does not replace Fleet's remote Vincent connectivity model.
- PAIR's node pairing does not replace Vincent/CIC Station worker identity, enrollment, authorization, or revocation.
- PAIR's request routing does not replace CIC Station work-item, attempt, lease, result, or audit authority.
- Fleet should not build PAIR-equivalent local inference routing unless a demonstrated Fleet use case requires behavior PAIR or another replaceable backend cannot provide.

## Re-evaluation triggers

Revisit PAIR when Fleet begins implementing local-model providers, heterogeneous inference resources, or a demonstrated need to route concurrent local inference across multiple machines. At that point evaluate:

- supported operating systems and accelerator constraints;
- headless deployment and lifecycle management on Vincent hosts;
- security and trust implications of PAIR cluster membership;
- whether PAIR should be treated as an external provider endpoint, bundled optional dependency, or source donor;
- failure behavior when a local inference node disappears during Fleet work;
- compatibility with Vincent's provider-health, credential-isolation, execution-bounding, and recovery contracts.

Until such a trigger occurs, PAIR remains FUTURE EVALUATION only.
