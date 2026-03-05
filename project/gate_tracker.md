# Gate Tracker — Sprint Governance View (C1-C7)

**Program:** EuroHealth AI Helpdesk  
**Owner:** AI-PM (Olha Lys)  
**Purpose:** Dynamic governance control for sprint execution.  
**Master Source:** `governance/operating-model/go-conditions-tracker.md`

**Current Gate Summary:** Scale Blockers Closed: 0/6 | In Progress: 4 | Open: 2 | ROI Gate: IN_PROGRESS | Scale Not Eligible  
**Scale Posture:** Controlled Build  
**Exposure Status:** No Production or Domain Expansion Exposure  
**Scale Eligibility:** Not Eligible

Summary must be reconciled on each status change.

---

## Status Definitions

- `OPEN` - not started or incomplete
- `IN_PROGRESS` - active work underway with partial evidence
- `READY_FOR_SIGNOFF` - closure criteria met; approval pending
- `CLOSED` - signed, evidence-linked, and logged in master tracker

A gate may transition to `CLOSED` only when closure criteria are satisfied and evidence is version-controlled, date-stamped, and independently reviewable.

Reopening a `CLOSED` gate requires documented trigger, date-stamped master tracker entry, and automatic freeze reactivation.

## Health Legend

- `On Track` - delivery currently aligned to deadline and closure criteria
- `Monitoring (External)` - timeline sensitive to external dependency cadence (for example, Legal)
- `Monitoring (Org Dependency)` - timeline sensitive to internal cross-functional ownership alignment
- `Monitoring (Trigger-Based)` - activation depends on governance trigger event, not fixed start date
- `Monitoring (Upstream Dependency)` - gate progress is contingent on prior gate closure trajectory

---

## Runtime & Regulatory Scale Blockers

| Gate | Type | Condition | Dependency | Closure Criteria | Owner(s) | Accountable | Deadline | Health | Status | Evidence Link | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Legal | Final HIGH-RISK legal determination (Art. 9 readiness) | External legal cadence | Signed legal memo + decision-log entry | AI-SEC + Legal/CISO | AI-PM | 2026-03-14 | Monitoring (External) | IN_PROGRESS | governance/compliance/eu-ai-act-classification.md | Secure signed legal determination |
| C2 | Legal/Governance | Residual-risk acceptance signed (AI-PM + CIO) | C1 legal determination clarity + scope expansion trigger | Signed residual-risk acceptance referencing FRIA + gate status | AI-PM + CIO | AI-PM | Before scope expansion beyond assistive Phase 1 | Monitoring (Trigger-Based) | IN_PROGRESS | governance/compliance/fria.md | Prepare signature packet linked to FRIA IDs |
| C3 | Legal | DPIA + GDPR retention/DSR workflow sign-off | DPO/legal review cycle | Signed DPIA + documented retention and DSR workflow | AI-SEC + DPO/Legal | AI-PM | 2026-05-15 | On Track | IN_PROGRESS | governance/compliance/data-protection-impact.md | Finalize DPIA + retention + DSR approvals |
| C4 | Governance | Shadow AI ownership formalized (HR/Claims) | HR leadership alignment | Named owners in governance charter + inventory update | CIO + AI-PM + HR/Claims Leads | CIO | 2026-05-15 | Monitoring (Org Dependency) | IN_PROGRESS | governance/operating-model/governance-charter.md | Assign named owners in charter + inventory |
| C6 | Operational Control | 24h reconstructability + audit integrity demonstrated | Log schema baseline | Drill executed + validated trace artifact (append-only, tamper-evident storage confirmed) | AI-SE | AI-PM | 2026-05-15 | On Track | IN_PROGRESS | governance/evidence/audit-log-schema.json | Execute reconstructability drill + capture evidence |
| C7 | Board Governance | Board-ready evidence pack complete | C1-C6 closure trajectory and evidence maturity | Consolidated trace logs + policy proof + legal memo + residual-risk acceptance + scale validation summary | AI-PM + AI-SEC | AI-PM | 2026-07-31 | Monitoring (Upstream Dependency) | OPEN | governance/board-summary-ai-governance.md | Build consolidated governance evidence pack |

---

## ROI Communication Gate (Non-Scale Blocker)

| Gate | Type | Condition | Closure Criteria | Owner | Accountable | Deadline | Health | Status | Evidence Link | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|
| C5 | Financial | Baseline denominator confirmation (ROI gate) | Validated baseline dataset + sign-off | AI-DA | AI-PM | 2026-03-12 | On Track | IN_PROGRESS | docs/discovery/consolidated-discovery-report.md | Secure validated denominator sign-off for board-facing ROI claims |

---

## Governance Guardrails

- No production scale or scope expansion while any scale blocker is not `CLOSED` (`C1/C2/C3/C4/C6/C7`).
- `C7` is intentionally treated as a scale blocker under current controlled-build governance posture.
- `C5` governs ROI communication readiness only; it is not a runtime scale blocker.
- Any reopened scale blocker automatically reactivates release freeze authority.
- Reopen events must be documented in the master tracker with timestamp and trigger reason.
- Release freeze may be lifted only by AI-PM + CIO (AI-SEC consulted).

---

## Escalation Triggers

- Any gate not `READY_FOR_SIGNOFF` or `CLOSED` within 7 days of deadline escalates to AI-PM + CIO, with recovery plan required within 48h.
- If C1 legal timing slips past 2026-03-14, scale remains frozen and CIO is notified within 48h.

---

## Control Trigger Definitions

**Production scale trigger:** increase in live operational production volume/capacity or exposure. Prohibited while any scale blocker is not `CLOSED`.

**Scope expansion trigger:** expansion beyond assistive Phase 1 scope (for example, HR/Claims domain onboarding). Prohibited until C2 residual-risk acceptance is signed and applicable blockers are closed.

---

## Source-of-Truth Rule

- Daily sprint governance visibility is managed in this file.
- Formal compliance closure is recorded in `governance/operating-model/go-conditions-tracker.md`.
- If discrepancy exists, master tracker prevails and this document must be reconciled the same day.
