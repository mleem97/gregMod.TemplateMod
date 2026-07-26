# Template blueprints

All templates inherit `UNIFIED-REPOSITORY-STANDARD.md`. The structures below list the type-specific additions rather than repeating governance files in every section.

## Shared template foundation

Every template starts with:

```text
.github/
  CODEOWNERS
  dependabot.yml
  ISSUE_TEMPLATE/
  workflows/
.meyermedia/
  repository.yml
README.md
AGENTS.md
LICENSE or LICENSE.md
SECURITY.md
SUPPORT.md
CONTRIBUTING.md
CHANGELOG.md
.editorconfig
.gitattributes
.gitignore
docs/
  CI-CD.md
  TESTING.md
```

Public active templates additionally provide `.github/FUNDING.yml`, `SPONSORS.md`, release automation and a template initialization script.

## Governance and workflow templates

### `meyerMedia.CI.Workflows`

Purpose: reusable hardened CI/CD building blocks for every repository.

```text
.github/workflows/
  reusable-node.yml
  reusable-dotnet.yml
  reusable-python.yml
  reusable-rust.yml
  reusable-flutter.yml
  reusable-fivem.yml
  reusable-container.yml
  reusable-docs-policy.yml
  reusable-release.yml
  reusable-deploy.yml
actions/
  repository-policy/
  coverage-summary/
  artifact-metadata/
profiles/
  webapp.yml
  service.yml
  library.yml
  game-mod.yml
  infrastructure.yml
templates/
  AGENTS.md
  DESIGN.md
  SECURITY.md
  SUPPORT.md
  FUNDING.yml
schemas/
  repository-profile.schema.json
```

Key controls: immutable action pins, least privilege, OIDC, protected environments, dependency review, CodeQL, SBOM, checksums, attestations and build-once promotion.

### `meyerMedia.Repository.Template`

Purpose: minimal universal repository skeleton for types without a dedicated template.

Adds policy validation, docs linting, license detection, secret scanning and a no-op test placeholder that must be replaced before active status.

## greg / MelonLoader ecosystem

### `gregMod.TemplateMod`

Purpose: normal Data Center IL2CPP mod deployed to `Mods/`.

```text
src/<ModName>/
  Core/
  Features/
  Infrastructure/
  Patches/
  UI/
tests/
  Unit/
  Contract/
scripts/
  setup-dev.py
  build.*
  deploy.py
  package-release.py
references/
docs/
  ARCHITECTURE.md
  DESIGN.md          # when UI exists
  COMPATIBILITY.md
```

Coverage: 75/65 for testable core. Unity/IL2CPP calls are isolated behind adapters. CI performs public restore and template smoke tests; full builds use a protected private interop artifact.

### `gregPlugin.Template`

Purpose: early MelonLoader plugin deployed to `Plugins/`.

```text
src/<PluginName>/
  Bootstrap/
  Hooks/
  Pathing/
  Native/
  Infrastructure/
tests/
  Unit/
  LoaderSmoke/
```

Additional requirements: load-order documentation, fail-closed startup, no gameplay UI assumptions, safe native/Steam boundaries, plugin-directory deployment test.

### `gregCore.Module.Template`

Purpose: original reusable greg API/framework module.

```text
src/
  <Module>.Abstractions/
  <Module>.Core/
  <Module>.Il2CppAdapter/
examples/
  ExampleConsumer/
tests/
  Unit/
  Compatibility/
docs/
  API.md
  VERSIONING.md
  ARCHITECTURE.md
```

Coverage: 90/85 for public API and core logic. Unity-free core is mandatory. CI checks API compatibility and package contents.

### `gregLibs.Template`

Purpose: reproducible UserLib/dependency package such as MoonSharp.

```text
src/
  upstream/
  patches/
  adapter/
package/
  manifest.json
licenses/
  LICENSE-UPSTREAM
  NOTICE
scripts/
  fetch-upstream.py
  apply-patches.py
  build.*
  install-userlib.py
  package-release.py
tests/
  Unit/
  LoadSmoke/
UPSTREAM.md
```

Coverage applies to local patches/adapters, not vendored upstream code. Releases contain exact provenance, licenses, checksums and `UserLibs/` layout.

## Meyer Media web and Node.js

### `meyerMedia.mmui-Webapp.Template`

