# Account-wide repository migration plan

Inventory basis: 130 repositories owned by `mleem97` found through the installed GitHub connection and owner search. The list should be regenerated before execution because repositories can be created, renamed or archived after this plan.

## Status codes

- **Migrate** — active repository; adopt the target profile in place
- **Consolidate** — move useful code/history/docs to the named canonical project, then archive
- **Fork** — retain upstream layout and apply the upstream-fork governance profile
- **Audit** — inspect manifests, ownership and current purpose before structural migration
- **Placeholder** — empty or near-empty; define scope within 30 days or archive
- **Template** — maintained source template; enable GitHub template mode manually

## Retrieval codes

- **None** — no vector/search service justified
- **Lexical** — static index, PostgreSQL FTS, GIN/trigram or domain indexes
- **Hybrid-PG** — lexical search plus pgvector/HNSW in the primary PostgreSQL system
- **Vector** — dedicated Qdrant/OpenSearch after benchmark and multi-tenant/filter design
- **Logs** — OpenSearch/ClickHouse for operational events; vectors only for semantic incident search
- **API** — retrieval is provided by the server; client does not own a vector database

## Installed-connection inventory

| Repository | Target profile/template | Plan | Retrieval |
| --- | --- | --- | --- |
| `garrysmod_load` | `meyerMedia.GMod.Addon.Template` | Audit whether this is a loadscreen/content pack; normalize assets and Workshop packaging or archive | None |
| `AudioAffinityOptimizer` | `meyerMedia.PowerShell.WindowsTool.Template` | Migrate; add Pester, ScriptAnalyzer, dry-run coverage and Task Scheduler install/uninstall | None |
| `MP3_Normalizer` | `meyerMedia.Media.Tool.Template` + .NET desktop profile | Migrate from .NET Framework where feasible; add generated audio golden tests and packaging | None |
| `LabelManager` | `meyerMedia.Flutter.Client.Template` | Migrate; add Riverpod boundaries, offline storage tests, privacy and design docs | Lexical; API later |
| `RushBot` | `meyerMedia.Python.Automation.Template` with bot/AI profile | Migrate; split bot, provider, retrieval and web concerns; remove large generated assets from Git | Hybrid-PG or Vector |
| `ToDo-Webapp` | `meyerMedia.mmui-Webapp.Template` | Migrate if maintained; otherwise mark as educational/archive | None |
| `MyGM` | `meyerMedia.PHP.Webapp.Template` | Consolidate feature inventory into `mygm-next`; freeze old Laravel/Vue system after migration | Hybrid-PG for rule content |
| `gmod-fres` | `meyerMedia.GMod.Addon.Template` | Migrate; add Lua lint, client/server trust rules and package validation | None |
| `mleem97` | `meyerMedia.Profile.Template` | Migrate; generate project index and verify support/funding links automatically | Lexical |
| `mleem_music-web` | `meyerMedia.Next.Site.Template` | Audit scope, then migrate or consolidate into `djmleem-next` | None |
| `Win11ActivateAdmin` | `meyerMedia.PowerShell.WindowsTool.Template` | Migrate; threat model privileged changes and add reversible tests | None |
| `MariaDBAutobackup` | `meyerMedia.Server.Configuration.Template` with PowerShell/shell profile | Migrate; add encrypted config, restore tests, retention policy and disaster-recovery docs | None |
| `my-gamemaster` | `meyerMedia.mmui-Webapp.Template` | Consolidate with `mygm-next` after comparing unique features | Hybrid-PG |
| `FrikaCreate` | `meyerMedia.Minecraft.Modpack.Template` | Migrate; exact mod manifest, licensing checks, deterministic CurseForge/Modrinth export | None |
| `mm_megaphone` | `meyerMedia.FiveM.Resource.Template` | Migrate; secure event validation, voice bridge contracts and resource ZIP CI | None |
| `mm_gploads` | `meyerMedia.FiveM.Loadscreen.Template` | Migrate; media budget, accessibility and deterministic asset manifest | None |
| `mm_affiliate` | `meyerMedia.FiveM.NUI.Template` | Migrate; typed NUI contracts, server-authoritative rewards and focus cleanup | None |
| `svhameln-mlm` | `meyerMedia.mmui-Webapp.Template` | Audit manifests and privacy requirements before migration | Lexical |
| `portfolio-mleem` | `meyerMedia.Next.Site.Template` | Consolidate with the preferred personal-site repository or migrate as canonical portfolio | None |
| `teacherbuddy` | `meyerMedia.mmui-Webapp.Template` | Migrate; retain Vitest coverage, add Playwright and privacy/offline documentation | Lexical; Hybrid-PG only for semantic materials |
| `UnburnableMeat` | `meyerMedia.RustOxide.Plugin.Template` | Migrate; generate single-file release from tested modules and validate config migration | None |
| `DeathcounterIP` | `meyerMedia.RustOxide.Plugin.Template` | Migrate; permission, language, persistence and unload/reload tests | None |
| `Rushbot-Web` | `meyerMedia.mmui-Webapp.Template` | Consolidate into a RushBot workspace if tightly coupled; otherwise maintain API contracts | API |
| `cus-svh-webapp` | `meyerMedia.Next.SaaS.Template` or `Node.Workspace.Template` | Migrate in phases; repository-size cleanup, service boundaries, threat model and protected deploy | Hybrid-PG; Vector if corpus/QPS requires |
| `RR_BOT_AI` | `meyerMedia.AI.Application.Template` | Migrate; provider abstraction, evals, tenant isolation, cost/latency budgets and RAG tests | Vector with lexical fallback |
| `svh_theme` | `meyerMedia.Theme.Template` | Migrate; upstream compatibility, visual regression and asset license inventory | None |
| `Legacy_HTML` | `meyerMedia.Static.Site.Template` or archive | Audit consumers; preserve as reference or modernize with static validation only | None |
| `lunexor-client-six` | `meyerMedia.Theme.Template` | Migrate as WHMCS/client-area theme; add upstream version matrix and screenshots | None |
| `lunexor-cart` | `meyerMedia.Theme.Template` | Migrate as cart/order-flow theme; add visual and upstream compatibility tests | None |
| `djmleem-next` | `meyerMedia.Next.Site.Template` | Migrate and choose as canonical DJ/music site where appropriate | Lexical |
| `PBX` | `meyerMedia.Server.Configuration.Template` | Migrate; declarative inventory, encrypted secrets, backup and rollback | None |
| `meyer-hotel` | `meyerMedia.Next.SaaS.Template` | Migrate; separate Prisma migrations from build, protect Stripe/auth flows, add E2E | Lexical |
| `lnxr-whm` | `meyerMedia.Node.Workspace.Template` | Migrate; affected CI, nested AGENTS, independent deploys and shared schemas | Hybrid-PG; OpenSearch for platform-wide search |
| `lnxr-comingsoon` | `meyerMedia.Next.Site.Template` | Migrate or consolidate into the main Lunexor site | None |
| `lnxr-blog` | `meyerMedia.Next.Site.Template` | Migrate; content schema, link checks, accessibility and static/FTS search | Lexical; optional Hybrid-PG |
| `animus-invoicing` | `meyerMedia.PHP.Webapp.Template` or fork profile | Audit whether original or upstream-derived; then migrate or mark as fork | Lexical |
| `eufy-robovac-g10-lidar` | `meyerMedia.ReverseEngineering.Research.Template` | Migrate; hashes, provenance, legal scope and synthetic fixtures | None |
| `apeman_firmware_research` | `meyerMedia.ReverseEngineering.Research.Template` | Migrate; remove redistributability ambiguity and add reproducible analysis scripts | None |
| `StackWise` | `meyerMedia.Node.Workspace.Template` | Migrate npm workspace to standard boundaries; add DB integration and frontend E2E coverage | Hybrid-PG for learning content |
| `animusfound_soon` | `meyerMedia.Next.Site.Template` | Migrate or consolidate into the final Animusfound site | None |
| `Autolingo` | `meyerMedia.BrowserExtension.MV3.Template` + fork profile if upstream-derived | Audit provenance; migrate permissions, browser tests and package builds | None |
| `talkndate` | `meyerMedia.Next.SaaS.Template` | Migrate; privacy/threat model, auth/media/realtime tests and protected migrations | Hybrid-PG for discovery; Vector only after fairness/privacy review |
| `paywise-api` | `meyerMedia.Node.Package.Template` | Migrate; exports map, compatibility tests, trusted npm publishing and provenance | None |
| `frika-fba-finder` | `meyerMedia.Python.Automation.Template` | Migrate; reproducible data sources, CLI tests and rate-limit/error handling | Lexical; optional Hybrid-PG |
| `mvnet_ufw_manager` | `meyerMedia.Electron.AdminTool.Template` | Migrate; secure IPC, restricted SSH, no renderer Node access and signed packages | None |
| `hornflix` | `meyerMedia.Node.Workspace.Template` / SaaS profile | Migrate; split apps/services/packages, harden media auth and deployment | Hybrid-PG; Vector for semantic catalog at scale |
| `mm-jlb` | `meyerMedia.mmui-Webapp.Template` + AI module | Migrate; preserve local-first privacy, add evals and offline/PWA E2E | Local lexical; optional local/API vector |
| `mleem-tapestop` | dedicated audio-plugin profile based on `Media.Tool.Template` | Migrate; CMake/JUCE matrix, DSP golden tests, benchmarks and signed VST3 release | None |
| `rosa-tarifverbund` | `meyerMedia.mmui-Webapp.Template` | Audit current stack and consolidate with `rosa.fis.app` if it is the successor | Lexical/API |
| `hornflix_app` | `meyerMedia.Flutter.Client.Template` | Migrate; client contract tests, secure storage, caching and media integration | API |
| `metin-cms` | `meyerMedia.PHP.Webapp.Template` | Audit maintenance; migrate with PHP quality gates or archive if replaced | Lexical |
| `mygm-next` | `meyerMedia.Next.SaaS.Template` | Make canonical MyGM product; migrate data/features from older MyGM repositories | Hybrid-PG for rules/documents |
| `MetinServer` | `meyerMedia.Server.Configuration.Template` | Placeholder: define server scope or archive | None |
| `Server` | `meyerMedia.Server.Configuration.Template` | Placeholder: rename to a specific service/server or archive | None |
| `invoiceninja` | `meyerMedia.UpstreamApplicationFork.Template` | Fork governance; document upstream SHA, patch queue and sync cadence | Upstream-defined |
| `invoiceninja-ui` | `meyerMedia.UpstreamApplicationFork.Template` / theme profile | Fork governance; isolate Meyer Media UI patches and visual tests | Upstream-defined |
| `zammad-docker-compose` | `meyerMedia.UpstreamApplicationFork.Template` + Docker profile | Preserve upstream; document local compose overrides and sync automation | Logs |
| `ach-glueck` | `meyerMedia.mmui-Webapp.Template` | Audit against `mm-ach-stack`; consolidate duplicate product surfaces | Hybrid-PG if product search exists |
| `lunexor-mailtools` | `meyerMedia.Next.SaaS.Template` | Migrate; protect integration vault, SSH agent and DNS apply/rollback flows | Lexical; Logs for DMARC events |
| `mleem-jellyfin` | `meyerMedia.Docker.ServiceStack.Template` or theme profile | Audit whether stack, branding or proxy; migrate the applicable subset | Lexical media metadata via Jellyfin |
| `gregIPAM` | archive profile | Consolidate remaining history/features into `gregMod.IPAM`, then archive | None |
| `FrikaModFramework` | `gregCore.Module.Template` | Placeholder/audit; merge with active framework if no independent API remains | None |
| `DC_MelonRedirect` | `gregPlugin.Template` | Placeholder; consolidate with `gregModPathRedirector` or archive | None |
| `gregModmanager` | `meyerMedia.DotNet.DesktopTool.Template` | Migrate; Avalonia test layers, signed installers, update provenance and privacy docs | Lexical catalog; API search |
| `gregCore` | `gregCore.Module.Template` | Migrate as canonical framework; API compatibility and 90/85 core coverage | Lexical metadata only |
| `gregConsoleInputGuard` | `gregPlugin.Template` | Migrate; loader smoke tests and safe input interception | None |
| `gregModGregifyEmployees` | `gregMod.TemplateMod` | Migrate; isolate testable transformation rules and add in-game smoke plan | None |
| `gregModPathRedirector` | `gregPlugin.Template` | Migrate; path threat model, rollback and early-loader tests | None |
| `gregPluginLangCompatBridge` | `gregPlugin.Template` | Migrate; compatibility matrix and contract fixtures | None |
| `gregPluginAssetExporter` | `gregPlugin.Template` | Migrate; output-path safety, asset license notices and smoke tests | None |
| `gregPluginMultiplayer` | `gregPlugin.Template` | Migrate; network protocol design, server authority and compatibility tests | None |
| `gregPluginPlayerModels` | `gregPlugin.Template` | Migrate; asset provenance, compatibility and cleanup tests | None |
| `gregPluginSysadmin` | `gregPlugin.Template` | Migrate; privileged action allow-list and threat model | None |
| `gregPluginWebUIBridge` | `gregPlugin.Template` | Migrate; authenticated local bridge, CSP/origin policy and typed contracts | None |
| `Il2CppAssemblyFixer` | `meyerMedia.ReverseEngineering.Research.Template` + .NET CLI profile | Migrate; binary provenance, synthetic fixtures and deterministic transformations | None |
| `deploy` | `meyerMedia.Docker.ServiceStack.Template` / server config | Audit and merge generic deployment logic into central workflow/infra repos | None |
| `gregMod.HexViewer` | `gregMod.TemplateMod` | Migrate; parser/core unit coverage and game adapter smoke tests | None |
| `gregMod.IPAM` | `gregMod.TemplateMod` | Migrate; make canonical IPAM mod and archive `gregIPAM` | None |
| `gregMod.StorageServer` | `gregMod.TemplateMod` | Migrate; storage logic tests, serialization compatibility and smoke tests | None |
| `src` | repository-standard audit | Identify ownership and purpose, rename/split into meaningful repositories, then archive `src` | None |
| `DataCenter-RustBridge` | `meyerMedia.Rust.Workspace.Template` | Migrate; cargo-nextest, cargo-deny, FFI safety and cross-platform release | None |
| `gregCableRemover` | `gregMod.TemplateMod` | Migrate; isolate selection/removal logic and add compatibility smoke tests | None |
| `datacentermods` | `meyerMedia.DataCatalog.Template` | Migrate; schema, hashes, duplicate/link checks and generated catalog docs | Lexical; Hybrid-PG for semantic mod discovery |
| `greggorpages` | `meyerMedia.Next.Site.Template` or Static Site | Migrate; use as branded error/static pages with asset and accessibility checks | None |
| `git-kanban-enhanced-extension` | Browser extension + upstream fork profile | Audit upstream divergence; either maintain with MV3 tests or archive | None |
| `gregMod.Template` | archive profile | Archive and point to `gregMod.TemplateMod` | None |
| `ml-aimanager` | `meyerMedia.AI.Application.Template` | Migrate; agent/eval/retrieval boundaries and protected provider secrets | Vector with lexical fallback |
| `mm-gitManager` | `meyerMedia.DotNet.DesktopTool.Template` | Migrate; domain/UI separation, deployment-provider contracts and UI tests | Lexical repository search |
| `LuaLoader` | `gregCore.Module.Template` with loader adapter | Audit upstream/ownership; modularize loader API and preserve third-party licenses | None |
| `dataCenter.UnityExplorer` | upstream fork + research profile | Preserve upstream history/license; document Data Center patches and release provenance | None |
| `GregFramework` | `gregCore.Module.Template` | Consolidate shared APIs into canonical `gregCore` unless independent compatibility requires it | None |
| `gregRef` | `gregCore.Module.Template` or DataCatalog | Audit whether code library or reference data; migrate accordingly | Lexical |
| `gregWeb.Modstore` | `meyerMedia.Next.SaaS.Template` | Migrate; catalog schemas, auth/storage/jobs and protected deployment | Hybrid-PG; Vector/Qdrant at catalog scale |
| `revphoenix` | `meyerMedia.Shell.LinuxTool.Template` | Migrate; Bats, ShellCheck, privilege allow-list, dry-run and recovery tests | None |
| `cloud-drive` | `meyerMedia.Next.SaaS.Template` | Migrate; object authorization, malware scanning, retention and audit events | Hybrid-PG; Vector for semantic file search |
| `DEMT` | `meyerMedia.Shell.LinuxTool.Template` + Docker profile | Migrate as `infractl`; isolate privileged shell core and optional web UI | Logs |
| `Shitcloud-Infra` | `meyerMedia.Docker.ServiceStack.Template` | Migrate; reduce committed runtime data, validate backup/restore and protected deploy | Logs via OpenSearch/ClickHouse |
| `GregFrameCord` | `meyerMedia.Node.Service.Template` with bot profile | Audit language/runtime, then migrate Discord event and command contracts | None; Vector only for knowledge bot |
| `RackBuilder` | `gregMod.TemplateMod` | Migrate urgently to remove absolute DLL paths; add UI `DESIGN.md` and core tests | None |
| `powerwich` | `meyerMedia.Proxy.Service.Template` | Migrate; target allow-list, header/timeout policy and integration tests | None |

