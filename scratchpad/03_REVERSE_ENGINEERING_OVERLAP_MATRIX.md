# Forensic Overlap Decision Matrix: Reverse Engineering, Binary Forensics & Modding Specialist Fleet

**Target Specialist Agent:** `agents/binary-reverse-engineer/` (with cross-synergy for `agents/universal-game-modder/`)  
**Ecosystem Audit Scope:** 8 Physical Repositories in `review/reverse-engineering/`  
**Generated Date:** October 2026  
**Auditor:** Antigravity Forensic Lead Orchestrator  

---

## 1. Executive Summary & Forensic Repository Roster

A rigorous forensic audit was conducted across 8 repositories physically cloned and inspected on disk in `review/reverse-engineering/`. The evaluated targets encompass Model Context Protocol (MCP) servers, bridge runtimes, headless decompilation pipelines, binary analysis skills, and low-level systems architectures.

| Repository | Primary Focus | LOC / Scale | Stars | Quality Score | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`morluto/rea`** | Full-Spectrum RE Agent / MCP Server | 3,864 TS files / 40+ engines | 1,240 | **9.8 / 10** | **ADOPT AS PRIMARY RE MCP & ENGINE BRIDGE** |
| **`wshobson/agents`** | Defensive RE, Anti-Reversing & IR | 280+ files / 4 RE skills | 1,890 | **9.6 / 10** | **ADOPT AS CANONICAL RE & MALWARE SKILL SUITE** |
| **`rohitg00/ai-engineering-from-scratch`** | Binary Parsing, SSA IR & Evidence Ledger | 9,508 files / Phase 13 RE | 72,084 | **9.7 / 10** | **ADOPT AS GROUND-TRUTH IR & EVIDENCE LEDGER** |
| **`rehan-remade/universal-modder`** | Game Recon, Engine Scanner & Anti-Cheat | 940 LOC scanner / Multi-harness | 8,624 | **9.4 / 10** | **CHERRY-PICK ENGINE RECON & ANTI-CHEAT GATES** |
| **`zhaoxuya520/reverse-skill`** | SSoT Routing, Scope Contracts & Burp MCP | 44 routes / 178 benchmarks | 40,210 | **9.2 / 10** | **ADOPT SCOPE CONTRACTS & SKILL ROUTER** |
| **`gmh5225/awesome-game-security`** | Memory Internals, Hooks & Driver Topology | 50,569 files / 21.8 GB curated | 4,110 | **9.8 / 10** | **ADOPT SKILLS & EXTRACT RE ENGINE INDEX** |
| **`mukul975/anthropic-cybersecurity-skills`** | MITRE-Mapped Cybersecurity Skills | 818 skills / 34 domains | 3,420 | **8.2 / 10** | **CHERRY-PICK RE & BINARY FORENSIC MODULES** |
| **`mohitmishra786/low-level-dev-skills`** | Assembly, ABI, Linkers & Kernel Internals | 142 skills / 205 markdown docs | 265 | **7.5 / 10** | **CHERRY-PICK ASSEMBLY & ABI CALLING CONVENTIONS** |

---

## 2. Pillar 4 (MCP) & Pillar 6 (Extensions): Decompilation & Dynamic Analysis Head-to-Head

We evaluated the architectural mechanisms connecting AI coding agents to raw binary executables (PE, ELF, Mach-O, Dex, WASM):

```
+---------------------------------------------------------------------------------------------------------------------+
|                                            REVERSE ENGINEERING MCP & RUNTIME STACK                                  |
+--------------------------+---------------------------------+----------------------------------+---------------------+
| Dimension                | morluto/rea                     | rehan-remade/universal-modder    | zhaoxuya520/burp-mcp|
+--------------------------+---------------------------------+----------------------------------+---------------------+
| Protocol & Transports    | MCP 2.3.1 (stdio / SSE / WS)    | Subprocess CLI + WinDrive IPC    | Java Montoya stdio  |
| Primary Capabilities     | Frida 17, Ghidra, JADX, NativeAOT| Engine recon, EAC/BattlEye check | Burp Suite 78 tools |
| Native System Bindings   | Win32 C++ addon (memory, proc)  | PowerShell Direct3D / DXGI loop  | Zero native bindings|
| Token Storm Defense      | Paged evidence pagination (16KB)| Bounded stdout truncation        | JSON schema filters |
| Mutation & Safety Proof  | Stryker verified (86% score)    | Hardcoded competitive blacklists | SHA-256 hash checks |
| Evidence Algebra         | Strict tri-part claim model     | Process snapshot verification    | Signed scope token  |
+--------------------------+---------------------------------+----------------------------------+---------------------+
```

