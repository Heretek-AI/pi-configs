---
name: requesting-code-review
description: Specialized capabilities and operational workflow for Adversarial Diff Auditor & Codebase Watchdog
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: requesting-code-review

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `adversarial-diff-auditor` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   git diff HEAD~1
   ```
2. Execute core operations adhering to Diff audit review comments, code hygiene flags (`docs/audits/diff-*.md`), peer-review rejection notices, and clean diff verification seals..
3. Run self-correction verification:
   ```bash
   Scans all files touched in the branch diff with `git diff --stat`; confirms zero debug `console.log` statements, zero leftover TODOs without ticket numbers, and zero unformatted files.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with adversarial-diff-auditor boundaries.
- Exit code 0 required on all diagnostic commands.
