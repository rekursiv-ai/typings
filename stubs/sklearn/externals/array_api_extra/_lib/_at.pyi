from enum import Enum
from types import ModuleType
from typing import Self

from ._utils._compat import (
    array_namespace as array_namespace,
    is_dask_array as is_dask_array,
    is_jax_array as is_jax_array,
    is_torch_array as is_torch_array,
    is_writeable_array as is_writeable_array,
)
from ._utils._helpers import meta_namespace as meta_namespace
from ._utils._typing import (
    Array as Array,
    SetIndex as SetIndex,
)

class _AtOp(Enum):
    SET = "set"
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    POWER = "power"
    MIN = "min"
    MAX = "max"

class Undef(Enum):
    UNDEF = 0

class at:
    def __init__(self, x: Array, idx: SetIndex | Undef = ..., /) -> None: ...
    def __getitem__(self, idx: SetIndex) -> Self: ...
    def set(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def add(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def subtract(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def multiply(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def divide(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def power(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def min(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
    def max(
        self,
        y: Array | complex,
        /,
        copy: bool | None = None,
        xp: ModuleType | None = None,
    ) -> Array: ...
