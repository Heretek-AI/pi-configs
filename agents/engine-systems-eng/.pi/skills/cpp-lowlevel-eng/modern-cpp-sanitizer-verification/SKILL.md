---
name: cpp-lowlevel-eng/modern-cpp-sanitizer-verification
description: Specialized capabilities and operational workflow for Engine Core & Low-Level Memory Allocator Programmer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: cpp-lowlevel-eng/modern-cpp-sanitizer-verification

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `engine-systems-eng` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   cargo bench
   ```
2. Execute core operations adhering to Engine core frameworks (`engine/**`, `src/core/**`), memory pools, threading workers, cache line alignment attributes, and frame timing clocks..
3. Run self-correction verification:
   ```bash
   Executes performance microbenchmarks (`cargo bench` or `./build/bin/bench_allocator`) to verify zero allocation regression in hot render loops.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with engine-systems-eng boundaries.
- Exit code 0 required on all diagnostic commands.
