from typing import Any, ClassVar, overload

from _typeshed import Incomplete
from sklearn.metrics._dist_metrics import get_valid_metric_ids as get_valid_metric_ids
from sklearn.utils.validation import check_array as check_array

import _cython_3_2_2
import numpy.dtypes

CLASS_DOC: str
DOC_DICT32: dict
DOC_DICT64: dict
NodeData: numpy.dtypes.VoidDType
NodeHeapData: numpy.dtypes.VoidDType
VALID_METRICS32: list
VALID_METRICS64: list
VALID_METRIC_IDS32: list
VALID_METRIC_IDS64: list
__reduce_cython__: _cython_3_2_2.cython_function_or_method
__setstate_cython__: _cython_3_2_2.cython_function_or_method
__test__: dict
kernel_norm: _cython_3_2_2.cython_function_or_method
newObj: _cython_3_2_2.cython_function_or_method
nodeheap_sort: _cython_3_2_2.cython_function_or_method
simultaneous_sort: _cython_3_2_2.cython_function_or_method

class BallTree(BallTree64): ...

class BallTree32(BinaryTree32):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    @classmethod
    def __init__(cls, X, leaf_size=...) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X, leaf_size=...) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X, leaf_size=...) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X) -> Any: ...

class BallTree64(BinaryTree64):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    @classmethod
    def __init__(cls, X, leaf_size=...) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X, leaf_size=...) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X, leaf_size=...) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, X) -> Any: ...

class BinaryTree32:
    valid_metrics: ClassVar[list] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    data: Incomplete
    idx_array: Incomplete
    node_bounds: Incomplete
    node_data: Incomplete
    sample_weight: Incomplete
    sum_weight: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_arrays(self) -> Any: ...
    def get_n_calls(self) -> Any: ...
    def get_tree_stats(self) -> Any: ...
    def kernel_density(
        self,
        X,
        h,
        kernel=...,
        atol=...,
        rtol=...,
        breadth_first=...,
        return_log=...,
    ) -> Any: ...
    def query(
        self,
        X,
        k=...,
        return_distance=...,
        dualtree=...,
        breadth_first=...,
    ) -> Any: ...
    def query_radius(
        self,
        X,
        r,
        return_distance=...,
        count_only=...,
        sort_results=...,
    ) -> Any: ...
    def reset_n_calls(self) -> Any: ...
    def two_point_correlation(self, X, r, dualtree=...) -> Any: ...
    def __reduce__(self): ...

class BinaryTree64:
    valid_metrics: ClassVar[list] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    data: Incomplete
    idx_array: Incomplete
    node_bounds: Incomplete
    node_data: Incomplete
    sample_weight: Incomplete
    sum_weight: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_arrays(self) -> Any: ...
    def get_n_calls(self) -> Any: ...
    def get_tree_stats(self) -> Any: ...
    def kernel_density(
        self,
        X,
        h,
        kernel=...,
        atol=...,
        rtol=...,
        breadth_first=...,
        return_log=...,
    ) -> Any: ...
    def query(
        self,
        X,
        k=...,
        return_distance=...,
        dualtree=...,
        breadth_first=...,
    ) -> Any: ...
    def query_radius(
        self,
        X,
        r,
        return_distance=...,
        count_only=...,
        sort_results=...,
    ) -> Any: ...
    def reset_n_calls(self) -> Any: ...
    def two_point_correlation(self, X, r, dualtree=...) -> Any: ...
    def __reduce__(self): ...

class NeighborsHeap32:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def get_arrays(self, *args, **kwargs): ...
    def push(self, *args, **kwargs): ...
    def __reduce__(self): ...

class NeighborsHeap64:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def get_arrays(self, *args, **kwargs): ...
    def push(self, *args, **kwargs): ...
    def __reduce__(self): ...

class NodeHeap:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
