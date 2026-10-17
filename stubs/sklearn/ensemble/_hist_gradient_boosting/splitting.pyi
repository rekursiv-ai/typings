from typing import ClassVar

from _typeshed import Incomplete

import _cython_3_2_2

__test__: dict
compute_node_value: _cython_3_2_2.cython_function_or_method

class SplitInfo:
    def __init__(self, *args, **kwargs) -> None: ...

class Splitter:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    X_binned: Incomplete
    feature_fraction_per_split: Incomplete
    has_missing_values: Incomplete
    hessians_are_constant: Incomplete
    is_categorical: Incomplete
    l2_regularization: Incomplete
    left_indices_buffer: Incomplete
    min_gain_to_split: Incomplete
    min_hessian_to_split: Incomplete
    min_samples_leaf: Incomplete
    missing_values_bin_idx: Incomplete
    monotonic_cst: Incomplete
    n_bins_non_missing: Incomplete
    n_features: Incomplete
    n_threads: Incomplete
    partition: Incomplete
    right_indices_buffer: Incomplete
    rng: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def find_node_split(self, *args, **kwargs): ...
    def split_indices(self, *args, **kwargs): ...
    def __reduce__(self): ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...
