from collections.abc import (
    Callable as Callable,
    Sequence,
)
from types import ModuleType
from typing import ParamSpec, TypeAlias, overload

from numpy.typing import ArrayLike as ArrayLike

from ._funcs import broadcast_shapes as broadcast_shapes
from ._utils._compat import (
    array_namespace as array_namespace,
    is_dask_namespace as is_dask_namespace,
    is_jax_namespace as is_jax_namespace,
)
from ._utils._helpers import is_python_scalar as is_python_scalar
from ._utils._typing import (
    Array as Array,
    DType as DType,
)

NumPyObject: TypeAlias
P = ParamSpec("P")

@overload
def lazy_apply(
    func: Callable[P, Array | ArrayLike],
    *args: Array | complex | None,
    shape: tuple[int | None, ...] | None = None,
    dtype: DType | None = None,
    as_numpy: bool = False,
    xp: ModuleType | None = None,
    **kwargs: P.kwargs,
) -> Array: ...
@overload
def lazy_apply(
    func: Callable[P, Sequence[Array | ArrayLike]],
    *args: Array | complex | None,
    shape: Sequence[tuple[int | None, ...]],
    dtype: Sequence[DType] | None = None,
    as_numpy: bool = False,
    xp: ModuleType | None = None,
    **kwargs: P.kwargs,
) -> tuple[Array, ...]: ...
