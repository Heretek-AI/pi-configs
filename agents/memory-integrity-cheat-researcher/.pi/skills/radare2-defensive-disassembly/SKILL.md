---
name: radare2-defensive-disassembly
description: Specialized capabilities and operational workflow for Memory Integrity & Runtime Hooking Researcher
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: radare2-defensive-disassembly

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `memory-integrity-cheat-researcher` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   frida-compile
   ```
2. Execute core operations adhering to Memory signature definitions (`signatures/*.sig`), Frida hook scripts (`hooks/*.js`), pointer base offsets, and memory corruption regression proofs..
3. Run self-correction verification:
   ```bash
   Verifies that all Frida injection hooks compile cleanly without syntax errors using `frida-compile hooks/agent.js -o dist/agent.js` and validates signature uniqueness against memory dumps.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with memory-integrity-cheat-researcher boundaries.
- Exit code 0 required on all diagnostic commands.
