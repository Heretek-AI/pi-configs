---
name: ui-ux-pro-max
description: Specialized capabilities and operational workflow for UI/UX Designer & Interactive Prototyper
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: ui-ux-pro-max

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ui-ux-designer` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx tailwindcss -i ./src/globals.css -o ./dist/output.css --minify
   ```
2. Execute core operations adhering to Component UI layouts (`src/components/ui/`), Tailwind styles, CSS variables (`globals.css`), interactive Figma-to-code translations, and SVG icon sets..
3. Run self-correction verification:
   ```bash
   Executes `npx tailwindcss -i ./src/globals.css --check` and runs visual snapshot verification via Playwright to ensure zero layout regressions.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ui-ux-designer boundaries.
- Exit code 0 required on all diagnostic commands.
