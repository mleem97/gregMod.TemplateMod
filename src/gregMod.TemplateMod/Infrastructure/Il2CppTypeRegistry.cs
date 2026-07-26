using Il2CppInterop.Runtime.Injection;

namespace GregMod.TemplateMod.Infrastructure;

internal static class Il2CppTypeRegistry
{
    private static bool _registered;

    public static void Register()
    {
        if (_registered)
        {
            return;
        }

        ClassInjector.RegisterTypeInIl2Cpp<PersistentHost>();
        _registered = true;
        ModLog.Info("Registered IL2CPP injected types.");
    }
}
