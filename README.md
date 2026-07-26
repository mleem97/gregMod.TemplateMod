# gregMod.TemplateMod

A reusable C# template for **Data Center** mods built with **MelonLoader**, **Harmony**, **Il2CppInterop**, and optional **gregCore** integration.

This repository consolidates the stable conventions used across the `gregMod.*` projects:

- .NET 6, x64, library output
- local game and loader references outside Git
- MelonLoader lifecycle entry point
- Harmony patch bootstrap
- MelonPreferences configuration
- predictable `Core`, `Features`, `Patches`, and `Infrastructure` folders
- PowerShell and Bash build scripts
- cross-platform project initializer

## Create a new mod

1. Create a repository from this template or clone it.
2. Run the initializer from the repository root:

```bash
python scripts/init-template.py \
  --name gregMod.Example \
  --author your-github-name \
  --description "Example mod for Data Center"
```

The command renames the project folder, `.csproj`, assembly, namespace, metadata, and documentation references.

## Required references

Copy the required DLLs into `references/`, or set the `GREGMOD_REFERENCE_ROOT` environment variable to a directory containing them.

Minimum expected files:

```text
references/
├── MelonLoader.dll
├── 0Harmony.dll
├── Il2CppInterop.Runtime.dll
├── Il2Cppmscorlib.dll
├── Assembly-CSharp.dll
├── UnityEngine.CoreModule.dll
├── UnityEngine.IMGUIModule.dll
├── UnityEngine.PhysicsModule.dll
├── UnityEngine.TextRenderingModule.dll
├── UnityEngine.UI.dll
├── UnityEngine.UIModule.dll
├── Unity.InputSystem.dll
└── Unity.TextMeshPro.dll
```

`gregCore.dll` is optional. When present, the build defines `GREGCORE` and declares the Melon dependency automatically.

## Build

PowerShell:

```powershell
./scripts/build.ps1
```

Linux/macOS:

```bash
./scripts/build.sh
```

Output:

```text
artifacts/gregMod.TemplateMod.dll
```

## Project structure

```text
src/gregMod.TemplateMod/
├── Core/
├── Features/
├── Infrastructure/
├── Patches/
└── gregMod.TemplateMod.csproj
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for extension points and conventions.

## Development rules

- Keep game-specific reflection and patch code isolated from feature logic.
- Guard initialization with clear logging and exception handling.
- Avoid committing game, Unity, MelonLoader, or gregCore binaries.
- Prefer small Harmony patches with explicit targets.
- Store user configuration through `MelonPreferences`.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
