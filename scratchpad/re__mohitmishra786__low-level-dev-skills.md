# Forensic Audit: mohitmishra786/low-level-dev-skills
## 1. Target Metadata
- Repo URL / NPM URL: https://github.com/mohitmishra786/low-level-dev-skills / npx skills.sh: `mohitmishra786/low-level-dev-skills`
- Latest Commit Date / Publish Date: 2026-06-27 (Commit `bdc5847` - "Expand skill suite to 142 with bare-metal, kernel-dev, and systems coverage")
- Star Count / Forks / Issues: 265 stars / 30 forks / 4 issues (via GitHub CLI `gh repo view`)
- License: MIT License
- Pi Version Compatibility: High skill-level compatibility; skills follow the Anthropics `SKILL.md` format with YAML frontmatter, markdown instructions, command cheat sheets, and ASCII architecture diagrams. Directly consumable by `@earendil-works/pi-coding-agent` via `~/.pi/skills/` or `<project>/.pi/skills/`.

## 2. What They Claim To Do
`low-level-dev-skills` claims to be a curated suite of 142 AI agent skills for systems and low-level development across C/C++, Rust, Zig, GPU computing, bare-metal firmware, Linux kernel/driver development, computer architecture, compiler internals, HPC, observability, virtualization, and WebAssembly:
- Informs AI coding agents (Claude Code, Antigravity, Cursor, Codex) with expert guidance for compilers, debuggers, profilers, build systems, sanitizers, low-level programming, embedded development, and binary inspection.
- Targets common developer stumbling blocks: reading compiler-generated assembly output, understanding System V AMD64 vs ARM AAPCS vs RISC-V psABI calling conventions, diagnosing stack corruption, writing inline assembly, using SIMD intrinsics, tuning CPU cache utilization, and configuring microcontroller clock trees.
- Distributes skills via `skills.sh` / `npx skills add` with language-specific bundles:
  1. **C/C++ Toolchain Bundle**:
     - Compilers, debuggers, build systems, and profilers: `gcc`, `clang`, `llvm`, `msvc-cl`, `cross-gcc`, `pgo`, `cmake`, `make`, `ninja`, `meson`, `conan-vcpkg`, `static-analysis`, `gdb`, `lldb`, `core-dumps`, `linux-perf`, `valgrind`, `flamegraphs`, `strace-ltrace`, `heaptrack`, `sanitizers`, `fuzzing`, `elf-inspection`, `linkers-lto`, `binutils`, `dynamic-linking`, `assembly-x86`, `assembly-arm`, `interpreters`, `simd-intrinsics`, `memory-model`, `cpu-cache-opt`.
  2. **Rust Systems Bundle**:
     - Compiler, Cargo, debugging, profiling, FFI, cross-compilation, sanitizers, async, security: `rustc-basics`, `cargo-workflows`, `rust-debugging`, `rust-profiling`, `rust-ffi`, `rust-cross`, `rust-sanitizers-miri`, `rust-unsafe`, `rust-async-internals`, `rust-security`, `rust-no-std`, `rust-build-times`.
  3. **Zig Toolchain Bundle**:
     - Compiler, build system, C interop, debugging, cross-compilation, testing, comptime: `zig-compiler`, `zig-build-system`, `zig-cinterop`, `zig-debugging`, `zig-cross`, `zig-testing`, `zig-comptime`.
  4. **Embedded & RTOS Bundle**:
     - Real-Time OS, JTAG/SWD debug probes, linker scripts, embedded Rust, bare-metal: `freertos`, `zephyr`, `openocd-jtag`, `linker-scripts`, `embedded-rust`, `baremetal-startup`, `mmio-and-bit-manipulation`, `interrupts-and-exceptions-baremetal`, `gpio-baremetal`, `uart-serial-baremetal`, `spi-i2c-baremetal`, `dma-baremetal`, `stm32-baremetal`, `low-power-embedded`.
  5. **Bare-Metal & Silicon Bring-Up Bundle**:
     - Peripherals from datasheets, clock trees, interrupt vector tables, PWM, ADC/DAC: `baremetal-startup`, `mmio-and-bit-manipulation`, `interrupts-and-exceptions-baremetal`, `peripherals-from-datasheet`, `gpio-baremetal`, `uart-serial-baremetal`, `spi-i2c-baremetal`, `timers-pwm-baremetal`, `adc-dac-baremetal`, `dma-baremetal`, `stm32-baremetal`, `datasheet-and-refmanual-reading`, `bootloaders-embedded`, `low-power-embedded`.
  6. **Linux Kernel & Driver Development Bundle**:
     - Kernel architecture, memory management, concurrency, Device Tree, platform devices, char drivers, I2C/SPI bus drivers, advanced debugging, QEMU: `linux-kernel-architecture`, `kernel-memory-management`, `kernel-concurrency`, `device-tree`, `platform-device-model`, `writing-char-drivers`, `bus-drivers-i2c-spi`, `kernel-debugging-advanced`, `qemu-for-kernel-development`, `kernel-internals`, `device-drivers`.
  7. **Computer Architecture Fundamentals**:
     - CPU pipelines, memory hierarchy, cache coherency, virtual memory paging/TLB, branch prediction: `cpu-pipelines-and-hazards`, `memory-hierarchy-and-caches`, `virtual-memory-paging-and-tlb`, `abi-and-calling-conventions`, `branch-prediction-and-speculation`.
  8. **Observability, Profiling, & Hardening**:
     - Dynamic tracing, security mitigations: `ebpf`, `ebpf-rust`, `binary-hardening`, `linux-perf`, `valgrind`, `flamegraphs`, `strace-ltrace`, `heaptrack`, `intel-vtune-amd-uprof`, `hardware-counters`.
  9. **WebAssembly Systems Bundle**:
     - Compiling low-level code to Wasm: `wasm-emscripten`, `wasm-wasmtime`.

