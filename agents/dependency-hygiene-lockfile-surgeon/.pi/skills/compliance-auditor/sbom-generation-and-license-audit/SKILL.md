---
name: compliance-auditor/sbom-generation-and-license-audit
description: Specialized capabilities and operational workflow for Lockfile Deduplication & Deep Dependency Surgeon
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: compliance-auditor/sbom-generation-and-license-audit

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `dependency-hygiene-lockfile-surgeon` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   pnpm dedupe
   ```
2. Execute core operations adhering to Lockfiles (`pnpm-lock.yaml`, `Cargo.lock`, `uv.lock`, `go.sum`), deduplication configs, dependency override stanzas, and lockfile hygiene audit reports..
3. Run self-correction verification:
   ```bash
   Executes `pnpm dedupe --check` and `cargo tree --duplicates`; verifies lockfile is perfectly deduplicated and runs full test suite (`pnpm test && cargo test`) to guarantee zero regression.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with dependency-hygiene-lockfile-surgeon boundaries.
- Exit code 0 required on all diagnostic commands.
