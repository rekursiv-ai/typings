from collections.abc import Callable
from types import FunctionType
from typing import Generic, ParamSpec, Protocol, TypeVar

from numpy.typing import NDArray

import numpy as np

from triton.language import dtype

_P = ParamSpec("_P")
_R = TypeVar("_R")

class InterpretedFunction(Generic[_P, _R]):
    fn: FunctionType
    rewritten_fn: dict[Callable[..., object], Callable[..., object]]
    def __init__(self, fn: Callable[_P, _R]) -> None: ...
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
    def __getitem__(
        self,
        grid: tuple[int, ...] | Callable[[dict[str, int]], tuple[int, ...]],
    ) -> Callable[..., object]: ...

class TensorHandle:
    data: NDArray[np.generic]
    dtype: dtype
    def __init__(self, data: NDArray[np.generic], dtype: dtype) -> None: ...

class InterpreterBuilder:
    def binary_op(
        self,
        lhs: TensorHandle,
        rhs: TensorHandle,
        op: Callable[[NDArray[np.generic], NDArray[np.generic]], NDArray[np.generic]],
    ) -> TensorHandle: ...

# What ``_patch_lang_tensor`` reads of its scope, Triton's ``_LangPatchScope``.
class _SetAttr(Protocol):
    def set_attr(self, obj: object, name: str, value: object) -> None: ...

def _patch_lang_tensor(tensor: type, scope: _SetAttr) -> None: ...
