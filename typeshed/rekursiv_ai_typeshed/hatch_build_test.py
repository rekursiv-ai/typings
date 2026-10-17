"""The wheel hook registers the built tree as shared data, then removes it."""

from __future__ import annotations

from importlib.machinery import ModuleSpec
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import TYPE_CHECKING, Final, Protocol, cast

from hatchling.builders.wheel import WheelBuilder

import pytest


if TYPE_CHECKING:
    from types import ModuleType


_CWD: Final = Path(__file__).resolve().parent

# Stands in for ``build.py``, which the hook loads from its ``_CWD``: the real one
# copies 7k stub files, which is ``test_wheel_build_removes_its_temp_tree``'s job.
_FAKE_BUILD: Final = '''
from pathlib import Path


def build(target: Path) -> None:
    """Write one marker directory where the real build writes its trees."""
    (target / "ty").mkdir(parents=True)
'''


class _Hook(Protocol):
    def initialize(self, version: str, build_data: dict[str, object]) -> None: ...

    def finalize(
        self,
        version: str,
        build_data: dict[str, object],
        artifact_path: str,
    ) -> None: ...


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


# By path: the wheel omits ``hatch_build.py``, so an installed package has no
# ``rekursiv_ai_typeshed.hatch_build`` to import.
@pytest.fixture
def hook_module(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    (tmp_path / "build.py").write_text(_FAKE_BUILD)
    spec = spec_from_file_location("hatch_build_under_test", _CWD / "hatch_build.py")
    assert spec is not None
    assert spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "_CWD", tmp_path)
    return module


@pytest.fixture
def hook(hook_module: ModuleType, tmp_path: Path) -> _Hook:
    hook_class = cast("_HookClass", hook_module.TypeshedBuildHook)
    builder = WheelBuilder(str(_CWD.parent))
    return hook_class(
        root=str(_CWD.parent),
        config={},
        build_config=cast("object", builder.config),
        metadata=cast("object", builder.metadata),
        directory=str(tmp_path / "dist"),
        target_name="wheel",
    )


def test_initialize_ships_the_tree_and_finalize_removes_it(hook: _Hook) -> None:
    build_data: dict[str, object] = {}
    hook.initialize("standard", build_data)
    shared = cast("dict[str, str]", build_data["shared_data"])
    ((source, destination),) = shared.items()
    assert destination == "share/rekursiv-ai-typeshed"
    assert (Path(source) / "ty").is_dir()
    hook.finalize("standard", build_data, "unused.whl")
    assert not Path(source).exists()


def test_finalize_before_initialize_is_rejected(hook: _Hook) -> None:
    with pytest.raises(ValueError, match="_scratch is not None"):
        hook.finalize("standard", {}, "unused.whl")


@pytest.mark.parametrize(
    ("spec", "match"),
    [
        (None, r"^Expected spec is not None\.$"),
        (ModuleSpec("build", None), r"^Expected spec\.loader is not None\.$"),
    ],
)
def test_initialize_rejects_an_unloadable_build_module(
    hook_module: ModuleType,
    hook: _Hook,
    monkeypatch: pytest.MonkeyPatch,
    spec: ModuleSpec | None,
    match: str,
) -> None:
    def spec_from_file_location(*_: object) -> ModuleSpec | None:
        return spec

    monkeypatch.setattr(hook_module, "spec_from_file_location", spec_from_file_location)
    with pytest.raises(ValueError, match=match):
        hook.initialize("standard", {})


if __name__ == "__main__":
    from lib.testing.runner import test_main

    test_main(__file__)
