"""Check backend registration preserves compiler signatures in every decorator mode."""

from typing import assert_type

from torch import Tensor
from torch._dynamo.backends import registry
from torch._dynamo.backends.registry import (
    CompiledFn,
    register_backend,
    register_debug_backend,
    register_experimental_backend,
)

import pytest


def test_registration_preserves_compiler_signatures(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in ("_BACKENDS", "_COMPILER_FNS", "_BACKEND_TAGS"):
        monkeypatch.setattr(registry, name, {})

    regular = register_backend(_compiler, name="regular")
    regular_factory = register_backend(name="regular_factory")(_compiler)
    debug = register_debug_backend(_compiler, name="debug")
    debug_factory = register_debug_backend(name="debug_factory")(_compiler)
    experimental = register_experimental_backend(_compiler, name="experimental")
    experimental_factory = register_experimental_backend(name="experimental_factory")(
        _compiler,
    )

    assert_type(regular(object(), [], option=2), CompiledFn)
    assert_type(regular_factory(object(), [], option=2), CompiledFn)
    assert_type(debug(object(), [], option=2), CompiledFn)
    assert_type(debug_factory(object(), [], option=2), CompiledFn)
    assert_type(experimental(object(), [], option=2), CompiledFn)
    assert_type(experimental_factory(object(), [], option=2), CompiledFn)
    assert all(
        compiler is _compiler
        for compiler in (
            regular,
            regular_factory,
            debug,
            debug_factory,
            experimental,
            experimental_factory,
        )
    )
    assert registry.lookup_backend("regular") is _compiler


def _compiler(
    graph: object,
    inputs: list[Tensor],
    *,
    option: int = 2,
) -> CompiledFn:
    del graph, inputs, option
    return _compiled


def _compiled(*args: Tensor) -> tuple[Tensor, ...]:
    return args


if __name__ == "__main__":
    from lib.testing.runner import test_main

    test_main(__file__)
