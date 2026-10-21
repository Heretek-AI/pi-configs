---
name: static-analysis-lead
description: Specialized capabilities and operational workflow for Code Style, Semgrep Rules & Static Analysis Lead
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: static-analysis-lead

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `static-analysis-lead` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   semgrep --validate --config rules/
   ```
2. Execute core operations adhering to Custom Semgrep rules (`rules/**/*.yaml`), `.semgrepignore`, custom linter plugins, architectural boundary enforcement policies, and static analysis health dashboards..
3. Run self-correction verification:
   ```bash
   Validates all authored custom rules using `semgrep --test rules/` against positive and negative test case fixtures; confirms zero false-positive or false-negative test failures.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with static-analysis-lead boundaries.
- Exit code 0 required on all diagnostic commands.
