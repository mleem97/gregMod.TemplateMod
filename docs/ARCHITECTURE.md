# Architecture

## Lifecycle

`Core/TemplateMod.cs` owns the MelonLoader lifecycle. Keep lifecycle methods small and delegate work to feature classes.

Recommended flow:

1. initialize logging and preferences
2. apply Harmony patches
3. initialize features
4. dispatch `OnUpdate`, `OnGUI`, and scene events

## Folders

### `Core`

Assembly metadata and the MelonLoader entry point.

### `Features`

Project behavior that can be tested and reasoned about independently. Avoid placing Harmony attributes here unless the feature is itself a patch.

### `Infrastructure`

Logging, preferences, persistence, reflection helpers, and adapters around game or framework APIs.

### `Patches`

Harmony bootstrap and narrowly scoped patch classes.

Example patch shape:

```csharp
[HarmonyPatch(typeof(TargetType), nameof(TargetType.TargetMethod))]
internal static class TargetTypeTargetMethodPatch
{
    private static void Postfix(TargetType __instance)
    {
        // React to the original method.
    }
}
```

## Optional gregCore integration

When `references/gregCore.dll` exists, the project defines `GREGCORE` and adds the Melon dependency. Guard gregCore-specific source with:

```csharp
#if GREGCORE
using gregCore.API;
#endif
```

This keeps the base template buildable for standalone mods.

## Reference policy

Game and framework DLLs must not be committed. Use `references/` locally or point `GREGMOD_REFERENCE_ROOT` at a shared reference directory.

## Naming

- repository and assembly: `gregMod.FeatureName`
- namespace: `GregMod.FeatureName`
- mod GUID: reverse-domain-style stable identifier
- preferences category: assembly name
