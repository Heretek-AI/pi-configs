---
name: observability-eng
description: Specialized capabilities and operational workflow for Observability, Telemetry & OpenTelemetry Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: observability-eng

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `observability-eng` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   promtool check rules
   ```
2. Execute core operations adhering to OpenTelemetry exporter configs, Prometheus recording and alerting rules (`alerts.yaml`), Grafana dashboard JSON models (`dashboards/*.json`), and trace sampling rate policies..
3. Run self-correction verification:
   ```bash
   Validates Prometheus rules with `promtool check rules alerts.yaml` and verifies that all Grafana JSON dashboards pass schema validation without syntax errors.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with observability-eng boundaries.
- Exit code 0 required on all diagnostic commands.
