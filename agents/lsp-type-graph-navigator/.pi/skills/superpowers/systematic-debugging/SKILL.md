---
name: superpowers/systematic-debugging
description: Specialized capabilities and operational workflow for Semantic LSP & Code Knowledge Graph Navigator
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers/systematic-debugging

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `lsp-type-graph-navigator` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   git status
   ```
2. Execute core operations adhering to Codebase symbol maps, blast radius impact reports (`docs/architecture/impact-*.md`), call hierarchy traces, and semantic dependency graphs..
3. Run self-correction verification:
   ```bash
   Verifies that every symbol referenced in an impact report is confirmed via active LSP definition lookup (`lsp_goto_definition`) and cross-checked against the SCIP knowledge graph.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with lsp-type-graph-navigator boundaries.
- Exit code 0 required on all diagnostic commands.
