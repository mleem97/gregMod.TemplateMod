# CI/CD hardening baseline

This baseline applies to every Meyer Media template: Node.js applications, packages, FiveM resources, .NET mods, container stacks and release tooling.

## Security objectives

The pipeline must provide:

1. untrusted pull-request validation without privileged credentials
2. reproducible dependency installation and builds
3. explicit promotion of a previously built artifact
4. least-privilege authentication and deployment
5. verifiable provenance, checksums and dependency records
6. a documented rollback path

## Repository controls

Mandatory repository settings:

- protect the default branch
- require pull requests and successful status checks
- require review for workflow, dependency and deployment changes
- use `CODEOWNERS` for `.github/workflows/**`, deployment files, lockfiles and security configuration
- block force pushes and branch deletion on protected branches
- enable secret scanning and push protection where available
- enable Dependabot alerts and security updates
- require signed commits/tags where the collaboration model supports it
- use immutable releases for published artifacts when available

Recommended ownership examples:

```text
.github/workflows/** @security-maintainers
.github/dependabot.yml @security-maintainers
pnpm-lock.yaml @node-maintainers
package-lock.json @node-maintainers
Dockerfile* @platform-maintainers
compose*.yml @platform-maintainers
fxmanifest.lua @fivem-maintainers
```

## GitHub Actions policy

### Least privilege

Every workflow starts with:

```yaml
permissions:
  contents: read
```

Additional permissions are granted at job level only. Examples:

- `id-token: write` only for OIDC authentication or provenance
- `packages: write` only for the publishing job
- `attestations: write` only for artifact attestation
- `security-events: write` only for CodeQL upload
- `pull-requests: write` only for a job that must comment or label

Never use `write-all`.

### Pin actions immutably

All third-party and GitHub-authored actions must be pinned to a full-length commit SHA. Keep the readable release in a comment and let Dependabot or Renovate update the SHA.

```yaml
- uses: actions/checkout@<full-commit-sha> # v6.x
```

Do not use floating branches such as `main`, `master` or unpinned version tags in production workflows.

### Untrusted input

Treat pull-request titles, bodies, labels, branch names, commit messages, issue text and usernames as attacker-controlled.

Do not interpolate GitHub expressions directly into shell scripts:

```yaml
# Unsafe
run: echo "${{ github.event.pull_request.title }}"
```

Pass values through environment variables or action inputs and quote them in the receiving process.

Never combine `pull_request_target`, repository secrets and checkout/execution of the pull request head. Privileged follow-up jobs must consume reviewed artifacts or run only after an explicit maintainer-controlled action.

### Runner policy

- use GitHub-hosted runners for public/untrusted pull requests
- never run fork pull requests on persistent self-hosted runners
- use ephemeral self-hosted runners for deployment or private-network access
- place deployment runners in a restricted network segment
- do not give runners broad access to production databases, hypervisors or internal administration networks
- set job-level `timeout-minutes`
- use `concurrency` for deployments to prevent overlapping releases

### Cache policy

Caches are performance hints, not trusted release inputs.

- key caches by operating system, runtime and lockfile hash
- never cache secrets or `.npmrc` credentials
- do not restore write-capable caches from untrusted forks into privileged jobs
- disable package-manager caching for final registry publication where required by the publisher security model
- rebuild release artifacts from a clean checkout and frozen lockfile

## Node.js dependency baseline

As of July 2026, templates should target Node.js 24 LTS for production. Node.js 26 is still Current until it enters LTS.

Each repository must contain:

- `.node-version` or equivalent runtime declaration
- exact `packageManager` version in `package.json`
- one committed lockfile
- `engines.node` matching the supported LTS range
- automated dependency updates for npm/pnpm and GitHub Actions

Install commands:

```bash
pnpm install --frozen-lockfile
# or
npm ci
```

Do not run `npm install`, `pnpm update`, `npx npm-check-updates -u` or arbitrary package upgrades in CI or deployment jobs.

For pnpm, explicitly approve packages that may execute install/build scripts. Do not permit all dependency lifecycle scripts by default.

Required pull-request checks:

- lint
- strict type check
- unit tests
- build
- dependency review
- package audit/signature verification where supported
- CodeQL for JavaScript/TypeScript and GitHub Actions
- end-to-end tests for critical user journeys

## Build and release separation

Use a three-stage model:

```text
validate -> build/package -> deploy/promote
```

Rules:

