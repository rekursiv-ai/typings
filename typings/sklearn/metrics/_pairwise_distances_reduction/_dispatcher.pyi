from abc import abstractmethod

import abc

from sklearn import get_config as get_config
from sklearn.metrics._dist_metrics import (
    BOOL_METRICS as BOOL_METRICS,
    METRIC_MAPPING64 as METRIC_MAPPING64,
    DistanceMetric as DistanceMetric,
)
from sklearn.metrics._pairwise_distances_reduction._argkmin import (
    ArgKmin32 as ArgKmin32,
    ArgKmin64 as ArgKmin64,
)
from sklearn.metrics._pairwise_distances_reduction._argkmin_classmode import (
    ArgKminClassMode32 as ArgKminClassMode32,
    ArgKminClassMode64 as ArgKminClassMode64,
)
from sklearn.metrics._pairwise_distances_reduction._radius_neighbors import (
    RadiusNeighbors32 as RadiusNeighbors32,
    RadiusNeighbors64 as RadiusNeighbors64,
)
from sklearn.metrics._pairwise_distances_reduction._radius_neighbors_classmode import (
    RadiusNeighborsClassMode32 as RadiusNeighborsClassMode32,
    RadiusNeighborsClassMode64 as RadiusNeighborsClassMode64,
)

def sqeuclidean_row_norms(X, num_threads): ...

class BaseDistancesReductionDispatcher(metaclass=abc.ABCMeta):
    @classmethod
    def valid_metrics(cls) -> list[str]: ...
    @classmethod
    def is_usable_for(cls, X, Y, metric) -> bool: ...
    @classmethod
    @abstractmethod
    def compute(cls, X, Y, **kwargs): ...

class ArgKmin(BaseDistancesReductionDispatcher):
    @classmethod
    def compute(
        cls,
        X,
        Y,
        k,
        metric: str = "euclidean",
        chunk_size=None,
        metric_kwargs=None,
        strategy=None,
        return_distance: bool = False,
    ): ...

class RadiusNeighbors(BaseDistancesReductionDispatcher):
    @classmethod
    def compute(
        cls,
        X,
        Y,
        radius,
        metric: str = "euclidean",
        chunk_size=None,
        metric_kwargs=None,
        strategy=None,
        return_distance: bool = False,
        sort_results: bool = False,
    ): ...

class ArgKminClassMode(BaseDistancesReductionDispatcher):
    @classmethod
    def valid_metrics(cls) -> list[str]: ...
    @classmethod
    def compute(
        cls,
        X,
        Y,
        k,
        weights,
        Y_labels,
        unique_Y_labels,
        metric: str = "euclidean",
        chunk_size=None,
        metric_kwargs=None,
        strategy=None,
    ): ...

class RadiusNeighborsClassMode(BaseDistancesReductionDispatcher):
    @classmethod
    def valid_metrics(cls) -> list[str]: ...
    @classmethod
    def compute(
        cls,
        X,
        Y,
        radius,
        weights,
        Y_labels,
        unique_Y_labels,
        outlier_label,
        metric: str = "euclidean",
        chunk_size=None,
        metric_kwargs=None,
        strategy=None,
    ): ...
