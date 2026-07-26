# Node, MMUI and FiveM template roadmap

This document extends the portfolio template analysis with the recurring Meyer Media web, Node.js and FiveM project families.

## Evidence from existing repositories

The repositories show several distinct patterns that should not be combined into a single universal template:

- `mm-jlb` is a modern Next.js application with pnpm, TypeScript, Vitest, Playwright, PWA/offline storage, localization and optional AI providers.
- `meyer-hotel` is a transactional Next.js application with Prisma, authentication, Stripe and database deployment migrations.
- `gregWeb.Modstore` is a full application platform with authentication, PostgreSQL/Drizzle, Redis, S3-compatible storage, email and OpenAPI.
- `lnxr-whm` is a pnpm/Turborepo workspace containing multiple applications, services and shared packages.
- `mm_megaphone` is a standalone FiveM Lua resource with a framework/voice bridge.
- `mm_affiliate` combines FiveM client/server Lua with an NUI frontend.
- `mm_gploads` is a static FiveM loading-screen resource with media assets.

## Recommended template repositories

| Priority | Repository | Responsibility | Why it should be separate |
| --- | --- | --- | --- |
| 1 | `meyerMedia.mmui-Webapp.Template` | Opinionated Next.js web application using the Meyer Media UI system | Provides the default product-development path without forcing a multi-service monorepo or a full SaaS platform into every application. |
| 2 | `meyerMedia.CI.Workflows` | Reusable hardened GitHub Actions workflows and policy files | Security fixes, action pin updates and release rules should be maintained once and consumed by all templates. |
| 3 | `meyerMedia.Node.Service.Template` | Node.js HTTP/API/background service | Services have different runtime, observability, health-check and deployment requirements from Next.js applications. |
| 4 | `meyerMedia.Node.Workspace.Template` | pnpm/Turborepo monorepo with apps, services and packages | Large platforms need dependency boundaries, affected builds and coordinated releases that are unnecessary for single applications. |
| 5 | `meyerMedia.Node.CLI.Template` | TypeScript command-line and automation tool | CLI programs need argument parsing, exit-code discipline, signal handling, packaging and platform tests rather than browser concerns. |
| 6 | `meyerMedia.Node.Package.Template` | Publishable TypeScript library or SDK | Libraries require dual-format output, declarations, compatibility testing and trusted registry publishing rather than application deployment. |
| 7 | `meyerMedia.Next.Site.Template` | Lightweight content, landing and portfolio site | Keeps static sites free from databases, authentication services and operational dependencies. |
| 8 | `meyerMedia.FiveM.Resource.Template` | Standalone Lua client/server resource | Establishes secure event handling, framework adapters, localization, configuration and resource packaging. |
| 9 | `meyerMedia.FiveM.NUI.Template` | FiveM Lua resource with a compiled TypeScript web UI | NUI introduces browser security, typed message contracts, focus lifecycle and frontend build concerns. |
| 10 | `meyerMedia.FiveM.Loadscreen.Template` | Static FiveM loading screen | Loading screens should remain small, media-optimized and independent from gameplay/framework dependencies. |
| Conditional | `meyerMedia.FiveM.FrameworkBridge.Template` | Shared adapters for QBCore, ESX, ox_core, inventory and voice systems | Create this only when adapters are reused by several resources; otherwise keep adapters inside the resource template. |

## 1. `meyerMedia.mmui-Webapp.Template`

### Intended scope

This is the default template for interactive Meyer Media web products. It sits between a lightweight site and a large SaaS/monorepo.

Recommended baseline:

- Node.js Active LTS
- pnpm with an exact `packageManager` version and committed lockfile
- Next.js App Router, React and strict TypeScript
- MMUI design tokens, components and layout primitives
- Tailwind CSS with centralized theme tokens
- Zod-based environment and request validation
- Vitest and Testing Library for unit/component tests
- Playwright for critical browser journeys
- ESLint, Prettier and strict type checking
- error boundaries, structured server logging and request correlation IDs
- accessibility checks and performance budgets
- optional adapters for database, authentication, email, object storage, payments, PWA and AI providers

### Module policy

Features such as Prisma/Drizzle, Stripe, passkeys, Redis, S3, PWA and AI providers must be opt-in modules. The base template should build and test without credentials or external services.

