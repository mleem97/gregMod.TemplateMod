#!/usr/bin/env python3
"""Rename and configure a repository created from gregMod.TemplateMod."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TEMPLATE_PROJECT = "gregMod.TemplateMod"
TEMPLATE_NAMESPACE = "GregMod.TemplateMod"
TEMPLATE_AUTHOR = "mleem97"
TEMPLATE_DESCRIPTION = "Template mod for Data Center"
PROJECT_PATTERN = re.compile(r"^gregMod\.[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z][A-Za-z0-9]*)*$")
TEXT_SUFFIXES = {".cs", ".csproj", ".props", ".md", ".py", ".ps1", ".sh", ".json", ".yml", ".yaml"}
SKIP_PARTS = {".git", "bin", "obj", "artifacts"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Project name, for example gregMod.InventoryPlus")
    parser.add_argument("--author", required=True, help="Author or GitHub username")
    parser.add_argument("--description", required=True, help="Short project description")
    return parser.parse_args()


def namespace_for(project_name: str) -> str:
    return "GregMod." + project_name.removeprefix("gregMod.")


def replace_text(root: Path, replacements: dict[str, str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {"README.md"}:
            continue

        original = path.read_text(encoding="utf-8")
        updated = original
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != original:
            path.write_text(updated, encoding="utf-8")


def rename_project_paths(root: Path, project_name: str) -> None:
    old_directory = root / "src" / TEMPLATE_PROJECT
    old_project = old_directory / f"{TEMPLATE_PROJECT}.csproj"
    new_project = old_directory / f"{project_name}.csproj"
    new_directory = root / "src" / project_name

    if old_project.exists():
        old_project.rename(new_project)
    if old_directory.exists() and old_directory != new_directory:
        old_directory.rename(new_directory)


def main() -> int:
    args = parse_args()
    if not PROJECT_PATTERN.fullmatch(args.name):
        raise SystemExit("--name must look like gregMod.Example and contain valid C# namespace segments.")

    root = Path(__file__).resolve().parent.parent
    marker = root / ".template-initialized"
    if marker.exists():
        raise SystemExit("This repository has already been initialized from the template.")

    new_namespace = namespace_for(args.name)
    replacements = {
        TEMPLATE_NAMESPACE: new_namespace,
        TEMPLATE_PROJECT: args.name,
        TEMPLATE_AUTHOR: args.author,
        TEMPLATE_DESCRIPTION: args.description,
        "com.mleem97.gregmod.templatemod": f"com.{args.author.lower()}.{args.name.lower().replace('.', '')}",
    }

    replace_text(root, replacements)
    rename_project_paths(root, args.name)
    marker.write_text(f"{args.name}\n", encoding="utf-8")

    print(f"Initialized {args.name}")
    print("Next steps:")
    print("  1. Populate references/ or set GREGMOD_REFERENCE_ROOT.")
    print("  2. Run scripts/build.ps1 or scripts/build.sh.")
    print("  3. Replace ExampleFeature with project logic.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