Purpose: default interactive product webapp.

```text
src/
  app/
  components/mmui/
  features/
  lib/
    env/
    logging/
    security/
    retrieval/
  server/
  styles/
tests/
  unit/
  integration/
  e2e/
public/
docs/
  DESIGN.md
  ARCHITECTURE.md
  PRIVACY.md
  THREAT-MODEL.md
```

Baseline: Next.js, strict TypeScript, pnpm, MMUI tokens, Zod, Vitest, Testing Library and Playwright. Database, auth, payments, PWA, AI and vector retrieval are opt-in modules. Coverage: 80/75.

### `meyerMedia.Next.Site.Template`

Purpose: landing page, portfolio, documentation or content site.

```text
src/
  app/
  components/
  content/
  styles/
public/
tests/
  accessibility/
  smoke/
docs/
  DESIGN.md
  CONTENT.md
```

No database or auth by default. CI emphasizes accessibility, metadata, broken links, visual smoke tests and performance/asset budgets.

### `meyerMedia.Next.SaaS.Template`

Purpose: transactional product with identity, billing, storage and background work.

```text
src/
  app/
  features/
  server/
    auth/
    db/
    jobs/
    storage/
    billing/
    retrieval/
packages/
  schemas/
  observability/
infra/
tests/
  unit/
  integration/
  e2e/
docs/
  DESIGN.md
  ARCHITECTURE.md
  THREAT-MODEL.md
  PRIVACY.md
  OPERATIONS.md
  DEPLOYMENT.md
```

Coverage: 85/80 for server/business logic, 80/75 overall. Database migrations are a separate deployment job. Hybrid retrieval defaults to PostgreSQL FTS plus pgvector when semantic search is enabled.

### `meyerMedia.Node.Service.Template`

Purpose: REST API, webhook consumer, worker or internal service.

```text
src/
  api/
  domain/
  application/
  infrastructure/
  observability/
  retrieval/
  index.ts
tests/
  unit/
  integration/
  contract/
openapi/
infra/
docs/
  ARCHITECTURE.md
  THREAT-MODEL.md
  OPERATIONS.md
```

Requires readiness/liveness probes, graceful shutdown, request limits, structured logs and non-root container. Coverage: 85/80.

### `meyerMedia.Node.Workspace.Template`

Purpose: pnpm/Turborepo platform.

```text
apps/
services/
packages/
infra/
tooling/
docs/
  ARCHITECTURE.md
  DESIGN.md
  DEPLOYMENT.md
  OPERATIONS.md
AGENTS.md
```

Each workspace boundary receives a nested `AGENTS.md`. CI runs affected validation and independent deployment jobs. Shared schemas and retrieval clients live in packages; vector engines remain service-owned.

### `meyerMedia.Node.Package.Template`

Purpose: npm library, SDK or client.

```text
src/
tests/
examples/
docs/
  API.md
  VERSIONING.md
```

ESM-first, explicit exports, declarations, compatibility matrix, `npm pack --dry-run`, trusted publishing with OIDC and provenance. Coverage: 90/85.

### `meyerMedia.Node.CLI.Template`

Purpose: administration, migration or automation CLI.

```text
src/
  commands/
  config/
  services/
  output/
tests/
  unit/
  integration/
  fixtures/
docs/
  COMMANDS.md
```

Requires deterministic exit codes, `--json`, `--quiet`, `--verbose`, `--dry-run`, signal-safe cleanup and platform testing. Coverage: 80/70.

### `meyerMedia.AI.Application.Template`

Purpose: AI assistant, agent platform, RAG application or model orchestration product.

```text
apps/
  web/
services/
  api/
  workers/
packages/
  prompts/
  schemas/
  retrieval/
  evaluation/
evals/
  datasets/
  fixtures/
infra/
docs/
  DESIGN.md
  ARCHITECTURE.md
  MODEL-CARDS.md
  EVALUATION.md
  PRIVACY.md
  THREAT-MODEL.md
```

Mandatory: model/provider abstraction, prompt/version tracking, offline evals, cost and latency budgets, redaction, tenant-aware retrieval, embedding-version migration and non-vector fallback. Coverage: application profile plus evaluation gates.

## FiveM

### `meyerMedia.FiveM.Resource.Template`

