# Local references

Do not commit DLLs to this directory.

The preferred setup is to run:

```bash
python scripts/setup-dev.py --game-dir "/path/to/Data Center"
```

The project then references the generated proxy assemblies directly from `MelonLoader/Il2CppAssemblies`.

For an isolated or CI build, place the generated proxy assemblies in `.deps/interop/` or set `GREGMOD_INTEROP_DIR`.
