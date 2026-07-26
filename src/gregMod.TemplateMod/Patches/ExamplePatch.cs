#if TEMPLATE_EXAMPLE_PATCH
using System.Reflection;
using GregMod.TemplateMod.Infrastructure;
using HarmonyLib;

namespace GregMod.TemplateMod.Patches;

[HarmonyPatch]
internal static class ExamplePatch
{
    private static MethodBase TargetMethod()
    {
        Type targetType = AccessTools.TypeByName("Namespace.GameType")
            ?? throw new MissingMemberException("Target game type was not found.");

        return AccessTools.Method(targetType, "TargetMethod")
            ?? throw new MissingMethodException(targetType.FullName, "TargetMethod");
    }

    private static void Postfix()
    {
        ModLog.Info("Example patch executed.");
    }
}
#endif
