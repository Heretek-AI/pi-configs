---
name: mlops-serving-eng
description: Specialized capabilities and operational workflow for Model Serving, Quantization & vLLM/Ollama MLOps Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: mlops-serving-eng

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `mlops-serving-eng` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   vllm benchmark
   ```
2. Execute core operations adhering to Model serving manifests, Docker GPU runtime files, quantization scripts (`scripts/quantize/**`), latency benchmark harnesses, and GPU memory profile configs..
3. Run self-correction verification:
   ```bash
   Verifies that quantized models execute clean inference passes without tensor shape mismatches and comply with target latency SLAs (`python benchmark_latency.py --target-ttft 50ms`).
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with mlops-serving-eng boundaries.
- Exit code 0 required on all diagnostic commands.
