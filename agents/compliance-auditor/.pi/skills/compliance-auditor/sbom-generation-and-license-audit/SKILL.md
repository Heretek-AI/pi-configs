---
name: compliance-auditor/sbom-generation-and-license-audit
description: Specialized capabilities and operational workflow for SBOM, Software License & Regulatory Compliance Auditor
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: compliance-auditor/sbom-generation-and-license-audit

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `compliance-auditor` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   syft dir:. -o cyclonedx-json
   ```
2. Execute core operations adhering to SBOM manifests (`sbom.json`), license attribution ledgers (`THIRD_PARTY_LICENSES.md`), license violation scan reports, and regulatory compliance evidence logs..
3. Run self-correction verification:
   ```bash
   Runs `cargo deny check license` and `npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-3-Clause;ISC'`; verifies zero unapproved copyleft license infections in proprietary builds.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with compliance-auditor boundaries.
- Exit code 0 required on all diagnostic commands.
