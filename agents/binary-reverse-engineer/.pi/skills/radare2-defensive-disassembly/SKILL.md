---
name: binary-reverse-eng/radare2-defensive-disassembly
description: Specialized capabilities and operational workflow for Binary Disassembly & Headless Decompilation Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: binary-reverse-eng/radare2-defensive-disassembly

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `binary-reverse-engineer` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   r2 -qc 'aaa; afl' binary
   ```
2. Execute core operations adhering to Decompilation analyses (`docs/re/*.md`), Ghidra project archives, Radare2 script recipes, recovered C function signatures, and struct memory layout reconstructions..
3. Run self-correction verification:
   ```bash
   Verifies that all recovered functions, cross-references (XREFs), and struct offsets are documented with byte-precise address anchors and verified in `rabin2 -E` or Ghidra MCP.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with binary-reverse-engineer boundaries.
- Exit code 0 required on all diagnostic commands.