## Additional owner-search inventory

| Repository | Target profile/template | Plan | Retrieval |
| --- | --- | --- | --- |
| `gregMod.Inventory` | `gregMod.TemplateMod` | Migrate; canonical inventory mod structure and game smoke tests | None |
| `mm-skills` | `meyerMedia.AgentSkills.Template` | Migrate; validate skill metadata, examples, scripts and deterministic bundles | Lexical |
| `gregWeb.LandingWiki` | `meyerMedia.Next.Site.Template` + DataCatalog | Migrate as docs/landing/wiki surface; generate navigation from schemas | Lexical |
| `mm-saas-dash-ui` | `meyerMedia.mmui-Webapp.Template` | Treat as MMUI dashboard reference/showcase; visual tests and `DESIGN.md` mandatory | None |
| `goatEQ` | `meyerMedia.BrowserExtension.MV3.Template` | Migrate Chromium/Firefox packaging, permissions, Web Audio tests and privacy docs | None |
| `lnxr-mm-ui` | `meyerMedia.Node.Workspace.Template` or MMUI Webapp | Audit whether platform or UI system consumer; align with canonical `mm-ui` | Lexical |
| `mm-ach-stack` | `meyerMedia.Node.Workspace.Template` | Make canonical ACH product stack if it supersedes `ach-glueck` | Hybrid-PG |
| `gregMod.NoEOL` | `gregMod.TemplateMod` | Migrate; lifecycle and Harmony smoke tests | None |
| `animusfound-labelos` | `meyerMedia.Next.SaaS.Template` | Migrate; auth, label/release domain tests, privacy and protected deployment | Hybrid-PG for catalog/search |
| `yourse` | `meyerMedia.mmui-Webapp.Template` | Audit scope and maintenance; migrate or archive | Lexical |
| `mm-ui` | `meyerMedia.Node.Package.Template` with design-system profile | Make canonical MMUI package; Storybook/docs, visual regression, tokens and API compatibility | None |
| `ShareWithYourFriends` | Unity Mono multi-loader mod profile based on `gregMod.TemplateMod` | Create a separate Mono/BepInEx-compatible template; host-authoritative contract tests | None |
| `hytale-modding` | game-modding workspace/research profile | Audit current Hytale APIs and redistribution rules; split examples, libraries and research | None |
| `OpenEngine` | engine/native workspace profile | Audit language/build system; apply Rust/C++ workspace, asset provenance and benchmark standards | Vector only if engine content tooling needs it |
| `AnimusMidiStudio` | `meyerMedia.Media.Tool.Template` / desktop profile | Migrate; MIDI fixture tests, realtime performance benchmarks and signed packages | None |
| `afnd-smartlinks` | `meyerMedia.Next.SaaS.Template` | Migrate; redirect safety, analytics privacy and campaign/link tests | Lexical analytics |
| `invoices` | placeholder | Define whether it replaces invoicing forks/products; otherwise archive | None |
| `rosa.fis.app` | `meyerMedia.Flutter.Client.Template` | Make canonical Rosa client if active; consolidate `rosa-tarifverbund` | API |
| `MiningTools` | placeholder/research profile | Define scope, license and data sources or archive | None |
| `gregApply` | `meyerMedia.mmui-Webapp.Template` | Audit product scope; migrate with forms, document/privacy and E2E coverage | Lexical; optional Hybrid-PG |
| `mm-mein-sv` | `meyerMedia.mmui-Webapp.Template` | Audit and migrate as a small interactive product | Lexical |
| `mm-m2-source` | upstream source/reverse-engineering profile | Preserve provenance/licenses; do not apply normal product sponsoring or release assumptions | None |
| `lnxr-whmcs` | `meyerMedia.PHP.Webapp.Template` + upstream integration profile | Migrate custom modules/themes separately from upstream WHMCS boundaries | Lexical |
| `lnxr-robotsgen-ui` | `meyerMedia.mmui-Webapp.Template` | Migrate; deterministic robots output, SEO fixtures and browser E2E | None |
| `seotools-ui` | `meyerMedia.mmui-Webapp.Template` | Migrate; parser/generator unit tests and browser workflows | Lexical |
| `goateq-web` | `meyerMedia.Next.Site.Template` or MMUI Webapp | Use as product site/demo for `goatEQ`; consolidate duplicated product docs | None |
| `DarkCourtGame` | `meyerMedia.Node.Workspace.Template` with game profile | Audit engine/runtime; add deterministic simulations, asset licenses and deployment docs | Vector only for AI/NPC knowledge if justified |
| `meyer-mcp` | `meyerMedia.Node.Service.Template` with MCP/AI profile | Migrate; tool allow-list, schema tests, auth, rate limits and audit logs | Hybrid-PG or Vector for knowledge tools |
| `meyer-media-apps` | `meyerMedia.DataCatalog.Template` / Next Site | Make central app catalog with generated metadata and links | Lexical |
| `gregMod.TemplateMod` | template | Continue as canonical IL2CPP mod template and make it comply with the universal baseline | None |

