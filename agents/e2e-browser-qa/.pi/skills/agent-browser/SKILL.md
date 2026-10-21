---
name: agent-browser
description: Specialized capabilities and operational workflow for End-to-End Browser QA Automation Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: agent-browser

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `e2e-browser-qa` in the Quality Assurance & Verification Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx playwright test
   ```
2. Execute core operations adhering to E2E test suites (`tests/e2e/**`, `e2e/**`), Playwright configuration (`playwright.config.ts`), test fixtures, page object models (POM), and test artifact reports..
3. Run self-correction verification:
   ```bash
   Runs `npx playwright test --retries=1` and inspects traces to verify 100% test pass rate with zero flaky timing timeouts before signing off on test passes.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with e2e-browser-qa boundaries.
- Exit code 0 required on all diagnostic commands.
