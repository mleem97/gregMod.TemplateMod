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
TEMPLATE_GUID = "com.mleem97.gregmod.templatemod"
TEMPLATE_VERSION = "0.1.0"
PROJECT_PATTERN = re.compile(r"^gregMod\.[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z][A-Za-z0-9]*)*$")
TEXT_SUFFIXES = {".cs", ".csproj", ".props", ".md", ".py", ".ps1", ".sh", ".json", ".yml", ".yaml", ".sln"}
SKIP_PARTS = {".git", "bin", "obj", "artifacts", ".deps"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Project name, for example gregMod.InventoryPlus")
    parser.add_argument("--author", required=True, help="Author or GitHub username")
    parser.add_argument("--description", required=True, help="Short project description")
    parser.add_argument("--version", default=TEMPLATE_VERSION, help="Initial semantic version")
    parser.add_argument("--guid", help="Explicit stable mod GUID")
    return parser.parse_args()


def namespace_for(project_name: str) -> str:
    return "GregMod." + project_name.removeprefix("gregMod.")


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "", value.lower())
    return normalized or "author"


def replace_text(root: Path, replacements: list[tuple[str, str]]) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {"README.md"}:
            continue

        original = path.read_text(encoding="utf-8")
        updated = original
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != original:
            path.write_text(updated, encoding="utf-8")


def rename_paths(root: Path, project_name: str) -> None:
    old_dir = root / "src" / TEMPLATE_PROJECT
    old_project = old_dir / f"{TEMPLATE_PROJECT}.csproj"
    new_project = old_dir / f"{project_name}.csproj"
    if old_project.exists():
        old_project.rename(new_project)
    if old_dir.exists():
        old_dir.rename(root / "src" / project_name)

    old_solution = root / f"{TEMPLATE_PROJECT}.sln"
    if old_solution.exists():
        old_solution.rename(root / f"{project_name}.sln")


def main() -> int:
    args = parse_args()
    if not PROJECT_PATTERN.fullmatch(args.name):
        raise SystemExit("--name must look like gregMod.Example and contain valid C# namespace segments.")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", args.version):
        raise SystemExit("--version must be a semantic version such as 0.1.0.")

    root = Path(__file__).resolve().parent.parent
    marker = root / ".template-initialized"
    if marker.exists():
        raise SystemExit("This repository has already been initialized from the template.")

    new_namespace = namespace_for(args.name)
    new_guid = args.guid or f"com.{slug(args.author)}.{slug(args.name)}"
    replacements = [
        (TEMPLATE_GUID, new_guid),
        (TEMPLATE_NAMESPACE, new_namespace),
        (TEMPLATE_PROJECT, args.name),
        (TEMPLATE_DESCRIPTION, args.description),
        (TEMPLATE_AUTHOR, args.author),
        (TEMPLATE_VERSION, args.version),
    ]

    replace_text(root, replacements)
    rename_paths(root, args.name)
    marker.write_text(f"{args.name}\n", encoding="utf-8")

    print(f"Initialized {args.name}")
    print(f"Namespace: {new_namespace}")
    print(f"Mod GUID:  {new_guid}")
    print("Next: run scripts/setup-dev.py and then build.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
