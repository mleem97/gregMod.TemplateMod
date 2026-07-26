#!/usr/bin/env python3
"""Configure local Data Center and IL2CPP assembly paths."""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

REQUIRED = ("Assembly-CSharp.dll", "Il2Cppmscorlib.dll", "UnityEngine.CoreModule.dll")


def candidates() -> list[Path]:
    values: list[Path] = []
    env = os.environ.get("GREGMOD_GAME_DIR")
    if env:
        values.append(Path(env).expanduser())

    home = Path.home()
    values.extend(
        [
            Path(r"C:\Program Files (x86)\Steam\steamapps\common\Data Center"),
            Path(r"C:\Program Files\Steam\steamapps\common\Data Center"),
            home / ".local/share/Steam/steamapps/common/Data Center",
            home / ".steam/steam/steamapps/common/Data Center",
        ]
    )
    return values


def find_game_dir(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()

    for candidate in candidates():
        if candidate.is_dir():
            return candidate.resolve()

    raise SystemExit("Game directory not found. Pass --game-dir or set GREGMOD_GAME_DIR.")


def validate_interop(path: Path) -> None:
    missing = [name for name in REQUIRED if not (path / name).is_file()]
    if missing:
        joined = ", ".join(missing)
        raise SystemExit(
            f"Invalid interop directory: {path}\nMissing: {joined}\n"
            "Install MelonLoader, launch the game once, and retry."
        )


def write_props(root: Path, game_dir: Path, interop_dir: Path, gregcore: Path | None) -> None:
    lines = [
        "<Project>",
        "  <PropertyGroup>",
        f"    <GameDir>{escape(game_dir.as_posix())}</GameDir>",
        f"    <GameInteropDir>{escape(interop_dir.as_posix())}</GameInteropDir>",
    ]
    if gregcore:
        lines.append(f"    <GregCorePath>{escape(gregcore.as_posix())}</GregCorePath>")
    lines.extend(["  </PropertyGroup>", "</Project>", ""])
    (root / "Directory.Build.local.props").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game-dir", help="Data Center installation directory")
    parser.add_argument("--interop-dir", help="Override MelonLoader/Il2CppAssemblies")
    parser.add_argument("--gregcore-dll", help="Optional gregCore.dll path")
    parser.add_argument("--copy-interop", action="store_true", help="Copy proxies into .deps/interop")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    game_dir = find_game_dir(args.game_dir)
    interop = (
        Path(args.interop_dir).expanduser().resolve()
        if args.interop_dir
        else game_dir / "MelonLoader" / "Il2CppAssemblies"
    )
    validate_interop(interop)

    if args.copy_interop:
        destination = root / ".deps" / "interop"
        destination.mkdir(parents=True, exist_ok=True)
        for source in interop.glob("*.dll"):
            shutil.copy2(source, destination / source.name)
        interop = destination.resolve()

    gregcore: Path | None = None
    if args.gregcore_dll:
        gregcore = Path(args.gregcore_dll).expanduser().resolve()
        if not gregcore.is_file():
            raise SystemExit(f"gregCore DLL not found: {gregcore}")
    else:
        candidate = game_dir / "Mods" / "gregCore.dll"
        if candidate.is_file():
            gregcore = candidate.resolve()

    write_props(root, game_dir, interop, gregcore)
    print(f"Game:       {game_dir}")
    print(f"Interop:    {interop}")
    print(f"gregCore:   {gregcore or 'not configured'}")
    print("Wrote Directory.Build.local.props")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