## 3. Forensic Code Reality (Proof of Work)
Forensic physical inspection of `review\reverse-engineering\low-level-dev-skills` reveals a massive, purely static markdown skill repository containing 205 markdown files, 142 individual `SKILL.md` definitions, and 29,206 lines of technical guidance organized across 25 categories:

### A. Categorized Skills Inventory (`skills/`)
The physical directory breakdown confirms exactly 142 skills:
1. **allocators** (2 skills): Custom memory allocators, bump/pool/arena allocation patterns.
2. **async-io** (3 skills): Modern Linux `io_uring` setup, epoll event loops, and asynchronous I/O architectures.
3. **baremetal** (14 skills): `baremetal-startup` (reset vector, VTOR, `.data`/`.bss` init), `mmio-and-bit-manipulation`, `interrupts-and-exceptions-baremetal`, `gpio-baremetal`, `uart-serial-baremetal`, `spi-i2c-baremetal`, `timers-pwm-baremetal`, `adc-dac-baremetal`, `dma-baremetal`, `stm32-baremetal`, `bootloaders-embedded`, `datasheet-and-refmanual-reading`, `low-power-embedded`, `peripherals-from-datasheet`.
4. **binaries** (4 skills): `binutils` (objdump, readelf, nm, strip), `dynamic-linking` (ELF PLT/GOT, rpath, LD_PRELOAD), `elf-inspection` (headers, sections, symbols), `linkers-lto` (Link-Time Optimization, linker scripts).
5. **build-systems** (9 skills): `cmake`, `make`, `ninja`, `meson`, `conan-vcpkg`, `bazel`, `build-acceleration` (ccache, distcc), `static-analysis`, `include-what-you-use`.
6. **compiler-internals** (7 skills): LLVM IR, Clang AST, SSA form, optimization passes, instruction selection, intermediate representations.
7. **compilers** (8 skills): `gcc`, `clang`, `llvm`, `msvc-cl`, `cross-gcc`, `pgo` (Profile-Guided Optimization), compiler diagnostics, and flag optimization matrices.
8. **computer-architecture** (5 skills): `abi-and-calling-conventions` (System V AMD64, ARM AAPCS, RISC-V psABI), `branch-prediction-and-speculation`, `cpu-pipelines-and-hazards`, `memory-hierarchy-and-caches` (L1/L2/L3 cache lines, false sharing), `virtual-memory-paging-and-tlb`.
9. **debuggers** (6 skills): `gdb` (breakpoints, watchpoints, python scripting), `lldb`, `core-dumps` (post-mortem analysis), rr record-and-replay debugging, remote gdbserver.
10. **embedded** (5 skills): `freertos` (task scheduling, queues, semaphores), `zephyr`, `openocd-jtag` (SWD, CMSIS-DAP, ST-Link), `linker-scripts` (MEMORY, SECTIONS, LMA vs VMA), `embedded-rust`.
11. **gpu** (6 skills): `cuda-basics`, `cuda-optimization`, `metal-shading-language`, `vulkan-compute`, `opencl`, `gpu-memory-architectures` (coalesced memory access, warp divergence).
12. **hpc** (3 skills): `openmp`, `mpi`, `numa-aware-programming` (numactl, libnuma).
13. **kernel** (5 skills): `kernel-internals`, `device-drivers`, `ebpf`, `linux-kernel-modules`, `system-calls`.
14. **kernel-dev** (9 skills): `linux-kernel-architecture` (boot flow, initcall levels), `kernel-memory-management` (kmalloc, vmalloc, slab/slub allocators), `kernel-concurrency` (spinlocks, mutexes, RCU), `device-tree` (DTS/DTB parsing), `platform-device-model`, `writing-char-drivers`, `bus-drivers-i2c-spi`, `kernel-debugging-advanced` (kgdb, ftrace), `qemu-for-kernel-development`.
15. **languages** (2 skills): C23 standards, modern C++20/C++23 features.
16. **low-level-programming** (9 skills): `assembly-x86` (AT&T vs Intel syntax, registers, stack frames), `assembly-arm` (AArch64 registers, condition codes), `assembly-riscv`, `simd-intrinsics` (AVX-512, Neon), `memory-model` (acquire/release semantics, memory barriers), `cpu-cache-opt` (data-oriented design), `cpp-coroutines`, `interpreters` (bytecode dispatch, register machines).
17. **observability** (2 skills): `ebpf-tracing` (bpftrace, kprobes, uprobes), `systemtap`.
18. **platform** (3 skills): POSIX primitives, Windows Win32 internals, macOS Darwin subsystems.
19. **profilers** (7 skills): `linux-perf` (perf record, perf report, hardware counters), `valgrind` (memcheck, callgrind), `flamegraphs`, `strace-ltrace`, `heaptrack`, `intel-vtune-amd-uprof`, `hardware-counters` (PMUs, IPC, cache misses).
20. **qemu** (4 skills): `qemu-system-emulation`, `qemu-embedded-simulation`, `qemu-for-kernel-development`, `qemu-user-mode`.
21. **runtimes** (5 skills): `sanitizers` (AddressSanitizer, ThreadSanitizer, MemorySanitizer, UBSan), `fuzzing` (libFuzzer, AFL++), `wasm-wasmtime`, `wasm-emscripten`.
22. **rust** (12 skills): `rustc-basics`, `cargo-workflows`, `rust-debugging`, `rust-profiling`, `rust-ffi`, `rust-cross`, `rust-sanitizers-miri`, `rust-unsafe`, `rust-async-internals`, `rust-security`, `rust-no-std`, `rust-build-times`.
23. **security** (2 skills): `binary-hardening` (PIE, RELRO, stack canaries, CET, FORTIFY_SOURCE), `spectre-meltdown-mitigations`.
24. **virtualization** (3 skills): KVM/QEMU hypervisor, cgroups v2/namespaces, firecracker.
25. **zig** (7 skills): `zig-compiler`, `zig-build-system`, `zig-cinterop`, `zig-debugging`, `zig-cross`, `zig-testing`, `zig-comptime`.

