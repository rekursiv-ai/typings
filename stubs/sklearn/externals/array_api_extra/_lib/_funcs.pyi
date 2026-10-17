from collections.abc import Callable, Sequence
from types import ModuleType
from typing import overload

from ._utils._typing import Array

__all__ = [
    "apply_where",
    "atleast_nd",
    "broadcast_shapes",
    "cov",
    "create_diagonal",
    "expand_dims",
    "kron",
    "nunique",
    "pad",
    "setdiff1d",
    "sinc",
]

@overload
def apply_where(
    cond: Array,
    args: Array | tuple[Array, ...],
    f1: Callable[..., Array],
    f2: Callable[..., Array],
    /,
    *,
    xp: ModuleType | None = None,
) -> Array: ...
@overload
def apply_where(
    cond: Array,
    args: Array | tuple[Array, ...],
    f1: Callable[..., Array],
    /,
    *,
    fill_value: Array | complex,
    xp: ModuleType | None = None,
) -> Array: ...
def atleast_nd(x: Array, /, *, ndim: int, xp: ModuleType | None = None) -> Array: ...
def broadcast_shapes(*shapes: tuple[float | None, ...]) -> tuple[int | None, ...]: ...
def cov(m: Array, /, *, xp: ModuleType | None = None) -> Array: ...
def create_diagonal(
    x: Array,
    /,
    *,
    offset: int = 0,
    xp: ModuleType | None = None,
) -> Array: ...
def expand_dims(
    a: Array,
    /,
    *,
    axis: int | tuple[int, ...] = (0,),
    xp: ModuleType | None = None,
) -> Array: ...
def kron(
    a: Array | complex,
    b: Array | complex,
    /,
    *,
    xp: ModuleType | None = None,
) -> Array: ...
def nunique(x: Array, /, *, xp: ModuleType | None = None) -> Array: ...
def pad(
    x: Array,
    pad_width: int | tuple[int, int] | Sequence[tuple[int, int]],
    *,
    constant_values: complex = 0,
    xp: ModuleType,
) -> Array: ...
def setdiff1d(
    x1: Array | complex,
    x2: Array | complex,
    /,
    *,
    assume_unique: bool = False,
    xp: ModuleType | None = None,
) -> Array: ...
def sinc(x: Array, /, *, xp: ModuleType | None = None) -> Array: ...
