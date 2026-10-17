from _typeshed import Incomplete
from sklearn.base import RegressorMixin as RegressorMixin
from sklearn.metrics import DistanceMetric as DistanceMetric
from sklearn.neighbors._base import (
    KNeighborsMixin as KNeighborsMixin,
    NeighborsBase as NeighborsBase,
    RadiusNeighborsMixin as RadiusNeighborsMixin,
)
from sklearn.utils._param_validation import StrOptions as StrOptions

class KNeighborsRegressor(KNeighborsMixin, RegressorMixin, NeighborsBase):
    weights: Incomplete
    def __init__(
        self,
        n_neighbors: int = 5,
        *,
        weights: str = "uniform",
        algorithm: str = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str = "minkowski",
        metric_params=None,
        n_jobs=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    def fit(self, X, y): ...
    def predict(self, X): ...

class RadiusNeighborsRegressor(RadiusNeighborsMixin, RegressorMixin, NeighborsBase):
    weights: Incomplete
    def __init__(
        self,
        radius: float = 1.0,
        *,
        weights: str = "uniform",
        algorithm: str = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str = "minkowski",
        metric_params=None,
        n_jobs=None,
    ) -> None: ...
    def fit(self, X, y): ...
    def predict(self, X): ...
