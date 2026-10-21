---
name: systematic-debugging
description: Specialized capabilities and operational workflow for Site Reliability Engineer & Incident Commander
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: systematic-debugging

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `sre-incident-eng` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   curl -sI
   ```
2. Execute core operations adhering to Incident post-mortems (`docs/postmortems/*.md`), operational runbooks (`runbooks/**`), health check endpoints, circuit breakers, and chaos resilience configs..
3. Run self-correction verification:
   ```bash
   Verifies all authored runbooks against the operational readiness checklist and ensures that post-mortems strictly include concrete timeline timestamps and action item owners.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with sre-incident-eng boundaries.
- Exit code 0 required on all diagnostic commands.
