using UnityEngine;

namespace GregMod.TemplateMod.Features;

internal sealed class ExampleFeature
{
    private long _frameCount;
    private string _sceneName = "boot";

    public void Initialize()
    {
        _frameCount = 0;
    }

    public void Tick()
    {
        _frameCount++;
        // Add per-frame feature logic here.
    }

    public void OnSceneLoaded(int buildIndex, string sceneName)
    {
        _sceneName = sceneName;
    }

    public void DrawDebugHud()
    {
        GUI.Box(
            new Rect(20f, 20f, 360f, 90f),
            $"{BuildInfo.Name}\nScene: {_sceneName}\nFrames: {_frameCount}");
    }
}