- the build job has no production credentials
- deployment does not rebuild source code
- deployment consumes the exact artifact produced and tested by CI
- artifacts include a SHA-256 checksum
- release metadata records commit SHA, runtime version and dependency lock hash
- generate an SBOM for distributable applications and containers
- generate GitHub artifact attestations where the repository plan supports them
- keep release artifacts immutable after publication

## Publishing Node.js packages

Use npm trusted publishing with GitHub Actions OIDC instead of a long-lived `NPM_TOKEN` whenever available.

Publishing job requirements:

- GitHub-hosted runner
- protected release environment
- `contents: read`
- `id-token: write`
- exact trusted workflow filename configured on npm
- tests and package-content inspection before publish
- provenance enabled automatically through trusted publishing
- optional staged publishing for packages requiring human approval

The package must have an exact and correct `repository.url`. Release builds should run `npm pack --dry-run` and inspect the files included in the package.

## Deployment environments

Use separate GitHub environments:

- `development`
- `staging`
- `production`

Production recommendations:

- only protected branches or signed release tags may deploy
- required reviewer who is not the initiating actor, where the plan supports it
- environment-scoped secrets only
- prevent environment-rule bypass where possible
- deployment concurrency limited to one
- automatic rollback or documented one-command rollback

Prefer OIDC federation to cloud providers and registries. Avoid static cloud access keys. Where OIDC is unavailable, use a narrowly scoped credential with short expiration, restricted source/network access and documented rotation.

## Container hardening

For Node.js services and web applications:

- multi-stage build
- pinned base-image digest
- non-root runtime user
- read-only root filesystem where practical
- no package manager, compiler or source tree in the runtime image
- explicit health check
- minimal Linux capabilities
- resource limits in deployment configuration
- image scan and SBOM
- signed/attested image provenance

Database migrations run as an explicit pre-deployment job, not silently during application startup.

## FiveM CI baseline

Every FiveM resource workflow should validate:

- `fxmanifest.lua` exists and contains explicit metadata
- all referenced scripts/files exist
- no forbidden secrets or webhook URLs are committed
- Lua formatting and static analysis
- frontend lint/type/test/build for NUI resources
- deterministic package contents
- maximum asset and release archive size
- no development files, source maps or dependency directories in release ZIPs unless explicitly intended

Release package examples:

```text
resource-name-1.2.3.zip
resource-name-1.2.3.zip.sha256
resource-name-1.2.3.sbom.json
```

## FiveM deployment hardening

Preferred deployment model:

1. CI builds and signs/checksums a resource ZIP.
2. A protected production job downloads that exact artifact.
3. The deployment account has access only to the FiveM resource directory and restart mechanism.
4. The package is extracted into a versioned staging directory.
5. Manifest and file checks are repeated on the target.
6. Deployment switches an atomic symlink/directory pointer.
7. Only the affected resource is restarted when safe.
8. Health/log verification runs before marking the deployment successful.
9. The previous version remains available for immediate rollback.

Do not deploy directly from a developer working tree. Do not give the CI runner root access or unrestricted SSH access. Prefer a forced-command deploy key, restricted service account or pull-based deployment agent.

## FiveM runtime security

CI cannot compensate for insecure resource logic. Templates must enforce:

- server-authoritative validation
- local handlers for local-only events
- network events only when intentionally exposed
- validation and rate limiting for client-triggered server events
- no trust in client prices, item quantities, permissions, coordinates or reward results
- no secrets in client scripts, shared scripts or NUI bundles
- safe SQL parameterization
- framework and dependency version checks
- resource-stop cleanup

## Dependency automation

Dependabot or Renovate should update:

- npm/pnpm dependencies
- GitHub Actions SHAs
- Docker image digests
- language/runtime toolchains where supported

Update PRs should be grouped conservatively. Security updates remain separate and high priority. Major-version updates require human review and must not auto-merge by default.

## Reusable workflows

`meyerMedia.CI.Workflows` should provide versioned reusable workflows:

- `node-ci.yml`
- `node-package-release.yml`
- `next-build.yml`
- `container-build.yml`
- `fivem-validate.yml`
- `fivem-package.yml`
- `deploy-artifact.yml`
- `codeql.yml`

Consumer repositories should pass only explicit inputs and secrets. Reusable workflows must define minimal permissions internally and expose no generic shell-command input.

## Minimum merge gate

A change may merge only when:

- review requirements are satisfied
- lint and type checks pass
- tests pass
- clean build succeeds
- dependency review passes
- security scanning passes or findings are explicitly accepted
- generated artifacts match expected contents
- workflow changes have security-owner approval

A release may deploy only when the artifact was built from the protected default branch or an approved release tag and has passed the same commit's required checks.