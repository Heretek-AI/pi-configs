---
name: cpp-lowlevel-eng/modern-cpp-sanitizer-verification
description: Specialized capabilities and operational workflow for C++ Systems & Low-Level Systems Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: cpp-lowlevel-eng/modern-cpp-sanitizer-verification

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `cpp-lowlevel-eng` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   cmake --build build
   ```
2. Execute core operations adhering to C++ source and header files (`src/**/*.cpp`, `include/**/*.hpp`), `CMakeLists.txt`, conan/vcpkg package manifests, benchmark harnesses, and sanitizer targets..
3. Run self-correction verification:
   ```bash
   Builds and tests with AddressSanitizer and UndefinedBehaviorSanitizer enabled (`ctest -V`); verifies zero memory leaks, buffer overruns, or undefined behavior before yield.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with cpp-lowlevel-eng boundaries.
- Exit code 0 required on all diagnostic commands.
