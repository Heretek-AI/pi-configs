---
name: superpowers
description: Specialized capabilities and operational workflow for User Experience Telemetry & Feedback Analyst
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ux-research-analyst` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   duckdb
   ```
2. Execute core operations adhering to UX research synthesis reports (`docs/research/*.md`), customer friction matrices, user journey maps, and heuristic usability evaluations..
3. Run self-correction verification:
   ```bash
   Verifies all telemetry aggregation queries with `duckdb -c 'SUMMARIZE SELECT ...'` and checks that markdown findings cite concrete telemetry data points.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ux-research-analyst boundaries.
- Exit code 0 required on all diagnostic commands.
