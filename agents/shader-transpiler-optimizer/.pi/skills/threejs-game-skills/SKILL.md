---
name: threejs-game-skills
description: Specialized capabilities and operational workflow for Multi-Target Shader Transpilation & GPU Optimizer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: threejs-game-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `shader-transpiler-optimizer` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   naga
   ```
2. Execute core operations adhering to Shader transpilation pipelines (`tools/shaders/**`), Naga/Spirv-Cross configurations, intermediate representation (IR) dumps, and register allocation reports..
3. Run self-correction verification:
   ```bash
   Runs `spirv-opt -O input.spv -o optimized.spv && spirv-val optimized.spv`; verifies reduced instruction count and zero validation errors.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with shader-transpiler-optimizer boundaries.
- Exit code 0 required on all diagnostic commands.
