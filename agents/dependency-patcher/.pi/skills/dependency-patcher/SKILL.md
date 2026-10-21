---
name: dependency-patcher
description: Specialized capabilities and operational workflow for Automated SemVer Lockfile Patcher & Vulnerability Remediation
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: dependency-patcher

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `dependency-patcher` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   pnpm audit --fix
   ```
2. Execute core operations adhering to Automated dependency bump commits, package upgrade PRs, CVE remediation notes (`docs/cve-remediation/*.md`), and dependency regression test reports..
3. Run self-correction verification:
   ```bash
   Runs `pnpm audit && cargo audit`; verifies zero remaining high or critical CVE vulnerabilities and validates that the full project test suite passes cleanly.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with dependency-patcher boundaries.
- Exit code 0 required on all diagnostic commands.
