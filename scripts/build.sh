#!/usr/bin/env bash
set -euo pipefail

CONFIGURATION="${1:-Release}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT="$(find "$ROOT/src" -name '*.csproj' -type f | head -n 1)"
OUTPUT="$ROOT/artifacts"

if [[ -z "$PROJECT" ]]; then
  echo "No .csproj file found below src/." >&2
  exit 1
fi

mkdir -p "$OUTPUT"
echo "Building $(basename "$PROJECT") [$CONFIGURATION]"
dotnet build "$PROJECT" --configuration "$CONFIGURATION" --output "$OUTPUT" --no-incremental
echo "Build output: $OUTPUT"
