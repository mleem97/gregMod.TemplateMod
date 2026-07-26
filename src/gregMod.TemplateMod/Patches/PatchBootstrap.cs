using HarmonyLib;

namespace GregMod.TemplateMod.Patches;

internal static class PatchBootstrap
{
    public static void Apply(Harmony harmony)
    {
        ArgumentNullException.ThrowIfNull(harmony);
        harmony.PatchAll(typeof(PatchBootstrap).Assembly);
    }
}
