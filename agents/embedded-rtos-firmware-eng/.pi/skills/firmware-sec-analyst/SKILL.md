---
name: firmware-sec-analyst
description: Specialized capabilities and operational workflow for Embedded RTOS & Bare-Metal Systems Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: firmware-sec-analyst

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `embedded-rtos-firmware-eng` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   arm-none-eabi-gcc --version
   ```
2. Execute core operations adhering to Firmware sources (`firmware/**`, `src/drivers/**`), linker scripts (`*.ld`), board support packages (BSP), memory map headers, and hardware abstraction layer (HAL) code..
3. Run self-correction verification:
   ```bash
   Executes cross-compilation verification (`west build -b nucleo_f401re` or `cargo check --target thumbv7em-none-eabihf`) and inspects `.bss` and `.data` section sizes using `size_report` to ensure zero memory boundary overflows.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with embedded-rtos-firmware-eng boundaries.
- Exit code 0 required on all diagnostic commands.
