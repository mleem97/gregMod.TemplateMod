# Portfolio template analysis

This analysis groups the accessible `mleem97` repositories by recurring architecture, build system, and operational workflow. Empty repositories and near-upstream mirrors are excluded from template priority unless they reveal a repeated maintenance pattern.

## Recommended template roadmap

### 1. `gregPlugin.Template` — highest priority

Evidence: `gregPluginAssetExporter`, `gregPluginLangCompatBridge`, `gregPluginMultiplayer`, `gregPluginPlayerModels`, `gregPluginSysadmin`, `gregPluginWebUIBridge`, `gregModPathRedirector`, and `gregConsoleInputGuard`.

Purpose:

- MelonLoader plugin rather than normal mod lifecycle
- early/preload execution
- loader and workshop path handling
- no gameplay UI assumptions
- safe native/Steam API boundaries
- plugin deployment into `Plugins/`

This must remain separate from `gregMod.TemplateMod` because load order, failure impact, and deployment location differ.

### 2. `gregCore.Module.Template` — highest priority

Evidence: `gregCore`, `GregFramework`, `FrikaModFramework`, `gregRef`, `LuaLoader`, and modules that integrate with the shared framework.

Purpose:

- versioned public API surface
- compatibility contracts and deprecation policy
- package/reference export
- unit-testable services isolated from Unity
- optional IL2CPP adapter project
- API documentation and example consumer

### 3. `Next.SaaS.Template` — high priority

Evidence: `gregWeb.Modstore`, `lnxr-whm`, `lnxr-whmcs`, `lnxr-mm-ui`, `hornflix`, `cloud-drive`, `cus-svh-webapp`, and similar authenticated dashboards.

Purpose:

- Next.js App Router and TypeScript
- PostgreSQL with Drizzle migrations
- authentication/passkeys and RBAC
- Redis jobs/cache
- S3-compatible object storage
- email, OpenAPI, Docker Compose, health checks
- environment validation and production deployment

### 4. `Next.Site.Template` — high priority

Evidence: `djmleem-next`, `portfolio-mleem`, `lnxr-comingsoon`, `lnxr-blog`, `greggorpages`, `meyer-hotel`, and lightweight landing or content sites.

Purpose:

- Next.js, React, Tailwind, metadata/SEO
- content and localization conventions
- static-friendly deployment
- accessibility, performance budgets, and analytics abstraction

Keep this smaller than the SaaS template.

### 5. `BrowserExtension.MV3.Template` — high priority

Evidence: `goatEQ`, `git-kanban-enhanced-extension`, and browser automation projects such as `Autolingo`.

Purpose:

- Chromium Manifest V3 service worker
- optional offscreen document
- Firefox-specific background implementation
- typed message contracts
- permission minimization
- Chrome ZIP and Firefox XPI packaging
- browser API mocks and automated tests

### 6. `Docker.ServiceStack.Template` — high priority

Evidence: `zammad-docker-compose`, `Shitcloud-Infra`, `deploy`, `mleem-jellyfin`, `MariaDBAutobackup`, PBX/server repositories, and hosted application stacks.

Purpose:

- Compose profiles and pinned images
- `.env.example` with validation
- health checks and dependency conditions
- reverse proxy/TLS integration
- backup and restore scripts
- secrets, volumes, update and rollback procedures
- CI validation with `docker compose config`

### 7. `Electron.AdminTool.Template` — medium-high priority

Evidence: `mvnet_ufw_manager`, `LabelManager`, `mm-gitManager`, and desktop administration utilities.

Purpose:

- Electron + Vite + React + TypeScript
- strict main/preload/renderer separation
- typed and allow-listed IPC
- secure defaults (`contextIsolation`, no renderer Node access)
- packaging, auto-update, logging, and platform release matrix

### 8. `TypeScript.SDK.Template` — medium priority

Evidence: `paywise-api` and reusable API/client tooling.

Purpose:

- ESM/CJS and declaration output
- Jest/Vitest tests and ESLint
- API error model and retry abstraction
- semantic-release and npm provenance
- generated changelog and package-size checks

### 9. `Python.Automation.Template` — medium priority

Evidence: `RushBot`, `RR_BOT_AI`, `frika-fba-finder`, `ml-aimanager`, firmware/research helpers, and data-processing utilities.

Purpose:

- `pyproject.toml` with `uv` or pip-tools lock workflow
- Ruff, mypy, pytest, structured logging
- CLI entry points and configuration validation
- optional Docker image and scheduled workflow
- reproducible model/data dependency handling

### 10. `PowerShell.WindowsTool.Template` — medium priority

Evidence: `AudioAffinityOptimizer`, `Win11ActivateAdmin`, backup and Windows administration scripts.

Purpose:

- advanced function layout with `SupportsShouldProcess`
- automatic elevation as an explicit optional helper
- Pester tests and ScriptAnalyzer
- transcript/logging conventions
- Task Scheduler installation and removal scripts
- signed-release guidance

### 11. `Rust.Workspace.Template` — conditional priority

Evidence: `DataCenter-RustBridge` already uses a multi-crate workspace with API, macros, example modules, multiplayer, networking, and protocol crates.

Create this template if further Rust bridge or native tooling projects are planned. Include workspace lint policy, cargo-nextest, cargo-deny, cross-compilation, FFI safety rules, and release profiles.

### 12. `Flutter.Client.Template` — conditional priority

Evidence: `hornflix_app` demonstrates a Flutter client with HTTP, secure storage, Riverpod, routing, caching, and media playback.

Only promote this to a maintained template after a second active Flutter application appears. One repository alone does not yet justify the maintenance cost.

### 13. `ReverseEngineering.Research.Template` — conditional priority

Evidence: `Il2CppAssemblyFixer`, `dataCenter.UnityExplorer`, `apeman_firmware_research`, and loader/bridge experiments.

Purpose:

- strict binary-fixture exclusion
- hashes and provenance records
- reproducible analysis scripts
- legal/scope notes
- sample-data generation instead of committed proprietary firmware or game binaries

## Suggested creation order

1. `gregPlugin.Template`
2. `gregCore.Module.Template`
3. `Next.SaaS.Template`
4. `BrowserExtension.MV3.Template`
5. `Docker.ServiceStack.Template`
6. `Next.Site.Template`
7. `Electron.AdminTool.Template`
8. `TypeScript.SDK.Template`
9. `Python.Automation.Template`
10. `PowerShell.WindowsTool.Template`

Rust, Flutter, and reverse-engineering templates should follow only when another active project confirms repeated use.

## Consolidation opportunities

- Retire or archive the older `gregMod.Template` after consumers move to `gregMod.TemplateMod`.
- Use one shared `gregPlugin.Template` for the small plugin repositories instead of maintaining copied loader boilerplate.
- Separate lightweight sites from production SaaS dashboards to avoid unnecessary databases and infrastructure in small projects.
- Standardize release automation across TypeScript libraries, browser extensions, PowerShell tools, and mods.
- Centralize infrastructure conventions—health checks, backup/restore, secrets, and image pinning—in the Docker template.
