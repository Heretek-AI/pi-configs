---
name: cloud-sec-auditor/iam-least-privilege-audit
description: Specialized capabilities and operational workflow for Cloud Security Posture & IAM Security Auditor
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: cloud-sec-auditor/iam-least-privilege-audit

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `cloud-sec-auditor` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   checkov -d .
   ```
2. Execute core operations adhering to Cloud security audit reports (`docs/security/cloud-audit-*.md`), Checkov / tfsec policies, IAM policy remediation diffs, and encryption-at-rest enforcement manifests..
3. Run self-correction verification:
   ```bash
   Runs `checkov -d . --compact --quiet` and `tfsec .`; verifies zero wildcard IAM permissions (`Action: *`, `Resource: *`) and zero unencrypted storage resources.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with cloud-sec-auditor boundaries.
- Exit code 0 required on all diagnostic commands.
