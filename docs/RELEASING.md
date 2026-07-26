# Releasing

1. Update `BuildInfo.Version`.
2. Update `CHANGELOG.md`.
3. Run a clean Release build.
4. Launch the game and test initialization, scene transitions, preferences, and unload/quit behavior.
5. Create the ZIP:

```bash
python scripts/package-release.py
```

6. Tag the commit with `v<version>` and attach the ZIP.

Only the mod DLL, optional PDB/XML documentation, README, changelog, and license belong in the release. Never package generated interop assemblies or game files.
