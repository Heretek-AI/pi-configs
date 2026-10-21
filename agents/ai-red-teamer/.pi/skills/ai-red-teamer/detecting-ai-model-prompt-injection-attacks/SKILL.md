---
name: ai-red-teamer/detecting-ai-model-prompt-injection-attacks
description: Specialized capabilities and operational workflow for Generative AI & LLM Adversarial Red-Teamer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: ai-red-teamer/detecting-ai-model-prompt-injection-attacks

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ai-red-teamer` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   garak --model_type ...
   ```
2. Execute core operations adhering to AI red-teaming test suites (`tests/red-team/**`), prompt injection evaluation benchmarks, OWASP LLM Top-10 audit reports, and guardrail evaluation harnesses..
3. Run self-correction verification:
   ```bash
   Runs `npx promptfoo eval -c tests/red-team/promptfooconfig.yaml` and verifies that 100% of adversarial jailbreak and system prompt extraction attacks are successfully deflected.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ai-red-teamer boundaries.
- Exit code 0 required on all diagnostic commands.
