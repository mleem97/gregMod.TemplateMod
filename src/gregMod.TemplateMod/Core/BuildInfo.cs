using GregMod.TemplateMod.Core;
using MelonLoader;

[assembly: MelonInfo(typeof(TemplateMod), GregMod.TemplateMod.BuildInfo.Name, GregMod.TemplateMod.BuildInfo.Version, GregMod.TemplateMod.BuildInfo.Author)]
[assembly: MelonGame(GregMod.TemplateMod.BuildInfo.GameDeveloper, GregMod.TemplateMod.BuildInfo.GameName)]
#if GREGCORE
[assembly: MelonAdditionalDependencies("gregCore")]
#endif

namespace GregMod.TemplateMod;

public static class BuildInfo
{
    public const string Name = "gregMod.TemplateMod";
    public const string Version = "0.1.0";
    public const string Author = "mleem97";
    public const string Description = "Template mod for Data Center";
    public const string GameDeveloper = "Waseku";
    public const string GameName = "Data Center";
    public const string ModGuid = "com.mleem97.gregmod.templatemod";
}
