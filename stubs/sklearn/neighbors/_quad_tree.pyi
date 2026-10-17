from typing import ClassVar

from _typeshed import Incomplete

import numpy.dtypes

CELL_DTYPE: numpy.dtypes.VoidDType
__test__: dict

class _QuadTree:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    capacity: Incomplete
    cell_count: Incomplete
    cumulative_size: Incomplete
    leafs: Incomplete
    max_depth: Incomplete
    n_dimensions: Incomplete
    n_points: Incomplete
    verbose: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def build_tree(self, *args, **kwargs): ...
    def get_cell(self, *args, **kwargs): ...
    def __reduce__(self): ...
