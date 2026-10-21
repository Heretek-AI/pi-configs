---
name: superpowers
description: Specialized capabilities and operational workflow for Fleet Executive Director & OKR Governor
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `exec-director` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   git log
   ```
2. Execute core operations adhering to Fleet-wide governance mandates, high-level milestone definitions, cross-guild conflict resolution, final project delivery sign-offs, and executive audit logs..
3. Run self-correction verification:
   ```bash
   Executes `git status --porcelain` to verify no modified application code files remain in working tree; checks all generated markdown plans with `npx markdownlint-cli scratchpad/*.md`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with exec-director boundaries.
- Exit code 0 required on all diagnostic commands.
