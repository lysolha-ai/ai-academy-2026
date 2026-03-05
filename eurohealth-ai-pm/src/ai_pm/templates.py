"""Template builders for AI-PM delivery backbone markdown artifacts."""

from __future__ import annotations

from datetime import date


def sprint_board_template() -> str:
    """Return sprint board markdown template aligned to EuroHealth Week 1 build controls."""
    today: str = date.today().isoformat()
    return f"""# Sprint 1 Board — AI-PM Delivery Backbone

**Date:** {today}
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
"""


def standup_template() -> str:
    """Return daily standup markdown template aligned to governance cadence."""
    return """# Daily Standup Template — AI-PM

**Facilitator:** AI-PM
**Duration:** 15 minutes
**Cadence Rule:** Decisions and blockers logged same day in the conditions tracker.

## Per-Role Update
| Role | Yesterday | Today | Blocker | Needs From | Risk (R/A/G) |
|---|---|---|---|---|---|
| AI-PM |  |  |  |  |  |
| AI-SEC |  |  |  |  |  |
| AI-SE |  |  |  |  |  |
| FDE |  |  |  |  |  |
| AI-DS |  |  |  |  |  |
| AI-DA |  |  |  |  |  |
| AI-FE |  |  |  |  |  |

## Gate Snapshot (C1-C7)
- C1 Legal HIGH-RISK determination:
- C2 Residual-risk acceptance path:
- C3 DPIA/GDPR closure:
- C4 Shadow AI ownership:
- C5 Baseline denominator (ROI):
- C6 24h reconstructability evidence:
- C7 Board evidence pack readiness:

## Decisions Taken Today
- 

## Escalations (must be triggered within 48h)
- 

## Daily Control Checks
- Fail-closed behavior verified today (`PDP unavailable -> BLOCK + ESCALATE`).
- No token streaming before policy decision verified.
"""


def stakeholder_update_template() -> str:
    """Return stakeholder update markdown template for CIO/SteerCo."""
    return """# Stakeholder Update — CIO / Steering Committee

**Prepared by:** AI-PM
**Program:** EuroHealth AI Helpdesk
**Verdict Posture:** Go with Conditions

## Executive Summary
- Current posture: Controlled build under provisional HIGH-RISK governance.
- Progress this period:
- Top blockers this period:

## Conditions Tracker Snapshot
| Condition | Status | Owner | Deadline | Scale Blocker | Evidence Link |
|---|---|---|---|---|---|
| C1 Final HIGH-RISK legal determination | OPEN | AI-SEC + Legal/CISO | 2026-03-14 | Yes |  |
| C2 Residual-risk acceptance (AI-PM + CIO) | OPEN | AI-PM + CIO | Pre-expansion | Yes |  |
| C3 DPIA + GDPR retention/DSR sign-off | OPEN | AI-SEC + DPO/Legal | 2026-05-15 | Yes |  |
| C4 Shadow AI ownership formalization | OPEN | CIO + AI-PM + HR/Claims | 2026-05-15 | Yes |  |
| C5 Baseline denominator confirmation | OPEN | AI-DA | Week 1 | No |  |
| C6 24h reconstructability + audit integrity | OPEN | AI-SE | 2026-05-15 | Yes |  |
| C7 Board-ready evidence pack | OPEN | AI-PM + AI-SEC | 2026-07-31 | Yes |  |

## Governance Enforcement Statement
- No production scale or board-facing ROI claims proceed unless all legal/governance scale blockers are formally CLOSED, signed, and traceable in the decision log.

## Decisions Needed from CIO
1. 
2. 

## Next Reporting Commitments
- 
"""


def scope_tracker_template() -> str:
    """Return scope tracker markdown template aligned to Phase 1 boundaries."""
    return """# Scope Tracker — Phase 1

**Owner:** AI-PM
**Rule:** Scope expansion requires explicit gate approval under Art. 9 governance.

## In Scope (Phase 1)
- IT Helpdesk only.
- Assistive L1 support (human-in-the-loop).
- On-prem governed runtime.
- Policy-as-code enforcement and auditability.

## Out of Scope (Phase 1)
- HR automation.
- Claims automation.
- Autonomous L3 remediation.
- Cloud deployment or external telemetry.

## Deferred (Phase 2+)
- HR/Claims onboarding after C1-C4 closure.
- Expanded intent coverage after KPI stability proof.
- Scale expansion only after residual-risk acceptance and legal closure.

## Scope Change Log
| Date | Request | Requested By | Impact | Decision | Approver | Notes |
|---|---|---|---|---|---|---|

## Guardrails
- No scope change if any scale blocker is OPEN (C1/C2/C3/C4/C6/C7).
- No board-facing ROI claim while C5 is OPEN.
- Reopened scale blocker reactivates release freeze authority automatically.
"""
