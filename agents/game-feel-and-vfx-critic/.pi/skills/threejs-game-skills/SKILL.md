---
name: threejs-game-skills
description: Specialized capabilities and operational workflow for Game Feel, VFX & Juiciness Critic
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: threejs-game-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `game-feel-and-vfx-critic` in the Visual, Aesthetic & Design Systems Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   ffmpeg
   ```
2. Execute core operations adhering to Game feel audits (`docs/critiques/game-feel-*.md`), frame pacing benchmarks, easing curves specifications, screen shake intensity matrices, and VFX shader evaluations..
3. Run self-correction verification:
   ```bash
   Inspects captured video playback or canvas frame buffer using `ffprobe -show_frames` to verify 60fps frame delta stability and checks particle decay timing contracts.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with game-feel-and-vfx-critic boundaries.
- Exit code 0 required on all diagnostic commands.
