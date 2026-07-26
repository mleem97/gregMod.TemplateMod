using System.Collections.Concurrent;

namespace GregMod.TemplateMod.Infrastructure;

public static class MainThreadDispatcher
{
    private static readonly ConcurrentQueue<Action> Queue = new();

    public static void Enqueue(Action action)
    {
        ArgumentNullException.ThrowIfNull(action);
        Queue.Enqueue(action);
    }

    internal static void Drain(int maximumActions = 128)
    {
        for (int index = 0; index < maximumActions && Queue.TryDequeue(out Action? action); index++)
        {
            try
            {
                action();
            }
            catch (Exception exception)
            {
                ModLog.Error("A queued main-thread action failed.", exception);
            }
        }
    }
}
