# Architecture

## Core

`TemplateMod` owns the MelonLoader lifecycle. Initialization is deliberately ordered:

1. logging
2. preferences
3. IL2CPP type registration
4. persistent host creation
5. Harmony patching
6. feature initialization

A failure during initialization is logged and rethrown so the loader reports a broken mod instead of leaving a partially initialized state.

## Features

Feature classes contain user-facing behavior. They should not know how dependencies are discovered or how patches are registered.

Prefer explicit lifecycle methods such as `Initialize`, `Tick`, `OnSceneLoaded`, and `Shutdown`.

## Infrastructure

- `ModLog` centralizes structured messages.
- `ModPreferences` owns MelonPreferences entries.
- `Il2CppTypeRegistry` registers injected managed types exactly once.
- `PersistentHost` provides an IL2CPP-compatible `MonoBehaviour`.
- `MainThreadDispatcher` safely schedules work from background callbacks.

## Patches

`PatchBootstrap` owns Harmony registration. Keep each patch small, document its target, and avoid broad `PatchAll` calls over unrelated assemblies.

The example patch is behind `TEMPLATE_EXAMPLE_PATCH` so the template builds without assuming a concrete game method.

## Optional gregCore

When `GregCorePath` points to an existing DLL, the project adds the reference and defines `GREGCORE`. The assembly metadata then declares the runtime dependency.

Keep gregCore-specific integrations behind `#if GREGCORE` or in a separate adapter folder so a standalone build remains possible.
