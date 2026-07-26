using MelonLoader;

namespace GregMod.TemplateMod.Infrastructure;

internal static class ModPreferences
{
    private static MelonPreferences_Category _category;
    private static MelonPreferences_Entry<bool> _enabled;
    private static MelonPreferences_Entry<bool> _showDebugHud;

    public static bool Enabled => _enabled?.Value ?? true;
    public static bool ShowDebugHud => _showDebugHud?.Value ?? false;

    public static void Initialize()
    {
        _category = MelonPreferences.CreateCategory(BuildInfo.Name, BuildInfo.Name);
        _enabled = _category.CreateEntry("Enabled", true, "Enable the mod");
        _showDebugHud = _category.CreateEntry("ShowDebugHud", false, "Show the template diagnostics HUD");
    }
}