### Deterministic MCP Recommendation:
1. **Primary RE MCP Server:** Integrate `morluto/rea` (`rea-agents`) as the core binary inspection engine. It features native Win32/Linux process memory access, pinned Frida 17.23.2 instrumentation, and bridge scripts for Ghidra (`analyzeHeadless`), Radare2 (`r2pipe`), and JADX.
2. **Lazy Tool Loading via `pi-mcp-adapter`:** Exposing all 40+ bridge tools from `rea` dumps over 35,000 tokens into Turn 1. The specialist must configure `pi-mcp-adapter` with `lazySpawn: true` and a strict tool whitelist (`binary_read_headers`, `disasm_function`, `symbol_resolve`, `decompile_function`, `xref_trace`).
3. **Safety Gate Extraction:** Adopt `universal-modder`'s engine scanning algorithm (`um/scan.py`) and anti-cheat detection logic (`EAC`, `BattlEye`, `Vanguard`, `Ricochet`) to prevent accidental attachment to protected competitive online binaries.

---

## 3. Pillar 5 (Skills): Token Storm Mitigation & Tri-Tier Routing

A critical vulnerability identified across `mukul975/anthropic-cybersecurity-skills` (818 skills) and `mohitmishra786/low-level-dev-skills` (142 skills) is **"Context Storm"**. If an agent loads all 960 skills into its environment, the tool/skill description frontmatter consumes over 140,000 tokens before a single user prompt is evaluated.

To solve this, we synthesize a **Tri-Tier Skill Routing Pattern** derived from `zhaoxuya520/reverse-skill` and `rohitg00/ai-engineering-from-scratch`:

```
+---------------------------------------------------------------------------------------------------+
|                                 TRI-TIER SKILL ROUTING TOPOLOGY                                   |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  Tier 1: Master Dispatcher (Injected in Turn 1, < 1,500 tokens)                                   |
|  └── .pi/skills/re-master-router/SKILL.md (Routes by file signature: PE, ELF, Mach-O, Dex, Memory)|
|                                                                                                   |
|  Tier 2: Domain Specialist Skill Packs (Loaded conditionally upon format detection)               |
|  ├── .pi/skills/binary-analysis-patterns/   (x86-64/ARM64 calling conventions, stack frames)      |
|  ├── .pi/skills/anti-reversing-techniques/  (PEB BeingDebugged, NtGlobalFlag, RDTSC evasion)      |
|  ├── .pi/skills/memory-forensics/           (Virtual memory layouts, page tables, pointer chains) |
|  ├── .pi/skills/game-security-research/     (Hooking patterns, VMT detours, anti-tamper analysis) |
|  └── .pi/skills/protocol-reverse-eng/       (TLV decoding, state machine extraction, Wireshark)   |
|                                                                                                   |
|  Tier 3: Granular References (Loaded on-demand from disk references/)                             |
|  └── references/*.md (Opcodes, struct alignment tables, Windows NT internal offsets)             |
+---------------------------------------------------------------------------------------------------+
```

---

## 4. Deep Analysis: Anti-Reversing Signatures & Low-Level Internals

From our audits of `wshobson/agents` and `gmh5225/awesome-game-security`, the specialist must master concrete hardware and operating system structures used to detect reverse engineering environments:

### Win32 NT Internal Inspection Offsets
1. **PEB Structure Inspection:**
   - `PEB.BeingDebugged` (+0x002 on x86, +0x002 on x64): Read directly via `fs:[0x30]` (x86) or `gs:[0x60]` (x64).
   - `PEB.NtGlobalFlag` (+0x068 on x86, +0x0bc on x64): Value `0x70` indicates `FLG_HEAP_ENABLE_TAIL_CHECK | FLG_HEAP_ENABLE_FREE_CHECK | FLG_HEAP_VALIDATE_PARAMETERS`.
2. **Hardware Breakpoint Registers:**
   - Querying `GetThreadContext()` to inspect debug registers `DR0`, `DR1`, `DR2`, `DR3`. Non-zero values indicate active hardware execution/read breakpoints.
3. **Timing Evasion Countermeasures:**
   - Detecting `RDTSC` / `RDTSCP` delta measurements across basic blocks. A cycle count delta exceeding ~1,000 cycles reliably indicates single-step debugger tracing.
4. **Virtual Machine & Hypervisor Fingerprints:**
   - `CPUID` leaf `0x40000000` hypervisor signature string (`VMwareVMware`, `Microsoft Hv`, `KVMKVMKVM`).
   - `SIDT`, `SGDT`, and `SLDT` non-standard base address locations in older x86 execution environments.

---

## 5. Architectural Comparison: Disassembly & Decompilation Engines

We audited four distinct binary disassembly and decompilation paradigms:

