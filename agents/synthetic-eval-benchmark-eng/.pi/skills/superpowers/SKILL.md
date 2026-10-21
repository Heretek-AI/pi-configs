---
name: superpowers
description: Specialized capabilities and operational workflow for Synthetic Evaluation, Golden Dataset & LLM Benchmark Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `synthetic-eval-benchmark-eng` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   python -m pytest evals/
   ```
2. Execute core operations adhering to Golden evaluation datasets (`evals/datasets/**`), grading rubrics (`evals/rubrics/**`), LLM-as-a-judge evaluation pipelines, and benchmark scorecards..
3. Run self-correction verification:
   ```bash
   Runs evaluation test harness over the golden dataset; verifies that judge inter-rater reliability (Cohen's Kappa) exceeds 0.80 and outputs full accuracy regression matrices.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with synthetic-eval-benchmark-eng boundaries.
- Exit code 0 required on all diagnostic commands.
