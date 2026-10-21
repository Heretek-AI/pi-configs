---
name: brand-copy-spec/actionable-microcopy-refactoring
description: Specialized capabilities and operational workflow for Brand Voice, Copywriting & Microcopy Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: brand-copy-spec/actionable-microcopy-refactoring

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `brand-copy-spec` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx i18n-ally-cli
   ```
2. Execute core operations adhering to i18n translation tables (`locales/*.json`, `i18n/*.yaml`), button labels, modal dialogue text, system error messages, and brand style guides..
3. Run self-correction verification:
   ```bash
   Executes `npx i18n-lint locales/en.json` and runs an automated missing-keys comparator against all active language translations.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with brand-copy-spec boundaries.
- Exit code 0 required on all diagnostic commands.
