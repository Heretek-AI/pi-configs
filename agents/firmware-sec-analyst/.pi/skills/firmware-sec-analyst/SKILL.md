---
name: firmware-sec-analyst
description: Specialized capabilities and operational workflow for Firmware & Embedded Binary Security Analyst
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: firmware-sec-analyst

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `firmware-sec-analyst` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   binwalk -e
   ```
2. Execute core operations adhering to Firmware security audit reports (`docs/firmware-audits/*.md`), Binwalk extraction manifests, binary security flag reports (`checksec.json`), and hardware interface vulnerability matrices..
3. Run self-correction verification:
   ```bash
   Executes `checksec --file=firmware.bin` and scans extracted filesystem trees for unencrypted private keys, cleartext passwords, and insecure telnet/ssh configurations.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with firmware-sec-analyst boundaries.
- Exit code 0 required on all diagnostic commands.
