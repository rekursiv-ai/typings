"""Ship each ``stubs/<pkg>/`` as the PEP 561 stub-only package ``<pkg>-stubs``."""

from __future__ import annotations

from pathlib import Path
from typing import Final, cast, override

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.builders.wheel import WheelBuilderConfig


_CWD: Final = Path(__file__).resolve().parent
# createstub output for numpy's private names, which no consumer imports
# through turbojpeg.
_UNSHIPPED: Final = frozenset({Path("turbojpeg/numpy")})


class StubsBuildHook(BuildHookInterface[WheelBuilderConfig]):
    """Map every stub tree to ``<pkg>-stubs``; placeholder trees also to shared data."""

    PLUGIN_NAME = "custom"

    @override
    def initialize(self, version: str, build_data: dict[str, object]) -> None:
        del version
        force_include = cast(
            "dict[str, str]",
            build_data.setdefault("force_include", {}),
        )
        shared = cast("dict[str, str]", build_data.setdefault("shared_data", {}))
        stubs = _CWD / "stubs"
        for path in sorted(stubs.rglob("*.py*")):
            rel = path.relative_to(stubs)
            if path.suffix in {".py", ".pyi"} and not _UNSHIPPED & set(rel.parents):
                force_include[str(path)] = str(
                    Path(f"{rel.parts[0]}-stubs", *rel.parts[1:]),
                )
        for package in sorted(p for p in stubs.iterdir() if p.is_dir()):
            # A `-stubs` package resolves `.pyi` only, so a `.py` placeholder
            # (triton's, for a linux-only wheel) never reaches basedpyright's
            # `reportMissingModuleSource` check from there; the shared copy is
            # what a consumer's `extraPaths` names.
            if any(package.rglob("*.py")):
                shared[str(package)] = f"share/rekursiv-ai-typings/{package.name}"