```text
fxmanifest.lua
shared/
  config.lua
  locale.lua
client/
server/
bridge/
  framework.lua
  inventory.lua
  voice.lua
locales/
tests/
scripts/
  validate-manifest.*
  package-release.*
docs/
  ARCHITECTURE.md
  SECURITY.md
```

Server-authoritative event validation, rate limiting and namespaced events are mandatory. Coverage: 75/65 for testable Lua modules plus manifest/resource smoke tests.

### `meyerMedia.FiveM.NUI.Template`

Adds:

```text
web/
  src/
  tests/
  package.json
  vite.config.ts
shared/contracts/
docs/DESIGN.md
```

Typed Lua/NUI messages, local assets, payload validation, focus cleanup, CSP where supported and deterministic `web/dist` packaging.

### `meyerMedia.FiveM.Loadscreen.Template`

```text
fxmanifest.lua
web/
  index.html
  src/
assets/
  audio/
  images/
client.lua
tests/
```

No gameplay framework dependencies. CI enforces accessibility, media budgets, referenced-file validation and release ZIP contents.

### `meyerMedia.FiveM.FrameworkBridge.Template`

Created only after adapters are used by multiple resources. Contains versioned QBCore/ESX/ox/inventory/voice adapters, contract tests and compatibility documentation.

## Browser and desktop

### `meyerMedia.BrowserExtension.MV3.Template`

```text
src/
  background/
  content/
  popup/
  options/
  offscreen/
  shared/
manifests/
  chromium.json
  firefox.json
tests/
  unit/
  browser/
scripts/
  package-browsers.*
docs/
  DESIGN.md
  PERMISSIONS.md
  PRIVACY.md
```

Coverage: 80/75 plus browser smoke tests. Permissions are minimized and audited in CI; Chromium ZIP and Firefox XPI are reproducible.

### `meyerMedia.Electron.AdminTool.Template`

```text
src/
  main/
  preload/
  renderer/
  shared/
tests/
  unit/
  e2e/
packaging/
docs/
  DESIGN.md
  ARCHITECTURE.md
  THREAT-MODEL.md
```

Strict context isolation, allow-listed typed IPC, no renderer Node access, secure updates and signed artifacts. Coverage: 80/75.

### `meyerMedia.DotNet.DesktopTool.Template`

```text
src/
  App/
  Domain/
  Application/
  Infrastructure/
  Platform/
tests/
  Unit/
  Integration/
  UI/
packaging/
docs/
  DESIGN.md
  ARCHITECTURE.md
```

For WPF, Avalonia, WinUI or cross-platform .NET tools. Domain logic stays UI-independent. Coverage: 85/80 core, 75/65 UI adapters.

## Automation, data and native tooling

### `meyerMedia.Python.Automation.Template`

```text
src/<package>/
  cli.py
  config.py
  services/
  adapters/
tests/
  unit/
  integration/
  fixtures/
pyproject.toml
uv.lock
```

Ruff, mypy, pytest, structured logging and typed configuration. Bot/AI profiles add provider adapters, evaluation and retrieval modules. Coverage: 80/70; critical libraries 90/85.

### `meyerMedia.PowerShell.WindowsTool.Template`

```text
src/<Module>/
tests/
  Unit/
  Integration/
scripts/
  Install-ScheduledTask.ps1
  Uninstall-ScheduledTask.ps1
docs/
  OPERATIONS.md
```

Advanced functions, `SupportsShouldProcess`, optional explicit elevation, Pester, ScriptAnalyzer and signed-release guidance. Coverage: 80/70 where measurable.

### `meyerMedia.Rust.Workspace.Template`

```text
crates/
  api/
  core/
  cli/
  ffi/
  example/
tests/
docs/
  ARCHITECTURE.md
  SAFETY.md
```

Workspace lint policy, cargo-nextest, cargo-deny, clippy, rustfmt, FFI safety and cross-compilation. Coverage target: 85% core where tooling is stable.

### `meyerMedia.Flutter.Client.Template`

```text
lib/
  app/
  features/
  core/
  data/
  design_system/
test/
integration_test/
docs/
  DESIGN.md
  PRIVACY.md
```

Riverpod, routing, secure storage, API abstraction, offline/cache policy, golden tests and platform builds. Coverage: 80/75 plus critical integration journeys.

### `meyerMedia.ReverseEngineering.Research.Template`

