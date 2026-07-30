# Evidence review rules

## Sufficiency test

Assess five attributes:

- Relevance: answers the actual service-specific question.
- Reliability: source, provenance, independence, and integrity are credible.
- Scope: covers the legal entity, service, location, system, and control.
- Freshness: period is suitable for the risk and known change.
- Completeness: exceptions, dependencies, and required elements are included.

## Artifact-specific checks

### SOC reports

Check report type, period, auditor opinion, system scope, tests and exceptions,
complementary user-entity controls, complementary subservice controls, and
inclusive/carve-out treatment. Identify a bridge gap; do not assume it.

### ISO certificates

Check standard/version, certified legal entity, service/location scope,
effective and expiry dates, certification body, accreditation indicators, and
Statement of Applicability relevance if available. Certification is not a
service-specific operating-effectiveness conclusion.

### Penetration-test summaries

Check tester independence, date, scope, exclusions, methodology, severity
definitions, material findings, remediation status, and retest. Avoid retaining
exploit details unless needed and protected.

### Resilience evidence

Compare tested scenario, dependencies, achieved recovery, data loss, date, and
open actions against required RTO/RPO and service scope.

### Policies and questionnaires

Use them as design or assertion evidence. Seek operating evidence for material
claims when risk warrants it.

## Contradictions

Record both statements, their sources, and the decision affected. Do not choose
the more favorable statement without stronger support.