### B. Technical Code Proof of Work Across Key Subsystems

#### 1. Assembly & Calling Conventions (`assembly-x86` & `abi-and-calling-conventions`)
The x86-64 assembly guide covers register naming, stack alignment, and calling conventions:
```text
System V AMD64 Calling Convention:
  Argument Registers: %rdi (1st), %rsi (2nd), %rdx (3rd), %rcx (4th), %r8 (5th), %r9 (6th)
  Floating-point Args: %xmm0 - %xmm7
  Return Values: %rax (primary), %rdx (secondary / 128-bit)
  Callee-Saved Registers: %rbx, %rbp, %r12, %r13, %r14, %r15
  Stack Alignment: 16-byte alignment enforced prior to CALL instruction
  Red Zone: 128 bytes below %rsp available without stack allocation (Linux/BSD/macOS only; absent on Windows)
```
For ARM AAPCS (AArch64):
```text
AArch64 Register Assignments:
  General Arguments / Results: x0 - x7
  Indirect Result Location: x8
  Callee-Saved: x19 - x28
  Frame Pointer: x29 (fp)
  Link Register: x30 (lr)
  Stack Pointer: sp
```

#### 2. Linux Kernel Architecture (`linux-kernel-architecture`)
Documents kernel initialization flow and subsystem organization:
```text
Kernel Boot Sequence:
  Firmware/UEFI -> arch/*/boot (decompression) -> start_kernel()
  start_kernel(): mm_init(), sched_init(), trap_init(), init_IRQ(), time_init()
  rest_init() -> kernel_init thread -> run_init_process(/sbin/init or /init)
```
Subsystem mapping:
- Scheduler: `kernel/sched/` (`struct task_struct`, `struct sched_entity`)
- Memory Management: `mm/` (`struct page`, `struct mm_struct`, `struct vm_area_struct`)
- Virtual File System (VFS): `fs/` (`struct inode`, `struct dentry`, `struct file`, `struct super_block`)
- Networking: `net/` (`struct sk_buff`, `struct net_device`)

