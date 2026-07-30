# Inherent-risk method

Assess exposure without crediting vendor controls.

## Dimensions

Rate each dimension `Low`, `Moderate`, `High`, `Critical`, or `Unknown`:

1. Data: sensitivity, volume, subject population, regulated status, retention.
2. Access: production, privileged, network, code, physical, or no access.
3. Operational dependency: customer harm, safety, financial, legal, or mission
   impact if unavailable or corrupted.
4. Resilience: required RTO/RPO, substitutability, transition time, single
   source, geographic or provider concentration.
5. Regulatory and geographic exposure: regulated activity, cross-border
   processing, government access, localization, or sanctions considerations.
6. Supply chain: material subprocessors, opaque dependencies, software or
   hardware provenance, and fourth-party concentration.

## Overrides

Propose `Critical` or the organization's highest applicable path when any fact
could create catastrophic or intolerable impact, including:

- a critical activity with low substitutability;
- privileged or control-plane production access;
- sensitive or regulated data at material scale;
- a single point of failure against required recovery objectives;
- safety, systemic, or severe customer-harm potential.

Use `High` or enhanced review for substantial exposure below the critical
threshold. Never average an override away.

## Sample tiers

Use only if organizational policy is unavailable:

- `Tier 1 — Critical`: enhanced diligence, executive risk ownership, continuous
  trigger monitoring, tested exit strategy.
- `Tier 2 — High`: broad diligence, annual refresh, formal remediation.
- `Tier 3 — Moderate`: targeted diligence, periodic refresh.
- `Tier 4 — Low`: basic identity, sanctions, business, and contract checks.

Document the proposed nature of this model and require governance approval
before operational adoption.
