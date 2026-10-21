---
name: superpowers
description: Specialized capabilities and operational workflow for Product Director & Strategic PRD Author
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `product-director` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   gh issue create
   ```
2. Execute core operations adhering to Product Requirement Documents (`docs/prd/*.md`), user story specifications, feature acceptance criteria, roadmap prioritization, and GitHub milestone mapping..
3. Run self-correction verification:
   ```bash
   Validates all authored PRDs against the strict corporate PRD schema via `node ./scripts/validate-prd.mjs docs/prd/*.md`; ensures exit code 0 before task completion.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with product-director boundaries.
- Exit code 0 required on all diagnostic commands.
