from collections.abc import Sequence
from typing import Any, NamedTuple

from ._typing import Array, Device, DType, Namespace

__all__ = [
    "UniqueAllResult",
    "UniqueCountsResult",
    "UniqueInverseResult",
    "arange",
    "argsort",
    "ceil",
    "clip",
    "cumulative_prod",
    "cumulative_sum",
    "empty",
    "empty_like",
    "eye",
    "finfo",
    "floor",
    "full",
    "full_like",
    "iinfo",
    "isdtype",
    "linspace",
    "matmul",
    "matrix_transpose",
    "nonzero",
    "ones",
    "ones_like",
    "permute_dims",
    "reshape",
    "sign",
    "sort",
    "std",
    "tensordot",
    "trunc",
    "unique_all",
    "unique_counts",
    "unique_inverse",
    "unique_values",
    "unstack",
    "var",
    "vecdot",
    "zeros",
    "zeros_like",
]

def arange(
    start: float,
    /,
    stop: float | None = None,
    step: float = 1,
    *,
    xp: Namespace,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def empty(
    shape: int | tuple[int, ...],
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def empty_like(
    x: Array,
    /,
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def eye(
    n_rows: int,
    n_cols: int | None = None,
    /,
    *,
    xp: Namespace,
    k: int = 0,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def full(
    shape: int | tuple[int, ...],
    fill_value: complex,
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def full_like(
    x: Array,
    /,
    fill_value: complex,
    *,
    xp: Namespace,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def linspace(
    start: float,
    stop: float,
    /,
    num: int,
    *,
    xp: Namespace,
    dtype: DType | None = None,
    device: Device | None = None,
    endpoint: bool = True,
    **kwargs: object,
) -> Array: ...
def ones(
    shape: int | tuple[int, ...],
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def ones_like(
    x: Array,
    /,
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def zeros(
    shape: int | tuple[int, ...],
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...
def zeros_like(
    x: Array,
    /,
    xp: Namespace,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs: object,
) -> Array: ...

class UniqueAllResult(NamedTuple):
    values: Array
    indices: Array
    inverse_indices: Array
    counts: Array

class UniqueCountsResult(NamedTuple):
    values: Array
    counts: Array

class UniqueInverseResult(NamedTuple):
    values: Array
    inverse_indices: Array

def unique_all(x: Array, /, xp: Namespace) -> UniqueAllResult: ...
def unique_counts(x: Array, /, xp: Namespace) -> UniqueCountsResult: ...
def unique_inverse(x: Array, /, xp: Namespace) -> UniqueInverseResult: ...
def unique_values(x: Array, /, xp: Namespace) -> Array: ...
def std(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int | tuple[int, ...] | None = None,
    correction: float = 0.0,
    keepdims: bool = False,
    **kwargs: object,
) -> Array: ...
def var(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int | tuple[int, ...] | None = None,
    correction: float = 0.0,
    keepdims: bool = False,
    **kwargs: object,
) -> Array: ...
def cumulative_sum(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int | None = None,
    dtype: DType | None = None,
    include_initial: bool = False,
    **kwargs: object,
) -> Array: ...
def cumulative_prod(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int | None = None,
    dtype: DType | None = None,
    include_initial: bool = False,
    **kwargs: object,
) -> Array: ...
def clip(
    x: Array,
    /,
    min: float | Array | None = None,
    max: float | Array | None = None,
    *,
    xp: Namespace,
    out: Array | None = None,
) -> Array: ...
def permute_dims(x: Array, /, axes: tuple[int, ...], xp: Namespace) -> Array: ...
def reshape(
    x: Array,
    /,
    shape: tuple[int, ...],
    xp: Namespace,
    *,
    copy: bool | None = None,
    **kwargs: object,
) -> Array: ...
def argsort(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
    **kwargs: object,
) -> Array: ...
def sort(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
    **kwargs: object,
) -> Array: ...
def nonzero(x: Array, /, xp: Namespace, **kwargs: object) -> tuple[Array, ...]: ...
def ceil(x: Array, /, xp: Namespace, **kwargs: object) -> Array: ...
def floor(x: Array, /, xp: Namespace, **kwargs: object) -> Array: ...
def trunc(x: Array, /, xp: Namespace, **kwargs: object) -> Array: ...
def matmul(x1: Array, x2: Array, /, xp: Namespace, **kwargs: object) -> Array: ...
def matrix_transpose(x: Array, /, xp: Namespace) -> Array: ...
def tensordot(
    x1: Array,
    x2: Array,
    /,
    xp: Namespace,
    *,
    axes: int | tuple[Sequence[int], Sequence[int]] = 2,
    **kwargs: object,
) -> Array: ...
def vecdot(x1: Array, x2: Array, /, xp: Namespace, *, axis: int = -1) -> Array: ...
def isdtype(
    dtype: DType,
    kind: DType | str | tuple[DType | str, ...],
    xp: Namespace,
    *,
    _tuple: bool = True,
) -> bool: ...
def unstack(x: Array, /, xp: Namespace, *, axis: int = 0) -> tuple[Array, ...]: ...
def sign(x: Array, /, xp: Namespace, **kwargs: object) -> Array: ...
def finfo(type_: DType | Array, /, xp: Namespace) -> Any: ...
def iinfo(type_: DType | Array, /, xp: Namespace) -> Any: ...
