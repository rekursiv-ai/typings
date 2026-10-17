from builtins import bool as py_bool
from typing import Any

from _typeshed import Incomplete

from ._info import __array_namespace_info__ as __array_namespace_info__
from ._typing import Array, Device, DType
from ..common._typing import NestedSequence, SupportsBufferProtocol

__all__ = [
    "UniqueAllResult",
    "UniqueCountsResult",
    "UniqueInverseResult",
    "__array_namespace_info__",
    "acos",
    "acosh",
    "arange",
    "argsort",
    "asarray",
    "asin",
    "asinh",
    "astype",
    "atan",
    "atan2",
    "atanh",
    "bitwise_invert",
    "bitwise_left_shift",
    "bitwise_right_shift",
    "bool",
    "ceil",
    "clip",
    "concat",
    "count_nonzero",
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
    "pow",
    "reshape",
    "sign",
    "sort",
    "std",
    "take_along_axis",
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

bool: Incomplete
acos: Incomplete
acosh: Incomplete
asin: Incomplete
asinh: Incomplete
atan: Incomplete
atan2: Incomplete
atanh: Incomplete
bitwise_left_shift: Incomplete
bitwise_invert: Incomplete
bitwise_right_shift: Incomplete
concat: Incomplete
pow: Incomplete
arange: Incomplete
empty: Incomplete
empty_like: Incomplete
eye: Incomplete
full: Incomplete
full_like: Incomplete
linspace: Incomplete
ones: Incomplete
ones_like: Incomplete
zeros: Incomplete
zeros_like: Incomplete
UniqueAllResult: Incomplete
UniqueCountsResult: Incomplete
UniqueInverseResult: Incomplete
unique_all: Incomplete
unique_counts: Incomplete
unique_inverse: Incomplete
unique_values: Incomplete
std: Incomplete
var: Incomplete
cumulative_sum: Incomplete
cumulative_prod: Incomplete
clip: Incomplete
permute_dims: Incomplete
reshape: Incomplete
argsort: Incomplete
sort: Incomplete
nonzero: Incomplete
ceil: Incomplete
floor: Incomplete
trunc: Incomplete
matmul: Incomplete
matrix_transpose: Incomplete
tensordot: Incomplete
sign: Incomplete
finfo: Incomplete
iinfo: Incomplete

def asarray(
    obj: Array | complex | NestedSequence[complex] | SupportsBufferProtocol,
    /,
    *,
    dtype: DType | None = None,
    device: Device | None = None,
    copy: _Copy | None = None,
    **kwargs: Any,
) -> Array: ...
def astype(
    x: Array,
    dtype: DType,
    /,
    *,
    copy: py_bool = True,
    device: Device | None = None,
) -> Array: ...
def count_nonzero(
    x: Array,
    axis: int | tuple[int, ...] | None = None,
    keepdims: py_bool = False,
) -> Array: ...
def take_along_axis(x: Array, indices: Array, /, *, axis: int = -1): ...

vecdot: Incomplete
isdtype: Incomplete
unstack: Incomplete
