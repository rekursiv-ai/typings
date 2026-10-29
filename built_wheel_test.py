"""The stubs-only typings wheel ships its stub trees."""

from __future__ import annotations

import pytest

from lib.testing.wheel import built_wheel


pytestmark = pytest.mark.cli_uv


def test_the_wheel_ships_the_stub_trees() -> None:
    names = built_wheel("rekursiv-ai-typings", anchor=__file__).names()

    assert "yaml-stubs/__init__.pyi" in names


if __name__ == "__main__":
    from lib.testing.runner import test_main

    test_main(__file__)