```text
research/
  notes/
  provenance/
  hashes/
scripts/
fixtures/
  generated/
  synthetic/
tests/
tools/
docs/
  SCOPE.md
  LEGAL.md
  METHODOLOGY.md
  REPRODUCIBILITY.md
UPSTREAM.md
```

No proprietary binaries, firmware or game assets are committed unless redistribution rights are explicit. Every input is identified by hash and provenance.

## Game and content specializations

### `meyerMedia.GMod.Addon.Template`

```text
lua/
  autorun/
  client/
  server/
  shared/
materials/
resource/
tests/
scripts/
  package-workshop.*
docs/
  ARCHITECTURE.md
```

Client/server trust boundaries, hook cleanup, convar validation and Workshop packaging are required.

### `meyerMedia.Unity.Tool.Template`

For standalone Unity/IL2CPP analysis or game utilities that are not MelonLoader mods. Separates editor/runtime tooling, external game references and redistributable artifacts.

### `meyerMedia.Static.Site.Template`

For legacy HTML, static themes and simple microsites. Includes HTML/CSS/JS linting, accessibility, link checking, CSP, asset optimization and deploy preview. Numeric coverage only applies to meaningful JavaScript logic.

### `meyerMedia.Theme.Template`

For CMS/application themes. Adds upstream-version compatibility matrix, visual regression tests, asset build pipeline and a clear separation from the upstream application.

### `meyerMedia.Profile.Template`

For the GitHub profile repository. Includes generated project index, current support/funding links, contact policy and automated stale-link checks; it does not need application coverage.

### `meyerMedia.AgentSkills.Template`

For reusable `AGENTS.md` instructions and agent skills.

```text
skills/<skill-name>/
  SKILL.md
  references/
  scripts/
schemas/
tests/
  fixtures/
docs/
  AUTHORING.md
```

Validation checks front matter, paths, examples, script safety and deterministic packaging.

## Infrastructure and upstream repositories

### `meyerMedia.Docker.ServiceStack.Template`

```text
compose.yml
compose.override.yml.example
services/
config/
infra/
scripts/
  backup.*
  restore.*
  update.*
  rollback.*
monitoring/
docs/
  ARCHITECTURE.md
  OPERATIONS.md
  DEPLOYMENT.md
  DISASTER-RECOVERY.md
```

Pinned images/digests, health checks, secret handling, backup restore tests and `docker compose config` validation.

### `meyerMedia.Server.Configuration.Template`

For PBX, game server, Linux host or appliance configuration. Uses declarative configuration, encrypted secrets, validation, inventory, backup and rollback. Raw server state is not committed.

### `meyerMedia.UpstreamFork.Template`

```text
UPSTREAM.md
PATCHES.md
SECURITY.md
SUPPORT.md
scripts/
  sync-upstream.*
  verify-patches.*
```

Preserves upstream layout and license. Local CI validates patches without pretending the repository is an original Meyer Media product. Sponsoring points to upstream unless local work has a separate, clearly described funding scope.

### `meyerMedia.Archive.Template`

Archived repositories receive a final README banner, reason, replacement link, last supported version, license clarification and disabled deployment workflows. Security contacts remain only when releases are still distributed.

## Retrieval modules by template

| Template family | Default | Optional semantic layer |
| --- | --- | --- |
| Next Site / static content | static index or lexical search | hosted search only when corpus justifies it |
| MMUI Webapp / SaaS | PostgreSQL FTS + GIN/trigram | pgvector HNSW and hybrid ranking |
| Node Service / Workspace | domain-owned relational/search index | Qdrant or OpenSearch for dedicated high-throughput retrieval |
| AI Application | hybrid lexical + vector | Qdrant for vector-centric multi-tenant scale; OpenSearch for search-centric systems |
| Infrastructure/log platform | labels and structured query | OpenSearch or ClickHouse for logs/events; vectors only for semantic incident search |
| Mod store/catalog | exact metadata filters + lexical search | pgvector/Qdrant for semantic discovery and recommendations |
| Local desktop/CLI | SQLite/FTS or in-memory index | local vector index only for offline semantic workflows |

Vector choice must follow benchmarks and the rules in `UNIFIED-REPOSITORY-STANDARD.md`; no template adds a vector database as an unused default dependency.