Suggested structure:

```text
src/
  app/
  components/
    mmui/
  features/
  lib/
    env/
    logging/
    security/
  server/
  styles/
tests/
  unit/
  e2e/
```

## 2. Node.js template family

### `meyerMedia.Node.Service.Template`

Use for REST APIs, webhook consumers, workers and internal services.

Required conventions:

- explicit runtime schema validation
- `/health/live` and `/health/ready`
- graceful shutdown for `SIGTERM` and `SIGINT`
- request/body size limits and timeouts
- structured JSON logging with secret redaction
- rate limiting and trusted-proxy configuration
- OpenAPI generation from shared schemas
- container image running as a non-root user
- database migrations executed as a separate deployment step

### `meyerMedia.Node.Workspace.Template`

Use for platforms resembling `lnxr-whm`.

Required conventions:

- `apps/*`, `services/*` and `packages/*`
- pnpm workspace catalog/overrides and approved build scripts
- Turborepo affected builds and remote-cache isolation
- dependency-boundary checks
- Changesets for coordinated versioning
- independent deploy jobs per application/service
- shared generated schemas rather than copied DTOs

### `meyerMedia.Node.CLI.Template`

Use for local administration, migration and automation tools.

Required conventions:

- deterministic exit codes
- `--json`, `--quiet`, `--verbose` and `--dry-run` behavior
- no interactive prompt when running in CI
- signal-safe cleanup
- platform matrix for Windows, Linux and macOS where applicable
- packaged executable or documented `pnpm dlx` usage

### `meyerMedia.Node.Package.Template`

Use for reusable packages and API clients.

Required conventions:

- ESM-first output with declarations and an explicit `exports` map
- compatibility tests against supported Node.js LTS lines
- package-content inspection with `npm pack --dry-run`
- API Extractor or equivalent public-surface checks where useful
- npm trusted publishing through OIDC
- provenance, changelog and signed/attested release artifacts

## 3. FiveM template family

### `meyerMedia.FiveM.Resource.Template`

Recommended structure:

```text
fxmanifest.lua
shared/
  config.lua
  locale.lua
client/
  main.lua
server/
  main.lua
bridge/
  framework.lua
  inventory.lua
  voice.lua
locales/
tests/
```

Security requirements:

- use `AddEventHandler` for same-context events and `RegisterNetEvent` only when cross-context/network access is intentional
- treat every client-triggered server event as attacker-controlled
- validate `source`, permissions/job, entity ownership, distance, item counts, monetary values and state on the server
- rate-limit sensitive events and commands
- namespace all events and exports
- never trust NUI results for authorization or rewards
- keep secrets, webhooks and database credentials server-side
- clean up state and focus in `onResourceStop`

### `meyerMedia.FiveM.NUI.Template`

Adds a compiled Vite/React/TypeScript frontend to the resource template.

Required conventions:

- typed Lua-to-NUI and NUI-to-Lua message contracts
- bundled local assets; no runtime CDN dependencies
- restrictive Content Security Policy where CEF support permits it
- no `eval`, remote scripts or dynamic HTML insertion with untrusted content
- strict validation of every `RegisterNUICallback` payload
- focus restoration and resource-stop cleanup
- frontend build output copied into a deterministic `web/dist` directory
- frontend test mode independent of a running FiveM client

### `meyerMedia.FiveM.Loadscreen.Template`

Required conventions:

- no gameplay framework dependency
- optimized and size-budgeted images/audio
- preloading and graceful missing-media handling
- accessible mute/volume controls
- deterministic asset manifest
- release ZIP containing only required runtime files

## Creation order

1. `meyerMedia.CI.Workflows`
2. `meyerMedia.mmui-Webapp.Template`
3. `meyerMedia.FiveM.Resource.Template`
4. `meyerMedia.FiveM.NUI.Template`
5. `meyerMedia.Node.Service.Template`
6. `meyerMedia.Node.Workspace.Template`
7. `meyerMedia.Next.Site.Template`
8. `meyerMedia.Node.Package.Template`
9. `meyerMedia.Node.CLI.Template`
10. `meyerMedia.FiveM.Loadscreen.Template`

The shared workflow repository comes first because every later template should consume the same hardened CI, release and deployment contracts.