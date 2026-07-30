---
name: review-tprm-evidence
description: Evaluate third-party evidence for relevance, reliability, scope, freshness, and support, then record control conclusions and follow-ups without deciding risk acceptance. Use when reviewing questionnaires, assurance reports, certifications, policies, test summaries, resilience exercises, or vendor responses.
---

# Review TPRM Evidence

## Objective

Determine exactly what supplied evidence supports, where support is partial,
and what remains unknown. Preserve page, section, period, and scope traceability.

## Required inputs

- Due-diligence plan and review questions
- Evidence files or controlled-view notes, submission date, and provenance
- Service scope, inherent-risk context, and applicable criteria
- Prior findings and vendor clarifications, if relevant

## Workflow

1. Inventory each artifact with title, owner/issuer, date, period, scope,
   version, and access location.
2. Check authenticity indicators, relevance, scope, freshness, and independence.
3. Test each review question using
   `references/evidence-review-rules.md`.
4. Assign one status only: `SUPPORTED`, `PARTIAL`, `GAP`, `UNKNOWN`, or
   `NOT_APPLICABLE`.
5. Cite the exact artifact and location. Separate observed evidence from vendor
   assertions and reviewer inference.
6. Record exceptions, user responsibilities, subservice dependencies, stale
   periods, contradictions, and compensating evidence.
7. Draft the minimum follow-up needed to resolve decision-significant
   uncertainty. Do not demand sensitive detail without a defined use.
8. Copy `assets/evidence-review-record.md` and complete it.

## NIST alignment

Use `references/nist-alignment.md` for NIST CSF 2.0 `GV.SC-06`, `GV.SC-07`, and
`GV.SC-09`. Apply NIST SP 800-161 Rev. 1 as C-SCRM guidance, not as a claim
that a reviewed artifact proves framework conformity.

## Status semantics

- `SUPPORTED`: sufficient relevant evidence supports the stated conclusion.
- `PARTIAL`: some elements are supported, but a defined part is unresolved.
- `GAP`: evidence shows the criterion is not met or a required control is absent.
- `UNKNOWN`: evidence is missing, stale, out of scope, contradictory, or too
  weak to conclude.
- `NOT_APPLICABLE`: a documented fact makes the criterion irrelevant.

Missing evidence is normally `UNKNOWN`, not automatically `GAP`.

## Boundaries

- Do not assign residual risk, accept a gap, or approve the third party.
- Do not fabricate evidence, citations, testing, vendor facts, or approval.
- Do not claim certification or a clean report proves every relevant control.
- Flag potential legal, privacy, audit, or regulatory interpretations for the
  appropriate specialist.
- Keep final decisions and exceptions with an authorized human.

## Quality check

Confirm every conclusion has a citation, status semantics are applied
consistently, scope mismatches are visible, and sensitive evidence is referenced
rather than unnecessarily reproduced.
