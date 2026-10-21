---
name: wshobson__agents/documentation-generation
description: Specialized capabilities and operational workflow for Technical Documentation Lead & Docs-as-Code Architect
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: wshobson__agents/documentation-generation

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `tech-docs-lead` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   markdownlint-cli2
   ```
2. Execute core operations adhering to The entire `docs/` tree, `README.md`, `CONTRIBUTING.md`, architectural diagrams (Mermaid), and code-level API reference documentation..
3. Run self-correction verification:
   ```bash
   Executes `markdownlint-cli2 'docs/**/*.md' 'README.md'` and `npx broken-link-checker docs/` to guarantee zero broken links and zero lint errors.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with tech-docs-lead boundaries.
- Exit code 0 required on all diagnostic commands.
