using MelonLoader;

namespace GregMod.TemplateMod.Infrastructure;

internal static class ModPreferences
{
    private static MelonPreferences_Entry<bool>? _enabled;
    private static MelonPreferences_Entry<bool>? _showDebugHud;

    public static bool Enabled => _enabled?.Value ?? true;
    public static bool ShowDebugHud => _showDebugHud?.Value ?? false;

    public static void Initialize()
    {
        MelonPreferences_Category category =
            MelonPreferences.CreateCategory(BuildInfo.Name, BuildInfo.Name);

        _enabled = category.CreateEntry("Enabled", true, "Enable mod");
        _showDebugHud = category.CreateEntry("ShowDebugHud", false, "Show template diagnostic HUD");
    }
}