## Portfolio-level consolidation decisions

1. `gregMod.TemplateMod` replaces `gregMod.Template`.
2. `gregMod.IPAM` replaces `gregIPAM`.
3. `mygm-next` should become the canonical MyGM product after feature comparison with `MyGM` and `my-gamemaster`.
4. `mm-ach-stack` should be compared with `ach-glueck`; keep one canonical product architecture.
5. `mm-ui` should be the canonical design-system package; `lnxr-mm-ui` and `mm-saas-dash-ui` become consumers/showcases unless they have independent product scope.
6. `meyer-media-apps` and the profile repository should consume one generated project catalog rather than maintaining separate manual lists.
7. Generic repositories named `src`, `Server`, `deploy`, `invoices` and `MiningTools` require a scope/rename decision before further development.
8. Upstream forks must not be reformatted wholesale to match original-project templates; only governance overlays and local-patch validation are added.

## Execution waves

### Wave 0 — central foundations

- create `meyerMedia.CI.Workflows`
- create the repository-policy schema and scanner
- create shared docs/AGENTS/license/funding skeletons
- create coverage-normalization and release workflows

### Wave 1 — security-critical and canonical products

`gregCore`, `gregMod.TemplateMod`, `gregModmanager`, `gregWeb.Modstore`, `cus-svh-webapp`, `lnxr-whm`, `Shitcloud-Infra`, `DEMT`, `talkndate`, `cloud-drive`, `lunexor-mailtools`, `RushBot`, `RR_BOT_AI`, `ml-aimanager`.

### Wave 2 — reusable templates and active ecosystems

All greg mods/plugins, `mm-ui`, MMUI webapps, FiveM resources, browser extensions, Flutter clients and active desktop tools.

### Wave 3 — infrastructure, content and research

Docker stacks, PBX/server configuration, static sites/themes, modpacks, media tools and reverse-engineering repositories.

### Wave 4 — consolidation and archive

Old templates, duplicated product versions, empty placeholders and unmaintained upstream forks.

## Per-repository implementation checklist

For every row marked Migrate:

1. add `.meyermedia/repository.yml`
2. add/normalize README, license, SECURITY, SUPPORT, CONTRIBUTING, CHANGELOG and AGENTS
3. add `DESIGN.md`/architecture/privacy/threat model according to profile
4. pin runtime/package manager and commit one lockfile
5. establish measured coverage and fixtures
6. add reusable hardened CI
7. add SBOM/checksum/attestation release path
8. add deployment/rollback docs where applicable
9. enable branch/environment protection
10. remove stale badges, funding links, generated artifacts and secrets
