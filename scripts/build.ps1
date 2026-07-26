param(
    [ValidateSet("Debug", "Release")]
    [string]$Configuration = "Release"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot

python (Join-Path $PSScriptRoot "verify-env.py")
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

dotnet restore (Join-Path $Root "gregMod.TemplateMod.sln")
dotnet build (Join-Path $Root "gregMod.TemplateMod.sln") `
    --configuration $Configuration `
    --no-restore `
    --no-incremental

Write-Host "Artifact directory: $(Join-Path $Root "artifacts\$Configuration")" -ForegroundColor Green
