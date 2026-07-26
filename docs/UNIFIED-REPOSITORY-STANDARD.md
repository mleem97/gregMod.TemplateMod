# Unified repository standard

This document defines the mandatory Meyer Media / mleem97 repository baseline. Every maintained repository inherits this standard and adds a type-specific template profile.

## 1. Repository classes

Every repository must be assigned one lifecycle class:

- **product** — deployed application, service, mod, plugin, game resource or desktop tool
- **library** — reusable package, framework, SDK or UserLib dependency
- **infrastructure** — Docker, deployment, backup, server or observability configuration
- **research** — reverse engineering, firmware, protocol or experimental work
- **content** — website, documentation, profile, theme or static media project
- **template** — source for creating new repositories
- **upstream fork** — externally maintained project with local patches
- **archive** — retained for reference but no longer actively maintained
- **placeholder** — empty repository awaiting a concrete scope decision

A repository without an assigned class is non-compliant.

## 2. Mandatory root files

All maintained repositories contain:

```text
README.md
LICENSE or LICENSE.md
SECURITY.md
SUPPORT.md
CONTRIBUTING.md
CHANGELOG.md
AGENTS.md
.editorconfig
.gitattributes
.gitignore
.github/
  CODEOWNERS
  dependabot.yml or renovate.json
  pull_request_template.md
  ISSUE_TEMPLATE/
  workflows/
docs/
  CI-CD.md
  TESTING.md
```

Additional files by condition:

| File | Required when |
| --- | --- |
| `DESIGN.md` | UI/UX, public API, protocol, complex architecture, branding or product behavior requires explicit design decisions |
| `ARCHITECTURE.md` | More than one deployable component, major layer, runtime boundary or plugin/module system exists |
| `ROADMAP.md` | Product or framework has planned milestones |
| `DEPLOYMENT.md` | Repository produces a deployed runtime artifact |
| `OPERATIONS.md` | A service, database, container stack or server must be operated |
| `PRIVACY.md` | User data, telemetry, authentication, uploads, AI prompts or third-party processors are involved |
| `THREAT-MODEL.md` | Authentication, payments, privileged administration, remote execution, multiplayer events or sensitive data exist |
| `UPSTREAM.md` | Fork, vendored dependency or repackaged third-party library |
| `NOTICE` | Required by license or when third-party attribution is material |
| `SPONSORS.md` | Public project accepts financial support |
| `.github/FUNDING.yml` | Current funding channels have been verified |

Small scripts may combine `ARCHITECTURE.md`, `DESIGN.md` and `OPERATIONS.md` into concise sections in the README, but the exception must be recorded in `AGENTS.md`.

## 3. README contract

Every README follows this order:

1. project name and one-sentence purpose
2. status and maintenance level
3. badges: CI, coverage, license and release where applicable
4. screenshots or architecture diagram where useful
5. features and non-goals
6. requirements
7. quick start
8. configuration
9. test/build commands
10. deployment or installation
11. security and privacy links
12. contribution link
13. license and third-party notices
14. support and sponsoring link

Badges must reflect real checks. Placeholder, broken or stale badges are prohibited.

## 4. `AGENTS.md` contract

`AGENTS.md` is mandatory for every maintained repository and must be written for human and automated contributors. It contains:

- repository purpose and lifecycle class
- supported runtimes and package managers
- architecture map and important directories
- authoritative build, lint, test, coverage and release commands
- generated files and files that must not be edited manually
- dependency and lockfile policy
- security boundaries and secrets policy
- required documentation updates for each change type
- commit and pull-request expectations
- forbidden operations such as bypassing tests, weakening validation or committing binaries
- local environment notes
- completion checklist

Monorepos and large workspaces add nested `AGENTS.md` files in `apps/*`, `services/*`, `packages/*` or equivalent boundaries. The closest file wins for local instructions.

## 5. `DESIGN.md` contract

`DESIGN.md` is mandatory for web products, desktop applications, browser extensions, game UIs, NUI resources, public frameworks and complex tools. It records:

- user groups and primary workflows
- design principles and non-goals
- information architecture
- component and token strategy
- responsive behavior
- accessibility target
- loading, empty, error and offline states
- privacy-sensitive UI behavior
- screenshots, wireframes or diagrams where useful
- accepted trade-offs and rejected alternatives

