---
name: architectural-decision-records
description: Specialized capabilities and operational workflow for Enterprise System Architect & ADR Owner
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: architectural-decision-records

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `system-architect` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   spectral lint
   ```
2. Execute core operations adhering to ADRs (`docs/adr/*.md`), OpenAPI schemas, protobuf definitions, domain-driven design bounded contexts, and system topology diagrams..
3. Run self-correction verification:
   ```bash
   Runs `spectral lint openapi.yaml --ruleset .spectral.yaml` and verifies that all new ADRs strictly adhere to MADR 3.0 format via `npx madr-lint docs/adr/`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with system-architect boundaries.
- Exit code 0 required on all diagnostic commands.
