# Local assembly references

Place development-only game and loader DLLs in this directory. DLLs are ignored by Git.

Required by the default project:

- `MelonLoader.dll`
- `0Harmony.dll`
- `Il2CppInterop.Runtime.dll`
- `Il2Cppmscorlib.dll`
- `Assembly-CSharp.dll`
- `UnityEngine.CoreModule.dll`
- `UnityEngine.IMGUIModule.dll`
- `UnityEngine.PhysicsModule.dll`
- `UnityEngine.TextRenderingModule.dll`
- `UnityEngine.UI.dll`
- `UnityEngine.UIModule.dll`
- `Unity.InputSystem.dll`
- `Unity.TextMeshPro.dll`

Optional:

- `gregCore.dll`

Instead of copying files here, set `GREGMOD_REFERENCE_ROOT` to another directory containing the DLLs.
