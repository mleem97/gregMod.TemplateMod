using System;
using GregMod.TemplateMod.Features;
using GregMod.TemplateMod.Infrastructure;
using GregMod.TemplateMod.Patches;
using MelonLoader;

namespace GregMod.TemplateMod.Core;

public sealed class TemplateMod : MelonMod
{
    public static TemplateMod Instance { get; private set; }

    private readonly ExampleFeature _exampleFeature = new();

    public override void OnInitializeMelon()
    {
        try
        {
            Instance = this;
            ModLog.Initialize(LoggerInstance);
            ModPreferences.Initialize();
            PatchBootstrap.Apply(HarmonyInstance);
            _exampleFeature.Initialize();

            ModLog.Info($"{BuildInfo.Name} {BuildInfo.Version} loaded.");
        }
        catch (Exception exception)
        {
            LoggerInstance.Error($"{BuildInfo.Name} failed to initialize: {exception}");
            throw;
        }
    }

    public override void OnUpdate()
    {
        if (!ModPreferences.Enabled)
        {
            return;
        }

        try
        {
            _exampleFeature.Tick();
        }
        catch (Exception exception)
        {
            ModLog.Error("Update failed", exception);
        }
    }

    public override void OnGUI()
    {
        if (!ModPreferences.Enabled || !ModPreferences.ShowDebugHud)
        {
            return;
        }

        _exampleFeature.DrawDebugHud();
    }

    public override void OnSceneWasLoaded(int buildIndex, string sceneName)
    {
        _exampleFeature.OnSceneLoaded(buildIndex, sceneName);
        ModLog.Info($"Scene loaded: {sceneName} ({buildIndex})");
    }
}
