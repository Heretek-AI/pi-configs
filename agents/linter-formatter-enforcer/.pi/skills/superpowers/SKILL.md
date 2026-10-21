---
name: superpowers
description: Specialized capabilities and operational workflow for Autonomous Linter & Code Formatting Enforcer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `linter-formatter-enforcer` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx @biomejs/biome check --apply .
   ```
2. Execute core operations adhering to Linter configurations (`biome.json`, `.ruff.toml`, `.clang-format`, `rustfmt.toml`), automated file formatting triggers, and CI linter gate manifests..
3. Run self-correction verification:
   ```bash
   Runs comprehensive multi-tool check (`npx biome check . && ruff check . && cargo fmt -- --check && shellcheck scripts/*.sh`); verifies exit code 0 across all linters.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with linter-formatter-enforcer boundaries.
- Exit code 0 required on all diagnostic commands.