For non-visual systems, `DESIGN.md` covers API, protocol, data-model or operational design rather than visual styling.

## 6. License policy

| Repository type | Default policy |
| --- | --- |
| Original public software and templates | Apache-2.0 unless a deliberate exception is documented |
| Small compatibility snippets where maximum reuse is intended | MIT may be selected explicitly |
| Private/proprietary product | `LICENSE.md` with all-rights-reserved terms and owner statement |
| Fork | Preserve upstream license exactly; document local changes in `UPSTREAM.md` |
| `gregLibs.*` or vendored dependency | Preserve every upstream license, add `NOTICE`, provenance and exact upstream commit |
| Documentation/content released separately | State the content license explicitly; do not assume the code license covers assets |

License detection is a required CI check. A repository may not publish a release with unknown or incompatible dependency licenses.

## 7. Sponsoring policy

Public maintained projects may include `SPONSORS.md` and `.github/FUNDING.yml`. Funding links must be verified before publication and reviewed at least annually. Private, internal, archived and upstream-mirror repositories omit funding banners unless there is a clear business reason.

Sponsoring must never replace support documentation, security reporting or license attribution.

## 8. Testing and coverage standard

Coverage is a merge gate, not only a badge. Generated code, migrations, type declarations and external vendored code may be excluded with documented justification.

| Profile | Line coverage floor | Branch coverage floor | Additional requirement |
| --- | ---: | ---: | --- |
| Core libraries, SDKs, framework APIs and security logic | 90% | 85% | public API compatibility tests |
| Services, SaaS business logic and data access | 85% | 80% | integration tests with real database/service containers |
| Webapps and desktop apps | 80% | 75% | critical user journeys in E2E tests |
| Mods, plugins and game resources | 75% of testable managed/core logic | 65% | loader/resource smoke test; Unity/FiveM bindings isolated behind adapters |
| CLI, automation and PowerShell tools | 80% | 70% | exit-code, dry-run and failure-path tests |
| Infrastructure repositories | N/A for declarative files | N/A | configuration validation, policy tests and deployment smoke tests |
| Static sites, themes and loadscreens | N/A unless logic exists | N/A | accessibility, broken-link and asset-budget checks |
| Research repositories | case-specific | case-specific | reproducible fixture and regression tests for analysis scripts |

New or changed code should meet the profile floor. A temporary exception requires an issue, owner and expiry date.

Coverage artifacts:

- machine-readable report (`lcov`, Cobertura or equivalent)
- HTML report as a CI artifact
- changed-lines coverage where tooling supports it
- summary in pull requests
- no upload of source or secrets to an external coverage service without an explicit privacy decision

## 9. Universal CI pipeline

Every maintained repository implements:

```text
metadata/docs -> dependency install -> lint/format -> type/static analysis
-> unit tests + coverage -> integration/e2e/smoke -> build/package
-> security/license/SBOM -> artifact attestation -> protected deployment/release
```

Required controls:

- read-only workflow permissions by default
- full commit-SHA pinning for actions
- frozen lockfiles and reproducible dependency installation
- no privileged execution of untrusted pull-request code
- secret scanning and push protection where available
- dependency review and automated dependency-update pull requests
- CodeQL or language-appropriate SAST
- explicit job timeouts and deployment concurrency
- build once, promote the tested artifact without rebuilding
- checksums, SBOM and provenance for distributed artifacts
- OIDC or short-lived credentials instead of long-lived deployment tokens
- protected `staging` and `production` environments
- documented rollback

Details remain authoritative in `docs/CI-CD-HARDENING-BASELINE.md`.

## 10. Release standard

Every release-capable repository provides:

- semantic version or a documented alternative
- generated changelog from reviewed changes
- immutable artifact names containing the version
- SHA-256 checksums
- SBOM for applications, packages, containers and binary releases
- provenance/attestation when supported
- license and notice files inside distributable archives
- rollback or uninstall instructions
- release notes including migrations and breaking changes

Production deployment is never performed from an uncommitted working tree.

## 11. Search and retrieval architecture for large projects

A large project must define a retrieval strategy in `DESIGN.md` or `ARCHITECTURE.md`. A vector database is not mandatory merely because a repository is large; it is required only when semantic similarity, recommendations, RAG, multimodal retrieval or fuzzy knowledge discovery is a product requirement.

