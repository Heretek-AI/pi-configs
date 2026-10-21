---
name: wshobson__agents/kubernetes-manifests
description: Specialized capabilities and operational workflow for Kubernetes Platform & Helm Orchestrator
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: wshobson__agents/kubernetes-manifests

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `k8s-orchestrator` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   kubeconform -strict
   ```
2. Execute core operations adhering to Kubernetes YAML manifests (`k8s/**`), Helm charts (`charts/**`), `values.yaml`, HPA scaling policies, and pod disruption budgets..
3. Run self-correction verification:
   ```bash
   Validates all charts using `helm lint charts/*` and dry-runs manifest generation with `helm template test charts/* | kubeconform -strict -summary`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with k8s-orchestrator boundaries.
- Exit code 0 required on all diagnostic commands.