#### 3. Bare-Metal Reset Bring-Up (`baremetal-startup`)
Details the Cortex-M and RISC-V startup sequences:
- Reset vector table loading: `vector[0]` loaded into Main Stack Pointer (MSP), `vector[1]` branched to `Reset_Handler`.
- `Reset_Handler` implementation: loops to copy `.data` from flash LMA to SRAM VMA, zeroes out the `.bss` section in SRAM, configures the Vector Table Offset Register (VTOR), calls `SystemInit()`, and enters `main()`.

### C. Testing and Validation Infrastructure
- Unlike codebases with compiled test harnesses, `low-level-dev-skills` has:
  - `.markdownlint.json`: Basic formatting linting rules.
  - `.github/workflows/skill-review.yml`: Integrates Tessl Skill Review (`tesslio/skill-review@main`), which inspects markdown formatting on PRs.
  - `website/`: A static documentation catalog viewer built with vanilla HTML/CSS/JS (`index.html`, `script.js`, `style.css`).
  - **Critical Omission**: There is **no automated compilation or simulation test suite** validating that the C, C++, Assembly, or Linker Script snippets actually build or execute properly on real toolchains.

## 4. 6-Pillar Classification
The repository maps exclusively to the skills pillar:
- **1. Hooks**: None. No session hooks, tool guards, or execution wrappers.
- **2. LSP**: None. No Language Server configurations.
- **3. AST**: None. No AST parsers or structural transforms.
- **4. MCP**: None. Does not expose a Model Context Protocol server.
- **5. Skills**: Core Pillar (142 comprehensive systems, kernel, assembly, and toolchain markdown skills).
- **6. Extensions**: None.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 7.5/10 (High informational value; compromised by unvalidated hardware/linker bugs)
- **Technical Critique**:
  - *Unvalidated Code Snippets Cause Concrete Hardware & Linker Failures*:
    - **Issue #4 (STM32 Clock Overclocking)**: In `skills/baremetal/stm32-baremetal/SKILL.md` (Section "2. Clock configuration (RCC)"), the example sets SYSCLK to 168 MHz using an 8 MHz HSE with M=8, N=336, P=2. However, the configuration sets APB prescalers as:
      ```c
      RCC->CFGR |= RCC_CFGR_PPRE1_DIV2 | RCC_CFGR_PPRE2_DIV1 | RCC_CFGR_HPRE_DIV1;
      ```
      This makes APB1 run at 84 MHz and APB2 run at 168 MHz. According to the STM32F405/407 Reference Manual (RM0090), the maximum allowable frequency is **42 MHz for APB1** and **84 MHz for APB2**. The example severely overclocks the internal peripheral buses beyond silicon tolerance, causing peripheral malfunction and invalidating baud-rate calculations for USARTs on APB1. The correct prescalers must be `RCC_CFGR_PPRE1_DIV4` and `RCC_CFGR_PPRE2_DIV2`.
    - **Issue #6 (Linker Script Memory Overlap)**: In `skills/embedded/linker-scripts/SKILL.md` (Section "1. MEMORY and SECTIONS"), the minimal linker script omits runtime sections required by the C standard library (`newlib` / `newlib-nano`):
      ```ld
      SECTIONS {
          .text : { *(.text*) } > FLASH
          .data : AT(_etext) { *(.data*) } > RAM
          .bss  : { *(.bss*) } > RAM
      }
      ```
      When compiled with `arm-none-eabi-gcc -specs=nosys.specs`, the runtime injects `.init`, `.fini`, `.init_array`, and `.ARM.exidx`. Because these are omitted from the script, the linker places them as orphan sections in FLASH immediately after `.text`, colliding with the `AT(_etext)` load address of `.data`. The linker aborts with:
      ```text
      ld: section .init LMA [080012d4,080012df] overlaps section .data LMA [080012d4,08001823]
      collect2: error: ld returned 1 exit status
      ```
      This prevents any standard C/C++ firmware from linking.
    - **Issue #5 (Toolchain Documentation Inaccuracy)**: In `skills/embedded/openocd-jtag/SKILL.md`, ST-Link v2 is incorrectly documented under CMSIS-DAP examples rather than under the `interface/stlink.cfg` driver.
  - *Absence of Automated Verification*: Unlike repositories like `GodotPrompter` (which use automated Node test suites and syntax scanners to reject invalid APIs in CI), `low-level-dev-skills` relies entirely on manual documentation. Consequently, subtle hardware-specific and linker-specific bugs escape into the main branch.
  - *Exceptional Reference Value for Register & ABI Knowledge*: Despite snippet bugs, the conceptual value is immense. Having instant, structured lookup tables for System V AMD64 calling conventions, AArch64 registers, GDB python scripting, `io_uring` completion queues, and eBPF tracepoints provides exceptional context priming for agents working in C, C++, and Rust.

