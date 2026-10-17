from collections.abc import Sequence
from typing import Any, Literal

from _typeshed import Incomplete

from ._info import __array_namespace_info__ as __array_namespace_info__
from ._typing import Array, Device, DType
from ..common._aliases import (
    UniqueAllResult as UniqueAllResult,
    UniqueCountsResult as UniqueCountsResult,
    UniqueInverseResult as UniqueInverseResult,
)
from ..common._typing import NestedSequence, SupportsBufferProtocol

__all__ = [
    "UniqueAllResult",
    "UniqueCountsResult",
    "UniqueInverseResult",
    "__array_namespace_info__",
    "add",
    "all",
    "any",
    "arange",
    "asarray",
    "astype",
    "atan2",
    "bitwise_and",
    "bitwise_invert",
    "bitwise_left_shift",
    "bitwise_or",
    "bitwise_right_shift",
    "bitwise_xor",
    "broadcast_arrays",
    "broadcast_to",
    "can_cast",
    "clip",
    "concat",
    "conj",
    "copysign",
    "count_nonzero",
    "cumulative_prod",
    "cumulative_sum",
    "diff",
    "divide",
    "empty",
    "equal",
    "expand_dims",
    "eye",
    "finfo",
    "flip",
    "floor_divide",
    "full",
    "greater",
    "greater_equal",
    "hypot",
    "iinfo",
    "isdtype",
    "less",
    "less_equal",
    "linspace",
    "logaddexp",
    "matmul",
    "matrix_transpose",
    "max",
    "maximum",
    "mean",
    "meshgrid",
    "min",
    "minimum",
    "multiply",
    "newaxis",
    "nonzero",
    "not_equal",
    "ones",
    "permute_dims",
    "pow",
    "prod",
    "remainder",
    "repeat",
    "reshape",
    "result_type",
    "roll",
    "sign",
    "sort",
    "squeeze",
    "std",
    "subtract",
    "sum",
    "take",
    "take_along_axis",
    "tensordot",
    "tril",
    "triu",
    "unique_all",
    "unique_counts",
    "unique_inverse",
    "unique_values",
    "unstack",
    "var",
    "vecdot",
    "where",
    "zeros",
]

def result_type(*arrays_and_dtypes: Array | DType | bool | complex) -> DType: ...
def can_cast(from_: DType | Array, to: DType, /) -> bool: ...

bitwise_invert: Incomplete
newaxis: Incomplete
conj: Incomplete
add: Incomplete
atan2: Incomplete
bitwise_and: Incomplete
bitwise_left_shift: Incomplete
bitwise_or: Incomplete
bitwise_right_shift: Incomplete
bitwise_xor: Incomplete
copysign: Incomplete
divide: Incomplete
equal: Incomplete
floor_divide: Incomplete
greater: Incomplete
greater_equal: Incomplete
hypot: Incomplete
less: Incomplete
less_equal: Incomplete
logaddexp: Incomplete
maximum: Incomplete
minimum: Incomplete
multiply: Incomplete
not_equal: Incomplete
pow: Incomplete
remainder: Incomplete
subtract: Incomplete

def asarray(
    obj: Array
    | bool
    | complex
    | NestedSequence[bool | int | float | complex]
    | SupportsBufferProtocol,
    /,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    copy: bool | None = None,
    **kwargs: Any,
) -> Array: ...
def max(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
) -> Array: ...
def min(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
) -> Array: ...

clip: Incomplete
unstack: Incomplete
cumulative_sum: Incomplete
cumulative_prod: Incomplete
finfo: Incomplete
iinfo: Incomplete

