# Contributing

1. Create a focused branch.
2. Keep game-specific reflection and Harmony targets isolated from feature logic.
3. Do not commit game binaries, generated IL2CPP proxy assemblies, Unity assemblies, or private credentials.
4. Run `python scripts/verify-env.py` and a Release build before opening a pull request.
5. Update `CHANGELOG.md` for user-visible changes.

Prefer small patches with explicit failure logging. Avoid swallowing exceptions unless a game lifecycle transition is known to make an operation best-effort.
