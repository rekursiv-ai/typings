from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClusterMixin as ClusterMixin,
)
from sklearn.exceptions import DataConversionWarning as DataConversionWarning
from sklearn.metrics import pairwise_distances as pairwise_distances
from sklearn.metrics.pairwise import (
    PAIRWISE_BOOLEAN_FUNCTIONS as PAIRWISE_BOOLEAN_FUNCTIONS,
)
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils import gen_batches as gen_batches
from sklearn.utils._chunking import get_chunk_n_rows as get_chunk_n_rows
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    check_memory as check_memory,
    validate_data as validate_data,
)

class OPTICS(ClusterMixin, BaseEstimator):
    max_eps: Incomplete
    min_samples: Incomplete
    min_cluster_size: Incomplete
    algorithm: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    p: Incomplete
    leaf_size: Incomplete
    cluster_method: Incomplete
    eps: Incomplete
    xi: Incomplete
    predecessor_correction: Incomplete
    memory: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        *,
        min_samples: int = 5,
        max_eps=...,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
        cluster_method: str = "xi",
        eps=None,
        xi: float = 0.05,
        predecessor_correction: bool = True,
        min_cluster_size=None,
        algorithm: str = "auto",
        leaf_size: int = 30,
        memory=None,
        n_jobs=None,
    ) -> None: ...
    cluster_hierarchy_: Incomplete
    labels_: Incomplete
    def fit(self, X, y=None): ...

def compute_optics_graph(
    X,
    *,
    min_samples,
    max_eps,
    metric,
    p,
    metric_params,
    algorithm,
    leaf_size,
    n_jobs,
): ...
def cluster_optics_dbscan(*, reachability, core_distances, ordering, eps): ...
def cluster_optics_xi(
    *,
    reachability,
    predecessor,
    ordering,
    min_samples,
    min_cluster_size=None,
    xi: float = 0.05,
    predecessor_correction: bool = True,
): ...
