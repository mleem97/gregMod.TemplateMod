#!/usr/bin/env bash
set -euo pipefail

CONFIGURATION="${1:-Release}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$ROOT/scripts/verify-env.py"
dotnet restore "$ROOT/gregMod.TemplateMod.sln"
dotnet build "$ROOT/gregMod.TemplateMod.sln" \
  --configuration "$CONFIGURATION" \
  --no-restore \
  --no-incremental

echo "Artifact directory: $ROOT/artifacts/$CONFIGURATION"
