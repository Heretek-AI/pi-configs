---
name: threejs-game-skills
description: Specialized capabilities and operational workflow for 3D WebGL / WebGPU & Three.js Graphics Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: threejs-game-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `3d-webgl-threejs-specialist` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx gltf-transform inspect
   ```
2. Execute core operations adhering to Three.js scene graph architectures (`src/three/`), custom GLSL/WGSL shaders, glTF model optimization pipelines, post-processing pipelines, and 3D canvas interaction handlers..
3. Run self-correction verification:
   ```bash
   Validates Three.js canvas headless initialization via `node ./skills/threejs-game-skills/inspect-threejs-canvas.mjs` and verifies draw call counts and memory leaks before task yield.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with 3d-webgl-threejs-specialist boundaries.
- Exit code 0 required on all diagnostic commands.
