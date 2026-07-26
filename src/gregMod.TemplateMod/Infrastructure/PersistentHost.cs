using UnityEngine;

namespace GregMod.TemplateMod.Infrastructure;

public sealed class PersistentHost : MonoBehaviour
{
    private static PersistentHost? _instance;

    public PersistentHost(IntPtr pointer)
        : base(pointer)
    {
    }

    public static void Create()
    {
        if (_instance is not null)
        {
            return;
        }

        GameObject host = new($"{BuildInfo.Name}.Host");
        UnityEngine.Object.DontDestroyOnLoad(host);
        host.hideFlags = HideFlags.HideAndDontSave;
        _instance = host.AddComponent<PersistentHost>();
        ModLog.Info("Created persistent IL2CPP host.");
    }

    private void Update() => MainThreadDispatcher.Drain();

    private void OnDestroy()
    {
        if (_instance == this)
        {
            _instance = null;
        }
    }
}
