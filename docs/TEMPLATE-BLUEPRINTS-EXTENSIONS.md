# Additional template blueprints

These profiles extend `TEMPLATE-BLUEPRINTS.md` for existing repository families discovered during the account-wide inventory.

## `meyerMedia.PHP.Webapp.Template`

For maintained Laravel/PHP applications that should not yet be rewritten to the Node/Next stack.

```text
app/
  Domain/
  Application/
  Infrastructure/
  Http/
resources/
  js/
  views/
routes/
database/
  migrations/
  factories/
  seeders/
tests/
  Unit/
  Feature/
  Browser/
docs/
  DESIGN.md
  ARCHITECTURE.md
  THREAT-MODEL.md
  PRIVACY.md
  DEPLOYMENT.md
  OPERATIONS.md
```

Required: Composer lockfile, PHPStan/Psalm, Pint, PHPUnit/Pest, dependency audit, database integration tests, explicit queue/scheduler operation, non-root container and separate migration job. Coverage: 85/80 for business logic and APIs.

## `meyerMedia.Shell.LinuxTool.Template`

For Bash-based repair, deployment and system administration tools.

```text
bin/
lib/
config/
tests/
  bats/
fixtures/
scripts/
docs/
  COMMANDS.md
  THREAT-MODEL.md
  OPERATIONS.md
  RECOVERY.md
```

Required: ShellCheck, shfmt, Bats tests, `--dry-run`, explicit privilege checks, no unquoted expansion, safe temporary files, rollback and destructive-operation confirmations. Privileged commands must be individually allow-listed rather than relying on broad root execution.

## `meyerMedia.Minecraft.Modpack.Template`

For CurseForge/Modrinth-compatible modpacks and content packs.

```text
config/
defaultconfigs/
kubejs/
mods-manifest/
quests/
resourcepacks/
scripts/
docs/
  DESIGN.md
  COMPATIBILITY.md
  SERVER-SETUP.md
  CHANGELOG.md
pack-manifest.json
```

CI validates manifest entries, exact mod versions, licensing/redistribution rules, client/server compatibility, duplicate mods, config syntax, pack size and deterministic export. Binary mods are referenced through approved distribution manifests rather than committed when redistribution is not permitted.

## `meyerMedia.RustOxide.Plugin.Template`

For Rust game uMod/Oxide C# plugins.

```text
src/<PluginName>.cs
tests/
  Unit/
  Contract/
fixtures/
docs/
  CONFIGURATION.md
  PERMISSIONS.md
  COMPATIBILITY.md
scripts/
  validate-plugin.*
  package-release.*
```

Required: namespaced permissions/commands, defensive hook cleanup, config migration, language-file tests, serialization tests, no trust in client-supplied values and a server smoke-test plan. Coverage: 75/65 for extractable logic; the single-file release is generated from testable source modules when practical.

## `meyerMedia.GameServer.Content.Template`

For server packs, asset bundles and game-server configuration that are not normal code libraries.

```text
content/
config/
manifests/
scripts/
  validate.*
  package.*
docs/
  INSTALLATION.md
  OPERATIONS.md
  COMPATIBILITY.md
  ASSET-LICENSES.md
```

CI checks referenced assets, licenses, archive contents, forbidden secrets and size budgets. Large or proprietary assets use release storage, Git LFS or external manifests rather than normal Git history.

## `meyerMedia.Media.Tool.Template`

For audio/video processing tools such as normalizers or effects utilities.

```text
src/
  Core/
  Codecs/
  Processing/
  CliOrUi/
tests/
  Unit/
  Golden/
  Integration/
fixtures/
  generated/
docs/
  DESIGN.md
  FORMATS.md
  BENCHMARKS.md
```

Golden tests use short generated or properly licensed fixtures. CI validates deterministic output tolerances, metadata preservation, failure handling and platform packaging. Coverage: 85/80 core processing logic.

## `meyerMedia.Proxy.Service.Template`

For small compatibility proxies and redirects.

```text
src/
tests/
  unit/
  integration/
infra/
docs/
  ARCHITECTURE.md
  THREAT-MODEL.md
  OPERATIONS.md
```

Required: target allow-listing, header policy, loop prevention, timeout/body limits, health checks, access logging with redaction and tests preserving path/query semantics. Coverage: 90/85 because the functional surface is small.

## `meyerMedia.DataCatalog.Template`

For repositories that primarily publish an index, catalog or metadata about mods/assets/projects.

```text
data/
schemas/
scripts/
  validate-data.*
  generate-site.*
  check-links.*
docs/
tests/
```

Schema validation, duplicate detection, URL/hash verification and generated documentation are the primary gates. A semantic index is optional for large catalogs, but structured filters and lexical search remain the source of truth.

## `meyerMedia.UpstreamApplicationFork.Template`

For substantial forks such as Invoice Ninja or third-party browser extensions.

Adds to the upstream layout:

```text
UPSTREAM.md
PATCHES.md
LOCAL-ROADMAP.md
.github/workflows/local-validation.yml
scripts/sync-upstream.*
```

The local plan states whether the fork is a temporary patch queue, a maintained distribution or a migration source. Upstream license, security policy and attribution remain authoritative unless explicitly supplemented.
