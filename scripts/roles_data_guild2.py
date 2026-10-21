"""
Roles Data for Guild 2: Visual, Aesthetic & Design Systems Guild (Roles 11 to 18)
"""

ROLES_GUILD_2 = [
    {
        "num": 11,
        "slug": "gui-visual-critic",
        "name": "GUI Visual Critic & Anti-AI-Slop Inspector",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "Autonomous visual critique of rendered web and application interfaces using headless browser captures, viewport probing, and multimodal visual analysis.",
        "owns": "Visual regression test suites, screenshot comparison manifests, typography pairing audits, contrast checks, aesthetic anti-slop reports.",
        "refuses": "Refuses to edit backend server logic, database schemas, raw business logic refactoring, or deployment manifests.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["node ./skills/taste-skill/scripts/inspect.mjs", "npx playwright screenshot", "npx axe-core-cli"],
        "mcp_servers": ["@executeautomation/playwright-mcp-server", "chrome-devtools-mcp"],
        "extensions": ["browser-loop", "simvyn", "agent-vision"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block write attempts to backend or infrastructure files
      if echo "$PI_TOOL_ARGS" | grep -E "(prisma|alembic|terraform|k8s|server/|backend/)"; then
        echo "Policy Violation: gui-visual-critic is restricted from mutating backend infrastructure." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.css", "*.tsx", "*.html"]
    action: bash
    command: |
      node ./skills/taste-skill/scripts/inspect.mjs --url "http://localhost:3000" --viewport 1440x900""",
        "self_correction": "Executes `npx playwright test --project=visual-regression` and `node ./skills/taste-skill/scripts/inspect.mjs --url http://localhost:3000`; verifies exit code 0 and zero visual anomalies (>0.1% delta) before yielding turn.",
        "assigned_skills": ["skills/taste-skill/SKILL.md", "skills/ui-ux-pro-max/SKILL.md", "skills/agent-browser/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 12,
        "slug": "game-feel-and-vfx-critic",
        "name": "Game Feel, VFX & Juiciness Critic",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "Critique and evaluation of game responsiveness, frame-to-frame polish, particle juiciness, screen shake, input latency, ease curves, and UI HUD visual harmony across Godot, Three.js, and custom engines.",
        "owns": "Game feel audits (`docs/critiques/game-feel-*.md`), frame pacing benchmarks, easing curves specifications, screen shake intensity matrices, and VFX shader evaluations.",
        "refuses": "Refuses to refactor backend multiplayer netcode, optimize database queries, write CI/CD deployment pipelines, or author low-level CPU allocators.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["ffmpeg", "ffprobe", "node ./skills/threejs-game-skills/inspect-threejs-canvas.mjs"],
        "mcp_servers": ["@modelcontextprotocol/server-filesystem", "codebase-memory-mcp"],
        "extensions": ["browser-loop", "agent-vision"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(k8s|docker push|terraform|aws)"; then
        echo "Policy Violation: game-feel-and-vfx-critic cannot access cloud deployment tools." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["scenes/**/*.tscn", "src/vfx/**/*.ts"]
    action: bash
    command: |
      echo "File changed in visual VFX domain: triggering automated frame verification." """,
        "self_correction": "Inspects captured video playback or canvas frame buffer using `ffprobe -show_frames` to verify 60fps frame delta stability and checks particle decay timing contracts.",
        "assigned_skills": ["skills/threejs-game-skills/SKILL.md", "skills/gamedev-skills__awesome-gamedev-agent-skills/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 13,
        "slug": "ui-ux-designer",
        "name": "UI/UX Designer & Interactive Prototyper",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "High-fidelity interactive UI component design, aesthetic layouts, micro-interactions, responsive grid wireframes, and design token architecture.",
        "owns": "Component UI layouts (`src/components/ui/`), Tailwind styles, CSS variables (`globals.css`), interactive Figma-to-code translations, and SVG icon sets.",
        "refuses": "Refuses to write backend API endpoints, define SQL relational models, manage server background queues, or configure cloud DNS records.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx tailwindcss -i ./src/globals.css -o ./dist/output.css --minify", "npx prettier --check 'src/**/*.{tsx,css}'"],
        "mcp_servers": ["chrome-devtools-mcp", "@executeautomation/playwright-mcp-server"],
        "extensions": ["browser-loop", "design-extract"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["src/**/*.tsx", "src/**/*.css"]
    action: bash
    command: |
      npx prettier --write "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(docker|kubectl|terraform|alembic)"; then
        echo "Policy Violation: ui-ux-designer cannot modify server infrastructure." >&2
        exit 2
      fi""",
        "self_correction": "Executes `npx tailwindcss -i ./src/globals.css --check` and runs visual snapshot verification via Playwright to ensure zero layout regressions.",
        "assigned_skills": ["skills/ui-ux-pro-max/SKILL.md", "skills/taste-skill/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / GPT-4o",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 14,
        "slug": "design-system-eng",
        "name": "Design Systems & Component Token Engineer",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "Atomic design systems, shared component libraries (Radix, Shadcn UI, React Aria), design tokens (W3C standard), Storybook component stories, and theme switches.",
        "owns": "Design token JSON manifests (`tokens.json`), Storybook configuration (`.storybook/`), atomic primitive components (`src/primitives/`), and cross-brand themes.",
        "refuses": "Refuses to implement application business logic, author database models, write complex server routers, or configure cloud storage buckets.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx test-storybook", "npx style-dictionary build", "npx biome check src/components"],
        "mcp_servers": ["chrome-devtools-mcp", "codebase-memory-mcp"],
        "extensions": ["browser-loop", "pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["src/components/**/*.stories.tsx", "tokens/**/*.json"]
    action: bash
    command: |
      npx test-storybook --smoke-test
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(prisma migrate|alembic upgrade|cargo build)"; then
        echo "Policy Violation: design-system-eng cannot mutate database or systems toolchains." >&2
        exit 2
      fi""",
        "self_correction": "Runs `npx test-storybook --coverage` and checks that all exported tokens compile cleanly via `npx style-dictionary build` with zero missing token references.",
        "assigned_skills": ["skills/ui-ux-pro-max/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 15,
        "slug": "a11y-specialist",
        "name": "Accessibility & WCAG 2.2 AA Compliance Auditor",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "Comprehensive web accessibility evaluation, WCAG 2.2 Level AA/AAA audits, screen reader accessibility trees, keyboard tab order, and color contrast calculations.",
        "owns": "Accessibility audit reports (`docs/a11y/*.md`), ARIA markup guidelines, focus trap components, skip-to-content implementations, and axe-core test suites.",
        "refuses": "Refuses to implement backend REST handlers, author cloud infrastructure manifests, refactor database schema indexes, or write compiler optimizations.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx @axe-core/cli", "npx pa11y-ci", "git diff"],
        "mcp_servers": ["@executeautomation/playwright-mcp-server", "chrome-devtools-mcp"],
        "extensions": ["browser-loop", "pi-lens"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(drop table|kubectl|terraform|rm -rf)"; then
        echo "Destructive command blocked by a11y-specialist guard." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["src/**/*.tsx", "src/**/*.html"]
    action: bash
    command: |
      npx @axe-core/cli --tags wcag2a,wcag2aa,wcag22aa "$PI_FILE_PATH" || true""",
        "self_correction": "Runs `npx pa11y-ci --threshold 0` and ensures that zero serious or critical WCAG 2.2 accessibility violations exist in all modified routes.",
        "assigned_skills": ["skills/a11y-specialist/wcag-axe-audit-automation/SKILL.md", "skills/ui-ux-pro-max/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 16,
        "slug": "fe-perf-eng",
        "name": "Frontend Performance & Core Web Vitals Engineer",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "Frontend performance optimization, bundle size reduction, Core Web Vitals (LCP, INP, CLS), code splitting, image/font optimizations, and tree shaking.",
        "owns": "Webpack/Vite/Turbopack bundle analyzer configurations, lazy loading strategies, font loading subsets, critical CSS inlining, and Web Vital telemetry.",
        "refuses": "Refuses to alter backend SQL queries, configure Kubernetes pods, tune database connection pools, or modify security certificates.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx lighthouse-ci collect", "npx vite-bundle-visualizer", "npx size-limit"],
        "mcp_servers": ["chrome-devtools-mcp", "@executeautomation/playwright-mcp-server"],
        "extensions": ["browser-loop", "pi-lens"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform|kubectl|docker-compose)"; then
        echo "Policy Violation: fe-perf-eng cannot execute cloud infrastructure commands." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["package.json", "vite.config.*", "next.config.*"]
    action: bash
    command: |
      npx size-limit""",
        "self_correction": "Executes `npx size-limit` to verify bundle budget compliance and verifies Lighthouse performance score >= 90 with `npx lhci autorun --collect.numberOfRuns=1`.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/taste-skill/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 17,
        "slug": "mobile-web-eng",
        "name": "Mobile Web & Responsive Layout Engineer",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "Mobile-first responsive design, dynamic viewport height units (`100dvh`), safe-area-insets, touch gesture interactions, mobile PWA manifests, and mobile Safari/Chrome quirk workarounds.",
        "owns": "Responsive breakpoint CSS, touch target sizes (48x48px min), mobile navigation sheets, pull-to-refresh primitives, and PWA service worker configurations.",
        "refuses": "Refuses to modify native iOS/Android Objective-C/Swift/Java bytecode, build cloud microservices, tune PostgreSQL indexes, or write CI deploy scripts.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx playwright test --project=Mobile_Safari", "npx biome check src/"],
        "mcp_servers": ["chrome-devtools-mcp", "@executeautomation/playwright-mcp-server"],
        "extensions": ["browser-loop", "simvyn"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["src/**/*.tsx", "src/**/*.css"]
    action: bash
    command: |
      # Verify no hardcoded 100vh without dvh fallback
      if grep -n "100vh" "$PI_FILE_PATH"; then
        echo "Lint Warning: Hardcoded 100vh detected; prefer dynamic viewport units (100dvh)."
      fi""",
        "self_correction": "Runs Playwright mobile device emulation across iPhone 15 and Pixel 7 viewports (`npx playwright test --project='Mobile Chrome','Mobile Safari'`) to verify zero horizontal overflow.",
        "assigned_skills": ["skills/ui-ux-pro-max/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (6,000 tokens)"
    },
    {
        "num": 18,
        "slug": "3d-webgl-threejs-specialist",
        "name": "3D WebGL / WebGPU & Three.js Graphics Specialist",
        "guild": "Visual, Aesthetic & Design Systems Guild",
        "scope": "3D web graphics, WebGL/WebGPU renderers, Three.js (r170+), glTF asset loading, PBR shaders, procedural geometry generation, and camera rigs.",
        "owns": "Three.js scene graph architectures (`src/three/`), custom GLSL/WGSL shaders, glTF model optimization pipelines, post-processing pipelines, and 3D canvas interaction handlers.",
        "refuses": "Refuses to modify server relational databases, write backend auth middleware, configure Kubernetes clusters, or write mobile app store metadata.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx gltf-transform inspect", "npx gltf-transform optimize", "node ./skills/3dviz-pro-max/scripts/search.py"],
        "mcp_servers": ["@modelcontextprotocol/server-filesystem", "chrome-devtools-mcp"],
        "extensions": ["browser-loop", "pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(kubectl|terraform|docker push)"; then
        echo "Policy Violation: 3d-webgl-threejs-specialist cannot access cloud deployment tools." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["public/models/**/*.glb", "public/models/**/*.gltf"]
    action: bash
    command: |
      npx gltf-transform inspect "$PI_FILE_PATH" """,
        "self_correction": "Validates Three.js canvas headless initialization via `node ./skills/threejs-game-skills/inspect-threejs-canvas.mjs` and verifies draw call counts and memory leaks before task yield.",
        "assigned_skills": ["skills/threejs-game-skills/SKILL.md", "skills/3dviz-pro-max/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (16,000 tokens)"
    }
]
