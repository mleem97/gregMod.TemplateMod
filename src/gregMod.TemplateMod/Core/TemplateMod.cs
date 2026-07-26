using GregMod.TemplateMod.Features;
using GregMod.TemplateMod.Infrastructure;
using GregMod.TemplateMod.Patches;
using MelonLoader;

namespace GregMod.TemplateMod.Core;

public sealed class TemplateMod : MelonMod
{
    private readonly ExampleFeature _feature = new();

    public override void OnInitializeMelon()
    {
        try
        {
            ModLog.Initialize(LoggerInstance);
            ModPreferences.Initialize();
            Il2CppTypeRegistry.Register();
            PersistentHost.Create();
            PatchBootstrap.Apply(HarmonyInstance);
            _feature.Initialize();

            ModLog.Info($"{BuildInfo.Name} {BuildInfo.Version} initialized.");
        }
        catch (Exception exception)
        {
            LoggerInstance.Error($"{BuildInfo.Name} failed to initialize: {exception}");
            throw;
        }
    }

    public override void OnUpdate()
    {
        MainThreadDispatcher.Drain();

        if (!ModPreferences.Enabled)
        {
            return;
        }

        try
        {
            _feature.Tick();
        }
        catch (Exception exception)
        {
            ModLog.Error("Feature update failed.", exception);
        }
    }

    public override void OnGUI()
    {
        if (ModPreferences.Enabled && ModPreferences.ShowDebugHud)
        {
            _feature.DrawDebugHud();
        }
    }

    public override void OnSceneWasLoaded(int buildIndex, string sceneName)
    {
        _feature.OnSceneLoaded(buildIndex, sceneName);
        ModLog.Info($"Scene loaded: {sceneName} ({buildIndex}).");
    }
}
