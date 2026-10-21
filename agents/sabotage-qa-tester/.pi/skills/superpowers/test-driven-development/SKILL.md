---
name: superpowers/test-driven-development
description: Specialized capabilities and operational workflow for Mutation Testing & Chaos Sabotage Tester
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers/test-driven-development

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `sabotage-qa-tester` in the Quality Assurance & Verification Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx stryker run
   ```
2. Execute core operations adhering to Mutation test configurations (`stryker.config.json`, `mutants.toml`), mutant kill reports, boundary condition sabotage injections, and test gap remediation tickets..
3. Run self-correction verification:
   ```bash
   Verifies mutation score threshold (>= 80% mutants killed) with `npx stryker run` or `cargo mutants`; flags any surviving mutants as test assertion blind spots.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with sabotage-qa-tester boundaries.
- Exit code 0 required on all diagnostic commands.