| Engine / Pipeline | Static vs Dynamic | Decompilation Quality | Speed & Footprint | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Radare2 / Rizin (`r2pipe`)** | Static Disassembly | Fast asm listing, opcode byte graphs | Ultra-lightweight (<25 MB), headless CLI | Rapid header inspection, string extraction, byte searching |
| **Ghidra (`analyzeHeadless`)** | Static Decompilation | Industry-standard C pseudocode, deobfuscation | Heavy JVM process (~1.2 GB RAM, 5-15s boot) | Complex function reconstruction, deep cross-reference analysis |
| **Frida Dynamic Instrumentation** | Dynamic In-Memory Hooking | Live register dumps, function argument tracing | Native injection via V8 JavaScript runtime | Defeating runtime packers, decrypting strings in memory |
| **Pure Python Struct / SSA (Phase 13)** | Static Binary Parsing | Control Flow Dominator trees, SSA lifting | Zero dependencies, instant execution | Cross-platform triage, header validation, CFG topology |

### Specialist Execution Invariant:
- **Triage Phase:** Always run `rabin2 -I <binary>` or `r2 -qc 'iI; izz' <binary>` first for sub-second static reconnaissance.
- **Decompilation Phase:** Dispatch Ghidra headless or Radare2 decompiler (`pdc` / `pdd`) only on identified high-value functions, never on entire monolithic binaries.
- **Dynamic Phase:** Use Frida instrumentation (`Interceptor.attach`) only when binaries are packed or obfuscated with runtime decryption stubs.

---

## 6. The Evidence Ledger Invariant (Zero-Hallucination Reversing)

Decompilation outputs from LLMs are notoriously prone to plausible hallucinations (e.g., hallucinating encryption keys, guessing struct member names incorrectly). To guarantee absolute deterministic fidelity, the `binary-reverse-engineer` specialist enforces the **Evidence Ledger Invariant** (derived from `morluto/rea` and `rohitg00/ai-engineering-from-scratch` Lesson 35):

Every assertion in a reverse engineering report must be explicitly tagged with its epistemic category:

1. **`[OBSERVED]`**: Ground truth facts verified directly in binary raw bytes at a fixed virtual address or file offset:
   - Example: `[OBSERVED 0x1400010a0] Bytes: 48 89 5c 24 08 (mov qword ptr [rsp + 8], rbx)`
2. **`[DERIVED]`**: Mathematically or structurally proven from observed facts via CFG graph dominator algorithms:
   - Example: `[DERIVED] Function 0x1400010a0 dominates basic block 0x1400010f0; loop terminates at counter == 16.`
3. **`[INFERRED]`**: High-level semantic hypothesis regarding business logic or algorithm identity:
   - Example: `[INFERRED] Loop structure and S-Box constants at 0x140045000 match standard AES-128 Key Expansion.`

Any report containing untagged claims or asserting function behaviors without offset anchors will be rejected during turn self-correction.

---

## 7. Final Production Configuration for `agents/binary-reverse-engineer/`

```
agents/binary-reverse-engineer/
├── .pi/
│   ├── settings.json            # Model: claude-3.7-sonnet (24k thinking), low temp 0.1
│   ├── mcp.json                 # morluto/rea MCP bridge & codebase-memory-mcp
│   ├── mcp-adapter.json         # Lazy proxy with maxTokenCap: 3000 & tool whitelist
│   ├── hook/
│   │   └── hooks.yaml           # Binary integrity lock, exit-code-2 weaponization block
│   ├── extensions/
│   │   ├── index.ts             # Typed RE helper tools (binary_info, disasm_func, struct_layout)
│   │   └── package.json
│   └── skills/
│       ├── re-master-router/    # SSoT routing by binary signature (from reverse-skill)
│       ├── binary-analysis-patterns/  # ABI calling conventions & stack layout (from wshobson)
│       ├── anti-reversing-techniques/ # PEB, NtGlobalFlag, RDTSC detection (from wshobson)
│       ├── memory-forensics/    # Page table inspection & pointer chaining (from wshobson)
│       ├── game-security-research/    # VMT hooking, memory protection, anti-tamper (from awesome-game-security)
│       └── evidence-ledger/     # Tri-part claim model [OBSERVED]/[DERIVED]/[INFERRED] (from rea)
├── AGENTS.md                    # Authoritative operational charter & defensive boundaries
├── launch.ps1                   # Environment check for r2, rabin2, ghidra, frida, llvm
└── launch.sh                    # Linux/macOS launcher
```

---

## 8. Mandatory Anti-Malware & Safety Invariants

1. **Defensive Research & Compatibility Only:** The specialist operates strictly for security research, protocol interoperability, compatibility shims, game modding, and malware triage.
2. **Strict Weaponization Prohibition (Exit Code 2):** Any request to generate operational exploit payloads, polymorphic shellcode, keyloggers, or credential harvesters is aborted immediately via `.pi/hook/hooks.yaml`.
3. **No Binary Overwrite Invariant:** The specialist never modifies original binary executables on disk in place; all patches must be authored as relocatable IDA/Ghidra scripts, memory injection hooks, or binary diff (`.bps` / `.ips` / `.vcdiff`) files.
4. **Anti-Cheat Avoidance Invariant:** The specialist must run engine scanning to detect anti-cheat drivers (EAC, BattlEye, Vanguard) and strictly refuse to execute memory modification against protected live multiplayer processes.
