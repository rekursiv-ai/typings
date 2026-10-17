from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClusterMixin as ClusterMixin,
)
from sklearn.cluster._kmeans import k_means as k_means
from sklearn.metrics.pairwise import (
    KERNEL_PARAMS as KERNEL_PARAMS,
    pairwise_kernels as pairwise_kernels,
)
from sklearn.neighbors import (
    NearestNeighbors as NearestNeighbors,
    kneighbors_graph as kneighbors_graph,
)
from sklearn.utils import (
    as_float_array as as_float_array,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import validate_data as validate_data

def cluster_qr(vectors): ...
def discretize(
    vectors,
    *,
    copy: bool = True,
    max_svd_restarts: int = 30,
    n_iter_max: int = 20,
    random_state=None,
): ...
def spectral_clustering(
    affinity,
    *,
    n_clusters: int = 8,
    n_components=None,
    eigen_solver=None,
    random_state=None,
    n_init: int = 10,
    eigen_tol: str = "auto",
    assign_labels: str = "kmeans",
    verbose: bool = False,
): ...

class SpectralClustering(ClusterMixin, BaseEstimator):
    n_clusters: Incomplete
    eigen_solver: Incomplete
    n_components: Incomplete
    random_state: Incomplete
    n_init: Incomplete
    gamma: Incomplete
    affinity: Incomplete
    n_neighbors: Incomplete
    eigen_tol: Incomplete
    assign_labels: Incomplete
    degree: Incomplete
    coef0: Incomplete
    kernel_params: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        eigen_solver=None,
        n_components=None,
        random_state=None,
        n_init: int = 10,
        gamma: float = 1.0,
        affinity: str = "rbf",
        n_neighbors: int = 10,
        eigen_tol: str = "auto",
        assign_labels: str = "kmeans",
        degree: int = 3,
        coef0: int = 1,
        kernel_params=None,
        n_jobs=None,
        verbose: bool = False,
    ) -> None: ...
    affinity_matrix_: Incomplete
    labels_: Incomplete
    def fit(self, X, y=None): ...
    def fit_predict(self, X, y=None): ...
    def __sklearn_tags__(self): ...
