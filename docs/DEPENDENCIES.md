# Dependencies

## Public dependencies

`LavaGang.MelonLoader` is restored from NuGet and supplies the loader API plus its HarmonyX and Il2CppInterop dependencies. Its version is pinned in `Directory.Packages.props`.

This avoids checking loader binaries into every mod repository and makes restore behavior consistent across development machines.

## Game-specific dependencies

An IL2CPP mod must compile against generated proxy assemblies for the exact game build. MelonLoader creates these after the game is launched successfully:

```text
<Game>/MelonLoader/Il2CppAssemblies/
```

At minimum the template validates:

- `Assembly-CSharp.dll`
- `Il2Cppmscorlib.dll`
- `UnityEngine.CoreModule.dll`

The project references every DLL in that generated folder with `Private=false`, so they are used only at compile time and are not copied into the mod artifact.

These assemblies can be proprietary or derived from proprietary game metadata. Do not commit or redistribute them unless the rights holder explicitly permits it.

## Local setup

Run:

```bash
python scripts/setup-dev.py --game-dir "/path/to/Data Center"
```

The script discovers the generated interop directory, validates it, optionally detects `Mods/gregCore.dll`, and writes `Directory.Build.local.props`.

Environment-variable alternatives:

```text
GREGMOD_GAME_DIR
GREGMOD_INTEROP_DIR
GREGCORE_DLL
```

## Portable local cache

Use `--copy-interop` to copy generated assemblies into the gitignored `.deps/interop` directory:

```bash
python scripts/setup-dev.py --game-dir "/path/to/Data Center" --copy-interop
```

This is useful for containers or offline work but does not make the assemblies redistributable.

## CI full builds

The default CI workflow does not require game binaries. It restores packages and validates the template.

For full builds, provide a private ZIP containing the generated interop folder and configure:

- repository variable `CI_INTEROP_ARCHIVE_URL`
- optional secret `CI_INTEROP_TOKEN`

The archive must extract DLLs into `.deps/interop`. Keep the archive private and review the game's redistribution terms.
