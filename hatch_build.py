"""Ship each ``typings/<pkg>/`` as the PEP 561 stub-only package ``<pkg>-stubs``."""

from __future__ import annotations

from pathlib import Path
from typing import cast, override

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.builders.wheel import WheelBuilderConfig


def layout(stubs: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Map a stub root onto the wheel.

    Args:
      stubs: Directory holding one ``<pkg>/`` tree per library.

    Returns:
      force_include: Source file to its path under ``<pkg>-stubs/``.
      shared_data: Placeholder tree to its ``share/rekursiv-ai-typings/`` path.

    """
    force_include: dict[str, str] = {}
    for path in sorted(stubs.rglob("*")):
        rel = path.relative_to(stubs)
        # `py.typed` saying `partial` marks a tree that stubs only some
        # modules, so the checkers fall back to the library for the rest.
        if path.suffix in {".py", ".pyi"} or path.name == "py.typed":
            # A tree already named ``<pkg>-stubs`` (pyrefly treats only those
            # as typed) ships under that name.
            package = f"{rel.parts[0].removesuffix('-stubs')}-stubs"
            force_include[str(path)] = str(Path(package, *rel.parts[1:]))
    # A `-stubs` package resolves `.pyi` only, so a `.py` placeholder (triton's,
    # for a linux-only wheel) never reaches basedpyright's
    # `reportMissingModuleSource` check from there; the shared copy is what a
    # consumer's `extraPaths` names.
    shared_data = {
        str(package): f"share/rekursiv-ai-typings/{package.name}"
        for package in sorted(p for p in stubs.iterdir() if p.is_dir())
        if any(package.rglob("*.py"))
    }
    return force_include, shared_data


class StubsBuildHook(BuildHookInterface[WheelBuilderConfig]):
    """Register ``layout`` of the project's ``typings/`` with the wheel."""

    PLUGIN_NAME = "custom"

    @override
    def initialize(self, version: str, build_data: dict[str, object]) -> None:
        del version
        force_include, shared_data = layout(Path(self.root) / "typings")
        cast(
            "dict[str, str]",
            build_data.setdefault("force_include", {}),
        ).update(force_include)
        cast("dict[str, str]", build_data.setdefault("shared_data", {})).update(
            shared_data,
        )
