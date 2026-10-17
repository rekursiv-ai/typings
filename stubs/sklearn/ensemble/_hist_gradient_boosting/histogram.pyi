from typing import ClassVar

from _typeshed import Incomplete

import numpy.dtypes

HISTOGRAM_DTYPE: numpy.dtypes.VoidDType
__test__: dict

class HistogramBuilder:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    X_binned: Incomplete
    gradients: Incomplete
    hessians: Incomplete
    hessians_are_constant: Incomplete
    n_bins: Incomplete
    n_features: Incomplete
    n_threads: Incomplete
    ordered_gradients: Incomplete
    ordered_hessians: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def compute_histograms_brute(self, *args, **kwargs): ...
    def compute_histograms_subtraction(self, *args, **kwargs): ...
    def __reduce__(self): ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...
