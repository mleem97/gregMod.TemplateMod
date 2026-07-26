#!/usr/bin/env python3
"""Validate the .NET SDK and local IL2CPP build inputs."""

from __future__ import annotations

import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

REQUIRED = ("Assembly-CSharp.dll", "Il2Cppmscorlib.dll", "UnityEngine.CoreModule.dll")


def local_properties(root: Path) -> dict[str, str]:
    path = root / "Directory.Build.local.props"
    if not path.is_file():
        return {}
    tree = ET.parse(path)
    return {element.tag: (element.text or "").strip() for element in tree.findall(".//PropertyGroup/*")}


def expand(value: str, properties: dict[str, str]) -> str:
    for key, replacement in properties.items():
        value = value.replace(f"$({key})", replacement)
    return value


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    dotnet = shutil.which("dotnet")
    if not dotnet:
        print("ERROR: dotnet SDK is not installed.")
        return 1

    version = subprocess.check_output([dotnet, "--version"], text=True).strip()
    props = local_properties(root)

    game_dir = os.environ.get("GREGMOD_GAME_DIR") or props.get("GameDir", "")
    interop = os.environ.get("GREGMOD_INTEROP_DIR") or props.get("GameInteropDir", "")
    if not interop and game_dir:
        interop = str(Path(game_dir) / "MelonLoader" / "Il2CppAssemblies")
    if not interop:
        interop = str(root / ".deps" / "interop")
    interop = expand(interop, {**props, "GameDir": game_dir})

    interop_path = Path(interop).expanduser()
    missing = [name for name in REQUIRED if not (interop_path / name).is_file()]

    print(f".NET SDK:   {version}")
    print(f"Game:       {game_dir or 'not configured'}")
    print(f"Interop:    {interop_path}")
    print(f"Assemblies: {'OK' if not missing else 'missing ' + ', '.join(missing)}")

    if missing:
        print("Run: python scripts/setup-dev.py --game-dir \"/path/to/Data Center\"")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
