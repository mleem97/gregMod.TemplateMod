#!/usr/bin/env python3
"""Create a release ZIP without development or game dependencies."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--configuration", default="Release", choices=("Debug", "Release"))
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    build_info = next((root / "src").glob("gregMod.*/BuildInfo.cs"))
    text = build_info.read_text(encoding="utf-8")
    name = re.search(r'Name = "([^"]+)"', text).group(1)
    version = re.search(r'Version = "([^"]+)"', text).group(1)

    artifact_dir = root / "artifacts" / args.configuration
    dll = artifact_dir / f"{name}.dll"
    if not dll.is_file():
        raise SystemExit(f"Build artifact not found: {dll}")

    output = root / "artifacts" / f"{name}-{version}.zip"
    include = [dll, root / "README.md", root / "CHANGELOG.md", root / "LICENSE"]
    optional = [artifact_dir / f"{name}.pdb", artifact_dir / f"{name}.xml"]

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in include + [p for p in optional if p.is_file()]:
            archive.write(path, arcname=path.name)

    print(f"Created: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
