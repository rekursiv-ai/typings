from collections.abc import Sequence
from types import ModuleType
from typing import Literal

from ._lib._utils._typing import Array, DType

__all__ = ["isclose", "nan_to_num", "one_hot", "pad"]

def isclose(
    a: Array | complex,
    b: Array | complex,
    *,
    rtol: float = 1e-05,
    atol: float = 1e-08,
    equal_nan: bool = False,
    xp: ModuleType | None = None,
) -> Array: ...
def nan_to_num(
    x: Array | complex,
    /,
    *,
    fill_value: float = 0.0,
    xp: ModuleType | None = None,
) -> Array: ...
def one_hot(
    x: Array,
    /,
    num_classes: int,
    *,
    dtype: DType | None = None,
    axis: int = -1,
    xp: ModuleType | None = None,
) -> Array: ...
def pad(
    x: Array,
    pad_width: int | tuple[int, int] | Sequence[tuple[int, int]],
    mode: Literal["constant"] = "constant",
    *,
    constant_values: complex = 0,
    xp: ModuleType | None = None,
) -> Array: ...
