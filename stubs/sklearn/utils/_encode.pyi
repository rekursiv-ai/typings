from collections import Counter
from typing import NamedTuple

from _typeshed import Incomplete
from sklearn.utils._array_api import (
    device as device,
    get_namespace as get_namespace,
    xpx as xpx,
)
from sklearn.utils._missing import is_scalar_nan as is_scalar_nan

class MissingValues(NamedTuple):
    nan: bool
    none: bool
    def to_list(self): ...

class _nandict(dict):
    nan_value: Incomplete
    def __init__(self, mapping) -> None: ...
    def __missing__(self, key): ...

class _NaNCounter(Counter):
    def __init__(self, items) -> None: ...
    def __missing__(self, key): ...
