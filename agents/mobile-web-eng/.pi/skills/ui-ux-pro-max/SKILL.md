---
name: ui-ux-pro-max
description: Specialized capabilities and operational workflow for Mobile Web & Responsive Layout Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: ui-ux-pro-max

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `mobile-web-eng` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx playwright test --project=Mobile_Safari
   ```
2. Execute core operations adhering to Responsive breakpoint CSS, touch target sizes (48x48px min), mobile navigation sheets, pull-to-refresh primitives, and PWA service worker configurations..
3. Run self-correction verification:
   ```bash
   Runs Playwright mobile device emulation across iPhone 15 and Pixel 7 viewports (`npx playwright test --project='Mobile Chrome','Mobile Safari'`) to verify zero horizontal overflow.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with mobile-web-eng boundaries.
- Exit code 0 required on all diagnostic commands.
