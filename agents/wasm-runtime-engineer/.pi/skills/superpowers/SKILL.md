---
name: superpowers
description: Specialized capabilities and operational workflow for WebAssembly & Component Model Systems Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `wasm-runtime-engineer` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   wasm-tools component new
   ```
2. Execute core operations adhering to WASM target configurations, WIT (WebAssembly Interface Types) specifications (`*.wit`), component bindings, memory sandboxing boundaries, and `wasm-opt` pipeline passes..
3. Run self-correction verification:
   ```bash
   Compiles and executes Wasm tests via `wasmtime run --wasm component-model target/wasm32-wasip2/release/module.wasm` and verifies binary size optimization with `wasm-opt`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with wasm-runtime-engineer boundaries.
- Exit code 0 required on all diagnostic commands.