def sort(
    x: Array,
    /,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
    **kwargs,
) -> Array: ...
def prod(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    dtype: DType | None = None,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def sum(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    dtype: DType | None = None,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def any(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def all(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def mean(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def std(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    correction: float = 0.0,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def var(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    correction: float = 0.0,
    keepdims: bool = False,
    **kwargs,
) -> Array: ...
def concat(
    arrays: tuple[Array, ...] | list[Array],
    /,
    *,
    axis: int | None = 0,
    **kwargs,
) -> Array: ...
def squeeze(x: Array, /, axis: int | tuple[int, ...]) -> Array: ...
def broadcast_to(x: Array, /, shape: tuple[int, ...], **kwargs) -> Array: ...
def permute_dims(x: Array, /, axes: tuple[int, ...]) -> Array: ...
def flip(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    **kwargs,
) -> Array: ...
def roll(
    x: Array,
    /,
    shift: int | tuple[int, ...],
    *,
    axis: int | tuple[int, ...] | None = None,
    **kwargs,
) -> Array: ...
def nonzero(x: Array, /, **kwargs) -> tuple[Array, ...]: ...
def diff(
    x: Array,
    /,
    *,
    axis: int = -1,
    n: int = 1,
    prepend: Array | None = None,
    append: Array | None = None,
) -> Array: ...
def count_nonzero(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
) -> Array: ...
def repeat(x: Array, repeats: int | Array, /, *, axis: int | None = None) -> Array: ...
def where(
    condition: Array,
    x1: Array | bool | complex,
    x2: Array | bool | complex,
    /,
) -> Array: ...
def reshape(
    x: Array,
    /,
    shape: tuple[int, ...],
    *,
    copy: bool | None = None,
    **kwargs,
) -> Array: ...
def arange(
    start: float,
    /,
    stop: float | None = None,
    step: float = 1,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs,
) -> Array: ...
def eye(
    n_rows: int,
    n_cols: int | None = None,
    /,
    *,
    k: int = 0,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs,
) -> Array: ...
def linspace(
    start: float,
    stop: float,
    /,
    num: int,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    endpoint: bool = True,
    **kwargs,
) -> Array: ...
def full(
    shape: int | tuple[int, ...],
    fill_value: bool | complex,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs,
) -> Array: ...
def ones(
    shape: int | tuple[int, ...],
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs,
) -> Array: ...
def zeros(
    shape: int | tuple[int, ...],
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs,
) -> Array: ...
def empty(
    shape: int | tuple[int, ...],
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    **kwargs,
) -> Array: ...
def tril(x: Array, /, *, k: int = 0) -> Array: ...
def triu(x: Array, /, *, k: int = 0) -> Array: ...
def expand_dims(x: Array, /, *, axis: int = 0) -> Array: ...
def astype(
    x: Array,
    dtype: DType,
    /,
    *,
    copy: bool = True,
    device: Device | None = None,
) -> Array: ...
def broadcast_arrays(*arrays: Array) -> list[Array]: ...
def unique_all(x: Array) -> UniqueAllResult: ...
def unique_counts(x: Array) -> UniqueCountsResult: ...
def unique_inverse(x: Array) -> UniqueInverseResult: ...
def unique_values(x: Array) -> Array: ...
def matmul(x1: Array, x2: Array, /, **kwargs) -> Array: ...

matrix_transpose: Incomplete

def vecdot(x1: Array, x2: Array, /, *, axis: int = -1) -> Array: ...
def tensordot(
    x1: Array,
    x2: Array,
    /,
    *,
    axes: int | tuple[Sequence[int], Sequence[int]] = 2,
    **kwargs,
) -> Array: ...
def isdtype(
    dtype: DType,
    kind: DType | str | tuple[DType | str, ...],
    *,
    _tuple: bool = True,
) -> bool: ...
def take(
    x: Array,
    indices: Array,
    /,
    *,
    axis: int | None = None,
    **kwargs,
) -> Array: ...
def take_along_axis(x: Array, indices: Array, /, *, axis: int = -1) -> Array: ...
def sign(x: Array, /) -> Array: ...
def meshgrid(*arrays: Array, indexing: Literal["xy", "ij"] = "xy") -> list[Array]: ...
