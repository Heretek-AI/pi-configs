---
name: cloud-platform-eng/opentofu-plan-and-validation
description: Specialized capabilities and operational workflow for Cloud Platform & OpenTofu / Infrastructure-as-Code Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: cloud-platform-eng/opentofu-plan-and-validation

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `cloud-platform-eng` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   tofu fmt -check
   ```
2. Execute core operations adhering to IaC configurations (`terraform/**`, `tofu/**`), module definitions, variable specifications (`variables.tf`), backend state manifests, and provider version pins..
3. Run self-correction verification:
   ```bash
   Runs `tofu validate && tflint && checkov -d .` to guarantee zero configuration syntax errors, zero deprecations, and zero critical security policy violations.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with cloud-platform-eng boundaries.
- Exit code 0 required on all diagnostic commands.
