from types import ModuleType
from typing import Any

import numpy as np

from ._utils._typing import Array

__all__ = ["as_numpy_array", "xp_assert_close", "xp_assert_equal", "xp_assert_less"]

def as_numpy_array(array: Array, *, xp: ModuleType) -> np.typing.NDArray[Any]: ...
def xp_assert_equal(
    actual: Array,
    desired: Array,
    *,
    err_msg: str = "",
    check_dtype: bool = True,
    check_shape: bool = True,
    check_scalar: bool = False,
) -> None: ...
def xp_assert_less(
    x: Array,
    y: Array,
    *,
    err_msg: str = "",
    check_dtype: bool = True,
    check_shape: bool = True,
    check_scalar: bool = False,
) -> None: ...
def xp_assert_close(
    actual: Array,
    desired: Array,
    *,
    rtol: float | None = None,
    atol: float = 0,
    err_msg: str = "",
    check_dtype: bool = True,
    check_shape: bool = True,
    check_scalar: bool = False,
) -> None: ...
