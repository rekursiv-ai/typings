from collections.abc import Callable, Iterable
from types import ModuleType
from typing import Any, Generic, ParamSpec, TypeVar
from typing_extensions import TypeIs

from ._typing import Array, Device

__all__ = [
    "asarrays",
    "capabilities",
    "eager_shape",
    "in1d",
    "is_python_scalar",
    "jax_autojit",
    "mean",
    "meta_namespace",
    "pickle_flatten",
    "pickle_unflatten",
]

P = ParamSpec("P")
T = TypeVar("T")

def in1d(
    x1: Array,
    x2: Array,
    /,
    *,
    assume_unique: bool = False,
    invert: bool = False,
    xp: ModuleType | None = None,
) -> Array: ...
def mean(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    xp: ModuleType | None = None,
) -> Array: ...
def is_python_scalar(x: object) -> TypeIs[complex]: ...
def asarrays(
    a: Array | complex,
    b: Array | complex,
    xp: ModuleType,
) -> tuple[Array, Array]: ...
def eager_shape(x: Array, /) -> tuple[int, ...]: ...
def meta_namespace(
    *arrays: Array | complex | None,
    xp: ModuleType | None = None,
) -> ModuleType: ...
def capabilities(
    xp: ModuleType,
    *,
    device: Device | None = None,
) -> dict[str, int | None]: ...

type FlattenRest = tuple[object, ...]

def pickle_flatten(
    obj: object,
    cls: type[T] | tuple[type[T], ...],
) -> tuple[list[T], FlattenRest]: ...
def pickle_unflatten(instances: Iterable[object], rest: FlattenRest) -> Any: ...

class _AutoJITWrapper(Generic[T]):
    obj: T
    def __init__(self, obj: T) -> None: ...

def jax_autojit(func: Callable[P, T]) -> Callable[P, T]: ...
