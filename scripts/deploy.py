#!/usr/bin/env python3
"""Deploy the built mod DLL to the configured Data Center Mods directory."""

from __future__ import annotations

import argparse
import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path


def read_game_dir(root: Path) -> Path:
    env = os.environ.get("GREGMOD_GAME_DIR")
    if env:
        return Path(env).expanduser()

    props = root / "Directory.Build.local.props"
    if props.is_file():
        tree = ET.parse(props)
        value = tree.findtext(".//GameDir")
        if value:
            return Path(value).expanduser()

    raise SystemExit("GameDir is not configured. Run scripts/setup-dev.py.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--configuration", default="Release", choices=("Debug", "Release"))
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    candidates = list((root / "artifacts" / args.configuration).glob("gregMod.*.dll"))
    if len(candidates) != 1:
        raise SystemExit("Expected exactly one gregMod.*.dll artifact. Build the project first.")

    target_dir = read_game_dir(root) / "Mods"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / candidates[0].name
    shutil.copy2(candidates[0], target)
    print(f"Deployed: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
