# Contributing

## Setup

1. Install the .NET 6 SDK.
2. Populate `references/` or set `GREGMOD_REFERENCE_ROOT`.
3. Build with `scripts/build.ps1` or `scripts/build.sh`.

## Changes

- Keep patches focused and document unusual reflection or IL2CPP behavior.
- Do not commit game or framework binaries.
- Include useful log messages for initialization failures.
- Verify both Debug and Release builds before opening a pull request.
- Update `CHANGELOG.md` for user-visible changes.

## Commit style

Use concise imperative messages, for example:

- `Add inventory persistence`
- `Fix input suppression after closing UI`
- `Document required Unity references`
