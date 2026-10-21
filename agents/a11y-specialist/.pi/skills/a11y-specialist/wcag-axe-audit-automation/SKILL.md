---
name: a11y-specialist/wcag-axe-audit-automation
description: Specialized capabilities and operational workflow for Accessibility & WCAG 2.2 AA Compliance Auditor
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: a11y-specialist/wcag-axe-audit-automation

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `a11y-specialist` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx @axe-core/cli
   ```
2. Execute core operations adhering to Accessibility audit reports (`docs/a11y/*.md`), ARIA markup guidelines, focus trap components, skip-to-content implementations, and axe-core test suites..
3. Run self-correction verification:
   ```bash
   Runs `npx pa11y-ci --threshold 0` and ensures that zero serious or critical WCAG 2.2 accessibility violations exist in all modified routes.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with a11y-specialist boundaries.
- Exit code 0 required on all diagnostic commands.