Decision order:

1. **Exact lookup and structured filters:** relational indexes, B-tree, GIN, GiST or appropriate key-value access.
2. **Keyword/document search:** PostgreSQL full-text search, trigram search or a dedicated lexical engine.
3. **Semantic search inside an existing PostgreSQL product:** `pgvector` with exact search initially and HNSW when benchmarks justify ANN.
4. **Vector-centric, filtered, multi-tenant or high-throughput retrieval:** a dedicated engine such as Qdrant.
5. **Existing search/log platform requiring hybrid lexical and vector search:** OpenSearch.
6. **Low-latency cache, session or live ranking workload:** Redis search/vector indexes where memory cost is acceptable.
7. **Analytics-first corpus:** ClickHouse or another analytical engine, with vector search only when it keeps the data path simpler.

The default for AI-enabled large products is **hybrid retrieval**: lexical search plus vector candidates, metadata filters and optional re-ranking.

Every vector design records:

- corpus and expected vector count
- embedding model, dimensions and versioning policy
- tenant and authorization filters
- update, deletion and re-embedding behavior
- latency, throughput and recall targets
- exact-vs-approximate benchmark
- storage/RAM cost and backup plan
- personal-data and retention rules
- fallback when the embedding provider is unavailable
- migration strategy between embedding models or engines

A vector engine may not become the source of truth for permissions, billing, inventory or other transactional state.

## 12. Repository settings

Mandatory where supported:

- default branch named `main` for new repositories
- protected default branch
- pull requests required
- required status checks
- stale approval dismissal after material changes
- CODEOWNERS review for workflows, lockfiles, deployment and security files
- force pushes and branch deletion blocked
- merge queue or auto-merge only after required checks
- releases and environments protected
- vulnerability alerts and dependency graph enabled

Legacy default branches are migrated only with a tested redirect/update plan.

## 13. Compliance automation

A future central repository, `meyerMedia.CI.Workflows`, should provide:

- reusable validation workflows per language/profile
- a repository-policy scanner
- standard issue and pull-request templates
- shared `AGENTS.md`, `README`, `DESIGN.md` and documentation skeletons
- license and funding templates
- coverage report normalization
- SBOM and artifact-attestation workflows
- scheduled stale-link, dependency and funding-link checks

Each repository should contain a machine-readable profile, for example:

```yaml
schemaVersion: 1
class: product
template: meyerMedia.mmui-Webapp.Template
maintenance: active
licensePolicy: apache-2.0
coverageProfile: webapp
requiresDesignDoc: true
requiresThreatModel: true
retrievalProfile: hybrid-pgvector
```

Recommended path: `.meyermedia/repository.yml`.

## 14. Migration order

1. classify repository and maintenance status
2. add license/security/support files
3. add `AGENTS.md` and documentation skeleton
4. normalize package/runtime declarations and lockfiles
5. add tests and establish a measured coverage baseline
6. add hardened validation CI
7. add build/release artifacts
8. add protected deployment only after validation is stable
9. enable branch and environment protections
10. raise coverage floors gradually to the target profile

Do not add a misleading coverage badge before the underlying suite and merge gate exist.

## 15. Greg Framework ecosystem naming

The Greg Framework naming policy is authoritative in [`GREG-ECOSYSTEM-NAMING.md`](./GREG-ECOSYSTEM-NAMING.md).

Mandatory rules:

- every repository whose name contains `greg` or `Greg` is classified as part of the Greg Framework ecosystem;
- every maintained repository whose primary scope is the game Data Center must use a canonical `greg`-prefixed repository name;
- Data Center mods, plugins, libraries, tools, bridges, websites, infrastructure and research use the type-specific prefixes defined in the naming policy;
- unrelated Meyer Media projects must not use the `greg` prefix;
- legacy Data Center repositories without the prefix must be renamed, consolidated or documented as upstream forks;
- repository renames must preserve compatibility for assemblies, package IDs, namespaces, configuration keys, URLs and release artifacts;
- Greg repositories declare `ecosystem: greg-framework` in `.meyermedia/repository.yml` and Data Center projects additionally declare `productFamily: data-center`.

Naming compliance is part of the repository-policy CI gate.