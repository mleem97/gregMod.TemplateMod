param(
    [ValidateSet("Debug", "Release")]
    [string]$Configuration = "Release"
)

$ErrorActionPreference = "Stop"
$RepositoryRoot = Split-Path -Parent $PSScriptRoot
$Project = Get-ChildItem -Path (Join-Path $RepositoryRoot "src") -Filter "*.csproj" -Recurse | Select-Object -First 1
$Output = Join-Path $RepositoryRoot "artifacts"

if (-not $Project) {
    throw "No .csproj file found below src/."
}

New-Item -ItemType Directory -Path $Output -Force | Out-Null
Write-Host "Building $($Project.Name) [$Configuration]" -ForegroundColor Cyan

dotnet build $Project.FullName --configuration $Configuration --output $Output --no-incremental

Write-Host "Build output: $Output" -ForegroundColor Green
