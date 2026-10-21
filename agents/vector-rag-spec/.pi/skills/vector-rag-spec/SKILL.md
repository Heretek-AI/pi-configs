---
name: vector-rag-spec
description: Specialized capabilities and operational workflow for Vector Embeddings, Hybrid Search & RAG Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: vector-rag-spec

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `vector-rag-spec` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   python -m pytest tests/rag
   ```
2. Execute core operations adhering to Vector search schemas, collection configurations, chunking and indexing scripts (`rag/**`, `src/retrieval/**`), embedding model wrappers, and retrieval evaluation benchmarks..
3. Run self-correction verification:
   ```bash
   Runs RAG evaluation suite verifying context recall >= 0.85 and answer relevancy >= 0.90 across the golden evaluation test set (`pytest tests/rag/test_eval.py`).
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with vector-rag-spec boundaries.
- Exit code 0 required on all diagnostic commands.
