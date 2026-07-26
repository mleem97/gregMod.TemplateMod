using GregMod.TemplateMod.Infrastructure;
using HarmonyLib;

namespace GregMod.TemplateMod.Patches;

internal static class PatchBootstrap
{
    public static void Apply(Harmony harmony)
    {
        harmony.PatchAll(typeof(PatchBootstrap).Assembly);
        ModLog.Info("Harmony patches applied.");
    }
}
