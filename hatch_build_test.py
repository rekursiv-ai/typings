"""The wheel ships every stub tree as ``<pkg>-stubs`` and placeholders as data."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from hatch_build import layout


if TYPE_CHECKING:
    from pathlib import Path


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


if __name__ == "__main__":
    from lib.testing.runner import test_main

    test_main(__file__)
