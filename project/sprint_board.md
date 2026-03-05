# Sprint 1 Board — AI-PM Delivery Backbone

**Date:** 2026-03-05
**Sprint Window:** Week 1 Build (Day 16-20)
**Goal:** Prove enforceable control before automation scale.
**Mode:** Controlled build under Go with Conditions.

## Task Board
| ID | Role | Task | Owner | Due | Dependency | Status |
|---|---|---|---|---|---|---|
| PM-01 | AI-PM | Daily standup + blocker triage cadence | AI-PM | Daily | None | IN PROGRESS |
| PM-02 | AI-PM | Gate tracker updates (C1-C7) + evidence links | AI-PM | Daily | AI-SEC/AI-DA updates | IN PROGRESS |
| PM-03 | AI-PM | Scope lock enforcement (IT-only assistive Phase 1) | AI-PM | Day 16 | CIO alignment | IN PROGRESS |
| SEC-01 | AI-SEC | Legal HIGH-RISK determination closure package (C1) | AI-SEC + Legal/CISO | 2026-03-14 | Legal slot | OPEN |
| SEC-02 | AI-SEC | Policy-as-code runtime enforcement validation | AI-SEC | Day 17 | FDE runtime hook | OPEN |
| SE-01 | AI-SE | 24h reconstructability drill plan (C6) | AI-SE | Day 18 | Audit schema baseline | OPEN |
| FDE-01 | FDE | Governed runtime path validation (ALLOW/BLOCK) | FDE | Day 16 | Runtime scaffold | IN PROGRESS |
| FDE-02 | FDE | Capacity envelope test and concurrency N definition | FDE | Day 19 | Infra slot | BLOCKED |
| DS-01 | AI-DS | Containment + parity test pack setup | AI-DS | Day 18 | Query set | OPEN |
| DA-01 | AI-DA | Baseline denominator sign-off (C5) | AI-DA | Week 1 | Source data availability | OPEN |
| FE-01 | AI-FE | No-stream-before-ALLOW + override UX validation | AI-FE | Day 17 | PEP output contract | OPEN |

## Week 1 Exit Criteria
- Governed runtime scaffold active (`AI-FE -> API Gateway -> Retriever -> Generator -> PEP/PDP -> Response -> Audit Logger -> Monitoring`).
- 1 `ALLOW` and 1 `BLOCK` scenario pass with signed audit records.
- No token streaming before policy decision.
- CI gate blocks promotion when policy tests fail.

## Non-Negotiable Guardrails
- No production scale while any scale blocker is OPEN (C1/C2/C3/C4/C6/C7).
- No board-facing ROI claims while C5 is OPEN.
- If any closed scale blocker reopens, release freeze authority reactivates automatically.
