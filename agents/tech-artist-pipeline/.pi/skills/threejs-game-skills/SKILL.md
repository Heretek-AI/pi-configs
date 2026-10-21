---
name: threejs-game-skills
description: Specialized capabilities and operational workflow for Technical Artist & Asset Pipeline Lead
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: threejs-game-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `tech-artist-pipeline` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx gltf-transform optimize
   ```
2. Execute core operations adhering to Asset conversion scripts (`tools/pipeline/**`), `gltf-transform` workflows, texture compression manifests, skeletal hierarchy verifications, and asset budget reports..
3. Run self-correction verification:
   ```bash
   Verifies all processed 3D assets comply with memory budgets (triangle count < 50k for props, texture resolution <= 2048x2048, KTX2 compression verified) via `gltf-transform inspect`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with tech-artist-pipeline boundaries.
- Exit code 0 required on all diagnostic commands.
