---
name: superpowers
description: Specialized capabilities and operational workflow for Frontend Performance & Core Web Vitals Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `fe-perf-eng` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx lighthouse-ci collect
   ```
2. Execute core operations adhering to Webpack/Vite/Turbopack bundle analyzer configurations, lazy loading strategies, font loading subsets, critical CSS inlining, and Web Vital telemetry..
3. Run self-correction verification:
   ```bash
   Executes `npx size-limit` to verify bundle budget compliance and verifies Lighthouse performance score >= 90 with `npx lhci autorun --collect.numberOfRuns=1`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with fe-perf-eng boundaries.
- Exit code 0 required on all diagnostic commands.
