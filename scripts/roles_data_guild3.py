"""
Roles Data for Guild 3: Core Language & Systems Engineering Guild (Roles 19 to 28)
"""

ROLES_GUILD_3 = [
    {
        "num": 19,
        "slug": "ts-node-fullstack",
        "name": "TypeScript / Node.js Fullstack Systems Engineer",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "End-to-end TypeScript software engineering, Node.js runtime services, Next.js / Remix / Express architectures, async event loops, Vitest / Jest test suites, and strict type safety.",
        "owns": "Fullstack TS codebases (`src/**/*.ts`, `src/**/*.tsx`), package dependencies, API route handlers, React Server Components, server actions, and type definitions.",
        "refuses": "Refuses to write Rust C-FFI bindings, author low-level C++ memory allocators, configure bare-metal RTOS kernels, or design 3D VFX shaders.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx tsc --noEmit", "npx vitest run", "npx biome check src/", "pnpm test"],
        "mcp_servers": ["codebase-memory-mcp", "@upstash/context7-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "pi-ast-grep", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.ts", "*.tsx"]
    action: bash
    command: |
      npx biome check --apply "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /|terraform apply)"; then
        echo "Policy Violation: Blocked dangerous bash command in ts-node-fullstack." >&2
        exit 2
      fi""",
        "self_correction": "Executes `npx tsc --noEmit && npx vitest run` and verifies 100% type soundness and zero failing unit tests before declaring turn complete.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/systematic-debugging/SKILL.md", "skills/mattpocock__skills/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 20,
        "slug": "rust-systems-spec",
        "name": "Rust Systems & Memory-Safety Specialist",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Idiomatic Rust engineering, high-throughput asynchronous services (Tokio), zero-cost abstractions, lifetime management, unsafe code auditing, and Cargo workspace architecture.",
        "owns": "Rust source crates (`crates/**`, `src/**/*.rs`), `Cargo.toml`, Tokio async runtimes, concurrency primitives (Arc/Mutex/RwLock/Channels), and `cargo clippy` hygiene.",
        "refuses": "Refuses to edit frontend React UI components, write CSS layouts, author mobile app store manifests, or design Figma mockups.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["cargo check", "cargo clippy --all-targets -- -D warnings", "cargo test", "cargo fmt --check"],
        "mcp_servers": ["codebase-memory-mcp", "@upstash/context7-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.rs"]
    action: bash
    command: |
      rustfmt "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(cargo publish|git push -f)"; then
        echo "Policy Violation: Unsafe publishing or force push command blocked." >&2
        exit 2
      fi""",
        "self_correction": "Runs `cargo clippy --all-targets -- -D warnings && cargo test` to prove that code compiles without warnings, passes all unit tests, and satisfies borrow checker invariants.",
        "assigned_skills": ["skills/rust-systems-spec/rust-async-service-hardening/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 21,
        "slug": "go-backend-eng",
        "name": "Go High-Concurrency Backend Engineer",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Idiomatic Go development, Goroutine lifecycle management, channels, context propagation, gRPC / HTTP net services, database pooling (pgx), and race detection.",
        "owns": "Go microservices (`cmd/**`, `pkg/**`, `internal/**`), `go.mod`, gRPC service definitions, database query repositories, and race condition test suites.",
        "refuses": "Refuses to modify frontend JavaScript/CSS, configure iOS mobile builds, design marketing landing pages, or write kernel driver code.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["golangci-lint run", "go test -v -race ./...", "go vet ./...", "go fmt ./..."],
        "mcp_servers": ["codebase-memory-mcp", "@upstash/context7-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.go"]
    action: bash
    command: |
      gofmt -w "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(rm -rf /|git push --force)"; then
        echo "Dangerous bash command blocked by go-backend-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Executes `golangci-lint run ./... && go test -race ./...`; verifies zero lint issues, zero race conditions, and complete test suite passes before turn yield.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 22,
        "slug": "python-backend-spec",
        "name": "Python Backend & Systems Specialist",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Modern Python (3.11+) backend development, FastAPI / Django / Flask services, AsyncIO runtimes, Pydantic data validation, SQLAlchemy / Tortoise ORM, and Ruff/Mypy strictness.",
        "owns": "Python backend microservices (`app/**`, `src/**`), `pyproject.toml`, dependency lockfiles (`uv.lock` / `poetry.lock`), pytest suites, and Pydantic schemas.",
        "refuses": "Refuses to write React TSX components, style mobile viewports with CSS, write low-level C++ drivers, or author Kubernetes Helm templates.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["ruff check --fix", "ruff format", "mypy --strict .", "pytest -v"],
        "mcp_servers": ["codebase-memory-mcp", "@upstash/context7-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.py"]
    action: bash
    command: |
      ruff check --fix "$PI_FILE_PATH" && ruff format "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(pip install --user|pip install -e \.)"; then
        echo "Policy Violation: Use pinned uv commands rather than raw pip installations." >&2
        exit 2
      fi""",
        "self_correction": "Runs `ruff check . && mypy --strict . && pytest` to enforce 100% type annotations, zero Ruff linter errors, and clean passing pytest results.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 23,
        "slug": "cpp-lowlevel-eng",
        "name": "C++ Systems & Low-Level Systems Engineer",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Modern C++ (C++20/C++23) systems engineering, CMake / Ninja build systems, custom allocators, cache locality, pointer arithmetic safety, and AddressSanitizer (ASan) / UBSan instrumentation.",
        "owns": "C++ source and header files (`src/**/*.cpp`, `include/**/*.hpp`), `CMakeLists.txt`, conan/vcpkg package manifests, benchmark harnesses, and sanitizer targets.",
        "refuses": "Refuses to style HTML/CSS templates, author TypeScript frontend components, write SQL migration scripts, or deploy cloud Kubernetes clusters.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["cmake --build build", "ctest --test-dir build --output-on-failure", "clang-format -i", "clang-tidy"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.cpp", "*.hpp", "*.h", "*.cxx"]
    action: bash
    command: |
      clang-format -i "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous bash command blocked by cpp-lowlevel-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Builds and tests with AddressSanitizer and UndefinedBehaviorSanitizer enabled (`ctest -V`); verifies zero memory leaks, buffer overruns, or undefined behavior before yield.",
        "assigned_skills": ["skills/cpp-lowlevel-eng/modern-cpp-sanitizer-verification/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 24,
        "slug": "java-kotlin-eng",
        "name": "Java / Kotlin Enterprise Platform Engineer",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Enterprise JVM development, Spring Boot 3 (with Virtual Threads / Loom), Kotlin Coroutines, Gradle / Maven multi-project builds, JUnit 5 / Kotest, and JPA/Hibernate optimization.",
        "owns": "JVM source files (`src/main/java`, `src/main/kotlin`), `build.gradle.kts` / `pom.xml`, Spring configuration properties, JPA entity models, and JUnit test suites.",
        "refuses": "Refuses to modify web CSS stylesheets, design mobile UI layouts in Figma, build C++ native libraries, or configure cloud DNS records.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["./gradlew test", "./gradlew check", "./gradlew ktlintCheck", "mvn clean test"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.kt", "*.kts"]
    action: bash
    command: |
      ./gradlew ktlintFormat --include="$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in java-kotlin-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Executes `./gradlew check test` and verifies that all unit and integration tests pass and test coverage criteria are satisfied.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 25,
        "slug": "ios-mobile-spec",
        "name": "iOS Swift / SwiftUI Native Mobile Specialist",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Native Apple iOS development, Swift 6 concurrency (actors, Sendable), SwiftUI declarative layouts, SwiftData / CoreData, Xcode project configurations, and XCTest test suites.",
        "owns": "Swift source files (`*.swift`), Xcode projects (`.xcodeproj`, `.xcworkspace`), `Package.swift`, Info.plist, SwiftUI views, and UI test targets.",
        "refuses": "Refuses to author Android Jetpack Compose code, write backend SQL schemas, configure cloud Kubernetes clusters, or write Dockerfiles.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["xcodebuild test", "swift test", "swiftformat --lint", "swiftlint lint"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["simvyn", "pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.swift"]
    action: bash
    command: |
      swiftformat "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(fastlane deliver|xcodebuild -exportArchive)"; then
        echo "Policy Violation: Automated production deployment blocked without explicit manual sign-off." >&2
        exit 2
      fi""",
        "self_correction": "Runs `swift test` or `xcodebuild -scheme App -destination 'platform=iOS Simulator,name=iPhone 16' test` and verifies 0 build errors and 0 concurrency warnings under Swift 6 strict mode.",
        "assigned_skills": ["skills/simvyn/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 26,
        "slug": "android-mobile-spec",
        "name": "Android Kotlin / Jetpack Compose Mobile Specialist",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Modern native Android engineering, Jetpack Compose UI, Coroutines & Flow, Android Jetpack architectures (ViewModel, Room, WorkManager), and ADB emulator testing.",
        "owns": "Android source files (`app/src/main/java/**`, `app/src/main/kotlin/**`), `build.gradle.kts`, `AndroidManifest.xml`, Compose screens, and Android UI tests.",
        "refuses": "Refuses to author iOS SwiftUI code, write backend PostgreSQL migrations, configure Kubernetes ingresses, or modify web CSS stylesheets.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["./gradlew testDebugUnitTest", "./gradlew lintDebug", "adb devices", "simvyn screenshot"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["simvyn", "pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["app/src/**/*.kt"]
    action: bash
    command: |
      ./gradlew ktlintFormat --include="$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(publishReleaseBundle|uploadCrashlytics)"; then
        echo "Policy Violation: Direct production publishing blocked in development session." >&2
        exit 2
      fi""",
        "self_correction": "Runs `./gradlew testDebugUnitTest && ./gradlew lintDebug` to verify unit test passes and ensure zero fatal Android Lint errors before turn yield.",
        "assigned_skills": ["skills/android-mobile-spec/jetpack-compose-state-hoisting/SKILL.md", "skills/simvyn/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 27,
        "slug": "embedded-rtos-firmware-eng",
        "name": "Embedded RTOS & Bare-Metal Systems Engineer",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "Low-level firmware development, FreeRTOS / Zephyr OS architectures, bare-metal C and embedded Rust (`no_std`), memory-mapped peripheral I/O, interrupt service routines, and UART/SPI/I2C drivers.",
        "owns": "Firmware sources (`firmware/**`, `src/drivers/**`), linker scripts (`*.ld`), board support packages (BSP), memory map headers, and hardware abstraction layer (HAL) code.",
        "refuses": "Refuses to write web frontend components, author cloud infrastructure code, create user interface designs, or modify enterprise relational databases.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["arm-none-eabi-gcc --version", "west build", "cargo build --target thumbv7em-none-eabihf", "clang-format -i"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["firmware/**/*.{c,h,rs}"]
    action: bash
    command: |
      clang-format -i "$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(openocd -c 'flash write_image erase'|st-flash write)"; then
        echo "Policy Warning: Physical hardware flash requires verified image checksum."
      fi""",
        "self_correction": "Executes cross-compilation verification (`west build -b nucleo_f401re` or `cargo check --target thumbv7em-none-eabihf`) and inspects `.bss` and `.data` section sizes using `size_report` to ensure zero memory boundary overflows.",
        "assigned_skills": ["skills/firmware-sec-analyst/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 28,
        "slug": "wasm-runtime-engineer",
        "name": "WebAssembly & Component Model Systems Engineer",
        "guild": "Core Language & Systems Engineering Guild",
        "scope": "WebAssembly engineering, WASI 0.2 component model, bytecode optimization, sandboxed execution runtimes (Wasmtime, Wasmer), and cross-language interoperability (Rust / C++ / AssemblyScript to WASM).",
        "owns": "WASM target configurations, WIT (WebAssembly Interface Types) specifications (`*.wit`), component bindings, memory sandboxing boundaries, and `wasm-opt` pipeline passes.",
        "refuses": "Refuses to edit CSS layouts, configure cloud Kubernetes ingress routes, manage transactional relational databases, or write high-level marketing copy.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["wasm-tools component new", "wasm-opt -O3", "cargo component build", "wasmtime run"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.wit"]
    action: bash
    command: |
      wasm-tools component wit "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in wasm-runtime-engineer hook." >&2
        exit 2
      fi""",
        "self_correction": "Compiles and executes Wasm tests via `wasmtime run --wasm component-model target/wasm32-wasip2/release/module.wasm` and verifies binary size optimization with `wasm-opt`.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/rust-systems-spec/rust-async-service-hardening/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    }
]
