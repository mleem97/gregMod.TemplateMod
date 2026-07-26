using MelonLoader;

namespace GregMod.TemplateMod.Infrastructure;

internal static class ModLog
{
    private static MelonLogger.Instance? _logger;

    public static void Initialize(MelonLogger.Instance logger) => _logger = logger;

    public static void Info(string message) => _logger?.Msg(message);

    public static void Warning(string message) => _logger?.Warning(message);

    public static void Error(string message, Exception? exception = null)
    {
        _logger?.Error(exception is null ? message : $"{message}{Environment.NewLine}{exception}");
    }
}
