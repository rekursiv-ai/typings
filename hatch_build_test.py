"""The wheel ships every stub tree as ``<pkg>-stubs`` and placeholders as data."""

from __future__ import annotations

from pathlib import Path
from typing import Final, Protocol, cast

import pytest

from hatch_build import StubsBuildHook, layout


_CWD: Final = Path(__file__).resolve().parent


class _Hook(Protocol):
    def initialize(self, version: str, build_data: dict[str, object]) -> None: ...


class _HookClass(Protocol):
    def __call__(
        self,
        *,
        root: str,
        config: dict[str, object],
        build_config: object,
        metadata: object,
        directory: str,
        target_name: str,
    ) -> _Hook: ...


@pytest.fixture
def stubs(tmp_path: Path) -> Path:
    root = tmp_path / "typings"
    for rel, text in {
        "yaml/__init__.pyi": "",
        "yaml/nodes.pyi": "",
        "fastapi/testclient.pyi": "",
        "fastapi/py.typed": "partial\n",
        "triton/__init__.pyi": "",
        "triton/__init__.py": "",
        "yaml/notes.txt": "",
    }.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text)
    return root


def test_each_tree_ships_as_its_stubs_package(stubs: Path) -> None:
    force_include, _ = layout(stubs)
    assert force_include[str(stubs / "yaml" / "nodes.pyi")] == "yaml-stubs/nodes.pyi"
    assert str(stubs / "yaml" / "notes.txt") not in force_include


def test_a_partial_tree_keeps_its_marker(stubs: Path) -> None:
    force_include, _ = layout(stubs)
    assert (
        force_include[str(stubs / "fastapi" / "py.typed")] == "fastapi-stubs/py.typed"
    )


def test_only_placeholder_trees_ship_as_shared_data(stubs: Path) -> None:
    _, shared_data = layout(stubs)
    assert shared_data == {
        str(stubs / "triton"): "share/rekursiv-ai-typings/triton",
    }


def test_an_optional_import_ships_a_placeholder() -> None:
    # Trackinizer imports aiortc under TYPE_CHECKING without depending on it.
    stubs = _CWD / "typings"
    _, shared_data = layout(stubs)
    assert shared_data[str(stubs / "aiortc")] == "share/rekursiv-ai-typings/aiortc"


def test_initialize_adds_the_layout_to_existing_build_data(stubs: Path) -> None:
    hook = cast("_HookClass", StubsBuildHook)(
        root=str(stubs.parent),
        config={},
        build_config=object(),
        metadata=object(),
        directory=str(stubs.parent / "dist"),
        target_name="wheel",
    )
    build_data: dict[str, object] = {
        "force_include": {"LICENSE": "LICENSE"},
        "shared_data": {"a": "share/a"},
    }

    hook.initialize("standard", build_data)

    force_include, shared_data = layout(stubs)
    assert build_data == {
        "force_include": {"LICENSE": "LICENSE", **force_include},
        "shared_data": {"a": "share/a", **shared_data},
    }


if __name__ == "__main__":
    from lib.testing.runner import test_main

    test_main(__file__)
