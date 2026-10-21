---
name: taste-skill
description: Specialized capabilities and operational workflow for GUI Visual Critic & Anti-AI-Slop Inspector
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: taste-skill

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `gui-visual-critic` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   node ./skills/taste-skill/scripts/inspect.mjs
   ```
2. Execute core operations adhering to Visual regression test suites, screenshot comparison manifests, typography pairing audits, contrast checks, aesthetic anti-slop reports..
3. Run self-correction verification:
   ```bash
   Executes `npx playwright test --project=visual-regression` and `node ./skills/taste-skill/scripts/inspect.mjs --url http://localhost:3000`; verifies exit code 0 and zero visual anomalies (>0.1% delta) before yielding turn.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with gui-visual-critic boundaries.
- Exit code 0 required on all diagnostic commands.
