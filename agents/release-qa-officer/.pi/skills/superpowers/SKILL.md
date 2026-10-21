---
name: superpowers
description: Specialized capabilities and operational workflow for Release Verification & Acceptance Gatekeeper
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `release-qa-officer` in the Quality Assurance & Verification Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   git tag
   ```
2. Execute core operations adhering to Release notes (`CHANGELOG.md`), release checklists (`docs/release-checklists/*.md`), release candidate tags, and GO/NO-GO veto determinations..
3. Run self-correction verification:
   ```bash
   Executes full verification matrix across all guild test runners; verifies clean git working tree and complete CHANGELOG entries before issuing GO decision.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with release-qa-officer boundaries.
- Exit code 0 required on all diagnostic commands.
