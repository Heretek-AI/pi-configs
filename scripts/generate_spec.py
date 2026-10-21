"""
Master Roster Specification Generator
Generates scratchpad/01_SPECIALIST_ROSTER_SPEC.md
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from roles_data_guild1 import ROLES_GUILD_1
from roles_data_guild2 import ROLES_GUILD_2
from roles_data_guild3 import ROLES_GUILD_3
from roles_data_guild4 import ROLES_GUILD_4
from roles_data_guild5 import ROLES_GUILD_5
from roles_data_guild6 import ROLES_GUILD_6
from roles_data_guild7 import ROLES_GUILD_7
from roles_data_guild8 import ROLES_GUILD_8

ALL_ROLES = (
    ROLES_GUILD_1
    + ROLES_GUILD_2
    + ROLES_GUILD_3
    + ROLES_GUILD_4
    + ROLES_GUILD_5
    + ROLES_GUILD_6
    + ROLES_GUILD_7
    + ROLES_GUILD_8
)

OUTPUT_PATH = r"C:\Users\derek\Desktop\Projects\pi-configs\scratchpad\01_SPECIALIST_ROSTER_SPEC.md"

def build_markdown():
    lines = []
    
    # Title & Metadata
    lines.append("# Master Specialist Roster Specification: 70 Ultra-Narrow Autonomous Agents")
    lines.append("**Platform**: `@mariozechner/pi-coding-agent` (v0.85+ / v1.0.0+ / v1.2.0+)")
    lines.append("**Orchestrator**: Native Worker RPC via `pi-agents-team` & `pi-subagents`")
    lines.append("**Safety & Guardrails**: `pi-yaml-hooks` (Deterministic Exit Code 2 Blocking)")
    lines.append("**Code Intelligence**: `@juvio15/pi-ast-grep`, `pi-lsp-adapter`, `CodeGraphContext`")
    lines.append("**Version**: Wave 4 Production Blueprint (October 2026)")
    lines.append("**Status**: 100% Complete - Zero Omissions, Fully Realized Hook & Tool Contracts")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 1: Executive Roster Overview
    lines.append("## 1. Executive Roster Overview")
    lines.append("")
    lines.append("### 1.1 Architectural Philosophy & The Local-First Principle")
    lines.append("This specification formally establishes the **Local Specialist Fleet** for `@mariozechner/pi-coding-agent`, replacing the monolithic Docker sidecar overhead of legacy multi-agent frameworks (such as Heretek-Crew under Paperclip/OpenCode) with ultra-narrow, self-contained local specialists.")
    lines.append("")
    lines.append("Key architectural invariants enforced across all 70 roles:")
    lines.append("1. **Principle of Least Privilege (PoLP)**: Every specialist operates within a hermetically sealed scope. Tools outside an agent's domain are strictly prohibited.")
    lines.append("2. **Deterministic Hook Interception**: Built on `pi-yaml-hooks`, any attempt by an agent to mutate out-of-scope files or execute prohibited bash commands is blocked prior to execution with bash exit code `2`.")
    lines.append("3. **Mandatory Self-Correction Protocol**: No specialist is permitted to yield its turn to the orchestrator or user until its domain-specific verification command suite passes with `exit code 0`.")
    lines.append("4. **Zero-Shim Native Subprocess RPC**: Agents are orchestrated natively via `pi-agents-team` and `pi-subagents` over JSON-RPC, eliminating fragile CLI wrappers.")
    lines.append("5. **Context Window Hygiene**: Utilizing `@juvio15/pi-ast-grep` and `pi-lsp-adapter`, agents perform syntax-tree searches and symbol resolutions rather than flooding context windows with multi-megabyte raw file dumps.")
    lines.append("")
    
    # Mermaid Diagram
    lines.append("### 1.2 Fleet Organization & Departmental Hierarchy")
    lines.append("")
    lines.append("```mermaid")
    lines.append("flowchart TD")
    lines.append('    subgraph G1 ["1. Executive, Product & Documentation (Roles 01-10)"]')
    lines.append('        R01["Role 01: exec-director"]')
    lines.append('        R02["Role 02: product-director"]')
    lines.append('        R03["Role 03: tpm-scrum-lead"]')
    lines.append('        R04["Role 04: system-architect"]')
    lines.append('        R05["Role 05: tech-docs-lead"]')
    lines.append('        R06["Role 06: ux-research-analyst"]')
    lines.append('        R07["Role 07: brand-copy-spec"]')
    lines.append('        R08["Role 08: api-spec-doc-specialist"]')
    lines.append('        R09["Role 09: creative-narrative-director"]')
    lines.append('        R10["Role 10: humanizer-and-tone-editor"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G2 ["2. Visual, Aesthetic & Design Systems (Roles 11-18)"]')
    lines.append('        R11["Role 11: gui-visual-critic"]')
    lines.append('        R12["Role 12: game-feel-and-vfx-critic"]')
    lines.append('        R13["Role 13: ui-ux-designer"]')
    lines.append('        R14["Role 14: design-system-eng"]')
    lines.append('        R15["Role 15: a11y-specialist"]')
    lines.append('        R16["Role 16: fe-perf-eng"]')
    lines.append('        R17["Role 17: mobile-web-eng"]')
    lines.append('        R18["Role 18: 3d-webgl-threejs-specialist"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G3 ["3. Core Language & Systems Engineering (Roles 19-28)"]')
    lines.append('        R19["Role 19: ts-node-fullstack"]')
    lines.append('        R20["Role 20: rust-systems-spec"]')
    lines.append('        R21["Role 21: go-backend-eng"]')
    lines.append('        R22["Role 22: python-backend-spec"]')
    lines.append('        R23["Role 23: cpp-lowlevel-eng"]')
    lines.append('        R24["Role 24: java-kotlin-eng"]')
    lines.append('        R25["Role 25: ios-mobile-spec"]')
    lines.append('        R26["Role 26: android-mobile-spec"]')
    lines.append('        R27["Role 27: embedded-rtos-firmware-eng"]')
    lines.append('        R28["Role 28: wasm-runtime-engineer"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G4 ["4. Game Engineering, Graphics & Modding (Roles 29-39)"]')
    lines.append('        R29["Role 29: game-systems-dev"]')
    lines.append('        R30["Role 30: graphics-shader-eng"]')
    lines.append('        R31["Role 31: engine-systems-eng"]')
    lines.append('        R32["Role 32: game-ai-dev"]')
    lines.append('        R33["Role 33: physics-sim-eng"]')
    lines.append('        R34["Role 34: tech-artist-pipeline"]')
    lines.append('        R35["Role 35: shader-transpiler-optimizer"]')
    lines.append('        R36["Role 36: godot-redot-architect"]')
    lines.append('        R37["Role 37: ue-unreal-engine-architect"]')
    lines.append('        R38["Role 38: universal-game-modder"]')
    lines.append('        R39["Role 39: memory-integrity-cheat-researcher"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G5 ["5. Architecture, Cloud & Infrastructure (Roles 40-46)"]')
    lines.append('        R40["Role 40: cloud-platform-eng"]')
    lines.append('        R41["Role 41: k8s-orchestrator"]')
    lines.append('        R42["Role 42: dba-specialist"]')
    lines.append('        R43["Role 43: cache-streaming-eng"]')
    lines.append('        R44["Role 44: sre-incident-eng"]')
    lines.append('        R45["Role 45: observability-eng"]')
    lines.append('        R46["Role 46: git-drift-coord"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G6 ["6. Quality Assurance & Verification (Roles 47-51)"]')
    lines.append('        R47["Role 47: e2e-browser-qa"]')
    lines.append('        R48["Role 48: api-contract-tester"]')
    lines.append('        R49["Role 49: load-stress-tester"]')
    lines.append('        R50["Role 50: sabotage-qa-tester"]')
    lines.append('        R51["Role 51: release-qa-officer"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G7 ["7. Defensive Security, Binary Forensics & AI Red-Teaming (Roles 52-58)"]')
    lines.append('        R52["Role 52: appsec-engineer"]')
    lines.append('        R53["Role 53: cloud-sec-auditor"]')
    lines.append('        R54["Role 54: binary-reverse-engineer"]')
    lines.append('        R55["Role 55: firmware-sec-analyst"]')
    lines.append('        R56["Role 56: threat-modeler"]')
    lines.append('        R57["Role 57: compliance-auditor"]')
    lines.append('        R58["Role 58: ai-red-teamer"]')
    lines.append("    end")
    lines.append("")
    lines.append('    subgraph G8 ["8. Data, Machine Learning & Code Hygiene (Roles 59-70)"]')
    lines.append('        R59["Role 59: data-pipeline-eng"]')
    lines.append('        R60["Role 60: vector-rag-spec"]')
    lines.append('        R61["Role 61: mlops-serving-eng"]')
    lines.append('        R62["Role 62: analytics-metrics-eng"]')
    lines.append('        R63["Role 63: synthetic-eval-benchmark-eng"]')
    lines.append('        R64["Role 64: ast-structural-refactorer"]')
    lines.append('        R65["Role 65: linter-formatter-enforcer"]')
    lines.append('        R66["Role 66: dependency-hygiene-lockfile-surgeon"]')
    lines.append('        R67["Role 67: dependency-patcher"]')
    lines.append('        R68["Role 68: lsp-type-graph-navigator"]')
    lines.append('        R69["Role 69: adversarial-diff-auditor"]')
    lines.append('        R70["Role 70: static-analysis-lead"]')
    lines.append("    end")
    lines.append("")
    lines.append("    R01 --> R02 --> R03 --> R04")
    lines.append("    R03 --> G2")
    lines.append("    R03 --> G3")
    lines.append("    R03 --> G4")
    lines.append("    R03 --> G5")
    lines.append("    R03 --> G8")
    lines.append("    G2 & G3 & G4 & G5 & G8 --> G6")
    lines.append("    G3 & G4 & G5 --> G7")
    lines.append("    G6 & G7 --> R51 --> R01")
    lines.append("```")
    lines.append("")
    
    # Master Summary Table
    lines.append("### 1.3 Master Summary Matrix (All 70 Roles)")
    lines.append("")
    lines.append("| # | Agent Slug | Display Name | Guild | Primary Tools / MCP | Model Tier | Thinking Level |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in ALL_ROLES:
        tools_summary = ", ".join(r["cli_tools"][:2] + r["mcp_servers"][:1])
        if len(tools_summary) > 45:
            tools_summary = tools_summary[:42] + "..."
        lines.append(f"| {r['num']:02d} | `{r['slug']}` | {r['name']} | {r['guild']} | `{tools_summary}` | {r['model_tier']} | {r['thinking_budget']} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Section 2: Detailed Specifications
    lines.append("## 2. Detailed Agent Specification Sheets (Roles 01 to 70)")
    lines.append("")
    lines.append("Every specialist defined below represents a production-ready, local configuration artifact. Each agent possesses explicit boundary definitions, automated hook interceptors, mandatory self-correction commands, and assigned skills.")
    lines.append("")
    
    for r in ALL_ROLES:
        lines.append(f"### Role {r['num']:02d}: {r['name']} (`{r['slug']}`)")
        lines.append(f"**Department / Guild**: {r['guild']}  ")
        lines.append(f"**Target Directory**: `agents/{r['slug']}/`  ")
        lines.append(f"**Recommended Model**: `{r['model_tier']}`  ")
        lines.append(f"**Reasoning / Thinking Budget**: `{r['thinking_budget']}`")
        lines.append("")
        
        # Domain Boundary
        lines.append("#### A. Domain Boundary & Operational Authority")
        lines.append(f"- **Precise Scope**: {r['scope']}")
        lines.append(f"- **What it OWNS**: {r['owns']}")
        lines.append(f"- **What it REFUSES to Touch**: {r['refuses']}")
        lines.append("")
        
        # Core Tool Matrix
        lines.append("#### B. Core Tool Matrix")
        lines.append(f"- **Native Pi Tools**: `{', '.join(r['native_tools'])}`")
        lines.append(f"- **Specialized CLI Tools**: `{', '.join(r['cli_tools'])}`")
        lines.append(f"- **MCP Servers**: `{', '.join(r['mcp_servers'])}`")
        lines.append(f"- **Extensions & Adapters**: `{', '.join(r['extensions'])}`")
        lines.append("")
        
        # Hooks & Safety
        lines.append("#### C. Hooks & Safety Policy (`hooks.yaml`)")
        lines.append("Enforced via `pi-yaml-hooks`. Any bash hook action returning exit code `2` immediately aborts pending tool execution:")
        lines.append("```yaml")
        lines.append(r['hooks_yaml'])
        lines.append("```")
        lines.append("")
        
        # Mandatory Self-Correction Protocol
        lines.append("#### D. Mandatory Self-Correction Protocol")
        lines.append(f"{r['self_correction']}")
        lines.append("")
        
        # Assigned Skills
        lines.append("#### E. Assigned Skills & Capabilities")
        for sk in r["assigned_skills"]:
            lines.append(f"- `{sk}`")
        lines.append("")
        lines.append("---")
        lines.append("")
        
    # Section 3: Wave 5 Batch Generator Architecture
    lines.append("## 3. Wave 5 Batch Generator Implementation Guide")
    lines.append("")
    lines.append("### 3.1 Directory Topology per Specialist (`agents/<slug>/`)")
    lines.append("For each specialist defined in this specification, Wave 5 automated batch generators will synthesize a fully self-contained directory under `agents/<slug>/` containing:")
    lines.append("```text")
    lines.append("agents/<slug>/")
    lines.append("|-- AGENTS.md               # Primary system prompt, operational charter, and DoD")
    lines.append("|-- hooks.yaml              # Declarative pi-yaml-hooks configuration with exit code 2 guards")
    lines.append("|-- prompts/                # Role-specific flat prompt templates and task recipes")
    lines.append("|   `-- init.md             # Initial context injection and activation prompt")
    lines.append("`-- skills/                 # Symlinks or copies of assigned skills from review/skills/")
    lines.append("```")
    lines.append("")
    lines.append("### 3.2 Automated Verification Standard")
    lines.append("Every generated agent profile must be validated using:")
    lines.append("1. `pi-yaml-hooks validate agents/<slug>/hooks.yaml` ensuring valid syntax and hook event mappings.")
    lines.append("2. Markdown linter verification over `AGENTS.md` to ensure zero broken skill links or missing sections.")
    lines.append("3. RPC mock invocation testing with `pi-agents-team` to verify that subagent instantiation succeeds with zero startup latency penalties.")
    lines.append("")
    lines.append("---")
    lines.append("**End of Specification**: 70/70 Specialists Fully Specified.")

    content = "\n".join(lines)
    return content

def main():
    print(f"Total roles loaded: {len(ALL_ROLES)}")
    if len(ALL_ROLES) != 70:
        print(f"ERROR: Expected 70 roles, got {len(ALL_ROLES)}")
        sys.exit(1)
        
    md_content = build_markdown()
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    file_size = os.path.getsize(OUTPUT_PATH)
    print(f"Successfully generated {OUTPUT_PATH}")
    print(f"File size: {file_size:,} bytes")
    print(f"Total lines: {len(md_content.splitlines()):,}")

if __name__ == "__main__":
    main()
