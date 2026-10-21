---
name: threejs-game-skills
description: Specialized capabilities and operational workflow for Graphics & Shader Pipeline Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: threejs-game-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `graphics-shader-eng` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   glslangValidator
   ```
2. Execute core operations adhering to Shader sources (`shaders/**/*.glsl`, `shaders/**/*.wgsl`, `shaders/**/*.hlsl`), material parameters, render pass configurations, and shader compilation validator tests..
3. Run self-correction verification:
   ```bash
   Validates all authored shaders with `glslangValidator -V` and `spirv-val`; confirms zero compile warnings and registers within GPU uniform buffer limits.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with graphics-shader-eng boundaries.
- Exit code 0 required on all diagnostic commands.
