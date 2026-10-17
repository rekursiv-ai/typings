from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClusterMixin as ClusterMixin,
)
from sklearn.cluster._dbscan_inner import dbscan_inner as dbscan_inner
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import validate_data as validate_data

def dbscan(
    X,
    eps: float = 0.5,
    *,
    min_samples: int = 5,
    metric: str = "minkowski",
    metric_params=None,
    algorithm: str = "auto",
    leaf_size: int = 30,
    p: int = 2,
    sample_weight=None,
    n_jobs=None,
): ...

class DBSCAN(ClusterMixin, BaseEstimator):
    eps: Incomplete
    min_samples: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    algorithm: Incomplete
    leaf_size: Incomplete
    p: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        eps: float = 0.5,
        *,
        min_samples: int = 5,
        metric: str = "euclidean",
        metric_params=None,
        algorithm: str = "auto",
        leaf_size: int = 30,
        p=None,
        n_jobs=None,
    ) -> None: ...
    core_sample_indices_: Incomplete
    labels_: Incomplete
    components_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def fit_predict(self, X, y=None, sample_weight=None): ...
    def __sklearn_tags__(self): ...
