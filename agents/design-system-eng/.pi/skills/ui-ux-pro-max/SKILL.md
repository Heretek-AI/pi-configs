---
name: ui-ux-pro-max
description: Specialized capabilities and operational workflow for Design Systems & Component Token Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: ui-ux-pro-max

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `design-system-eng` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx test-storybook
   ```
2. Execute core operations adhering to Design token JSON manifests (`tokens.json`), Storybook configuration (`.storybook/`), atomic primitive components (`src/primitives/`), and cross-brand themes..
3. Run self-correction verification:
   ```bash
   Runs `npx test-storybook --coverage` and checks that all exported tokens compile cleanly via `npx style-dictionary build` with zero missing token references.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with design-system-eng boundaries.
- Exit code 0 required on all diagnostic commands.
