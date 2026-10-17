from typing import ClassVar

import _cython_3_2_2
import numpy.dtypes

CONDENSED_dtype: numpy.dtypes.VoidDType
HIERARCHY_dtype: numpy.dtypes.VoidDType
__test__: dict
get_cluster_tree_leaves: _cython_3_2_2.cython_function_or_method
labelling_at_cut: _cython_3_2_2.cython_function_or_method
recurse_leaf_dfs: _cython_3_2_2.cython_function_or_method
tree_to_labels: _cython_3_2_2.cython_function_or_method

class TreeUnionFind:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...
