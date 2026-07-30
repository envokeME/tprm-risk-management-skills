# Monitoring rules

## Signal classes

- Periodic: assurance refresh, access review, resilience exercise, financial
  review, subprocessor confirmation, performance review.
- Event-driven: incident, outage, acquisition, control failure, audit exception,
  certificate lapse, data/location/use change, major release, subcontractor
  change, regulatory action, financial deterioration.
- Internal: SLA breach, complaints, access anomalies, integration change,
  finding age, contract departure, business criticality change.

## Indicator design

For each indicator define:

1. decision condition protected;
2. authoritative source and collection frequency;
3. threshold and severity;
4. validation step for noisy external data;
5. owner and response deadline;
6. escalation and reassessment path;
7. retained evidence and closure criterion.

Do not confuse absence of alerts with evidence of control effectiveness.

## Tiering

Critical relationships normally need more frequent evidence, event monitoring,
incident/recovery participation, concentration review, and tested exit
readiness. Lower tiers may use periodic attestations and exception-driven
review. Tailor to organizational policy and actual exposure.
