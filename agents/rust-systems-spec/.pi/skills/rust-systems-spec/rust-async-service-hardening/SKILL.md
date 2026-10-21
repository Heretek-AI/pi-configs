---
name: rust-systems-spec/rust-async-service-hardening
description: Specialized capabilities and operational workflow for Rust Systems & Memory-Safety Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: rust-systems-spec/rust-async-service-hardening

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `rust-systems-spec` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   cargo check
   ```
2. Execute core operations adhering to Rust source crates (`crates/**`, `src/**/*.rs`), `Cargo.toml`, Tokio async runtimes, concurrency primitives (Arc/Mutex/RwLock/Channels), and `cargo clippy` hygiene..
3. Run self-correction verification:
   ```bash
   Runs `cargo clippy --all-targets -- -D warnings && cargo test` to prove that code compiles without warnings, passes all unit tests, and satisfies borrow checker invariants.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with rust-systems-spec boundaries.
- Exit code 0 required on all diagnostic commands.
