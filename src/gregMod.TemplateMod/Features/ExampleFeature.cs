using UnityEngine;

namespace GregMod.TemplateMod.Features;

internal sealed class ExampleFeature
{
    private string _sceneName = "not loaded";
    private long _ticks;

    public void Initialize()
    {
        _ticks = 0;
    }

    public void Tick()
    {
        _ticks++;
    }

    public void OnSceneLoaded(int buildIndex, string sceneName)
    {
        _sceneName = $"{sceneName} ({buildIndex})";
    }

    public void DrawDebugHud()
    {
        GUI.Box(
            new Rect(20, 20, 360, 90),
            $"{BuildInfo.Name} {BuildInfo.Version}\nScene: {_sceneName}\nTicks: {_ticks}");
    }
}