## 6. Community Feedback & Sentiment
- 265 stars, 30 forks, 4 issues.
- The community comprises skilled systems programmers and firmware engineers.
- Issues filed on GitHub (e.g., by contributor `ibrahim-siali`) are of extremely high technical quality, citing exact microcontroller datasheet registers (STM32 RM0090 clock tree) and linker LMA/VMA collisions.
- The project has gained steady adoption on `skills.sh` as the primary reference catalog for systems programming.

## 7. Verdict
**EXTRACT/CHERRY-PICK WITH AUDITING & CORRECTION**
- **Justification**: The repository contains an enormous wealth of systems programming knowledge (142 skills), but it should NOT be adopted wholesale without remediation due to known hardware overclocking bugs and broken linker scripts.
  1. Cherry-pick high-value, verified reference skills into the Pi-Configs catalog:
     - Assembly & ABI: `assembly-x86`, `assembly-arm`, `abi-and-calling-conventions`, `simd-intrinsics`, `memory-model`.
     - Toolchains & Binaries: `elf-inspection`, `binutils`, `dynamic-linking`, `linkers-lto`, `sanitizers`, `fuzzing`.
     - Debugging & Profiling: `gdb`, `lldb`, `linux-perf`, `valgrind`, `flamegraphs`, `core-dumps`.
     - Kernel & Async: `io_uring`, `linux-kernel-architecture`, `kernel-memory-management`, `ebpf`.
  2. Audit and correct the bare-metal skills before deployment:
     - Patch `skills/baremetal/stm32-baremetal/SKILL.md`: Change APB1 prescaler to `RCC_CFGR_PPRE1_DIV4` (42 MHz) and APB2 to `RCC_CFGR_PPRE2_DIV2` (84 MHz).
     - Patch `skills/embedded/linker-scripts/SKILL.md`: Add explicit `.init`, `.fini`, `.init_array`, and `.ARM.exidx` section placement to prevent newlib LMA overlap errors.
  3. Package the curated subset into a clean, audited `skills/systems/` directory for Pi.

## 8. Discovered Alternatives & Recommendations
- Upstream Target: https://github.com/mohitmishra786/low-level-dev-skills - 142 AI agent skills for low-level systems programming, compilers, kernel development, and bare-metal firmware.
- Related Alternative: https://github.com/morluto/rea - Flagship universal reverse engineering MCP server and agent skills with native binary decompilation.
- Related Alternative: https://github.com/redhat-et/ripwire - C++23 zero-dependency AST and blast-radius engine.
- Related Alternative: https://github.com/SignalWhisperer/cargo-mcp - Cargo toolchain and vulnerability scanning MCP server.
- Related Alternative: https://github.com/LaurieWired/GhidraMCP - Production Ghidra MCP server for binary decompilation and analysis.
- Appended to `scratchpad/followup.txt`: `[LOW-LEVEL / SYSTEMS] https://github.com/mohitmishra786/low-level-dev-skills - 142 curated systems programming, kernel, and assembly skills for AI coding agents.`
