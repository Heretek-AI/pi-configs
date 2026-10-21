---
name: superpowers
description: Specialized capabilities and operational workflow for Performance Load & k6 Stress Testing Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `load-stress-tester` in the Quality Assurance & Verification Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   k6 run tests/load/scenario.js
   ```
2. Execute core operations adhering to Load test scripts (`tests/load/**/*.js`), k6 scenario definitions, threshold configurations (p95 < 200ms), and load test benchmark reports..
3. Run self-correction verification:
   ```bash
   Executes local baseline scenario `k6 run --vus 10 --duration 10s tests/load/smoke.js` to verify zero threshold failures and zero uncaught HTTP 5xx errors.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with load-stress-tester boundaries.
- Exit code 0 required on all diagnostic commands.
