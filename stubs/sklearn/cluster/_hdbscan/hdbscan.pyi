from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClusterMixin as ClusterMixin,
)
from sklearn.cluster._hdbscan._linkage import (
    MST_edge_dtype as MST_edge_dtype,
    make_single_linkage as make_single_linkage,
    mst_from_data_matrix as mst_from_data_matrix,
    mst_from_mutual_reachability as mst_from_mutual_reachability,
)
from sklearn.cluster._hdbscan._reachability import (
    mutual_reachability_graph as mutual_reachability_graph,
)
from sklearn.cluster._hdbscan._tree import (
    HIERARCHY_dtype as HIERARCHY_dtype,
    labelling_at_cut as labelling_at_cut,
    tree_to_labels as tree_to_labels,
)
from sklearn.metrics import pairwise_distances as pairwise_distances
from sklearn.metrics._dist_metrics import DistanceMetric as DistanceMetric
from sklearn.neighbors import (
    BallTree as BallTree,
    KDTree as KDTree,
    NearestNeighbors as NearestNeighbors,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import validate_data as validate_data

FAST_METRICS: Incomplete

def remap_single_linkage_tree(tree, internal_to_raw, non_finite): ...

class HDBSCAN(ClusterMixin, BaseEstimator):
    min_cluster_size: Incomplete
    min_samples: Incomplete
    alpha: Incomplete
    max_cluster_size: Incomplete
    cluster_selection_epsilon: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    algorithm: Incomplete
    leaf_size: Incomplete
    n_jobs: Incomplete
    cluster_selection_method: Incomplete
    allow_single_cluster: Incomplete
    store_centers: Incomplete
    copy: Incomplete
    def __init__(
        self,
        min_cluster_size: int = 5,
        min_samples=None,
        cluster_selection_epsilon: float = 0.0,
        max_cluster_size=None,
        metric: str = "euclidean",
        metric_params=None,
        alpha: float = 1.0,
        algorithm: str = "auto",
        leaf_size: int = 40,
        n_jobs=None,
        cluster_selection_method: str = "eom",
        allow_single_cluster: bool = False,
        store_centers=None,
        copy: str = "warn",
    ) -> None: ...
    labels_: Incomplete
    probabilities_: Incomplete
    def fit(self, X, y=None): ...
    def fit_predict(self, X, y=None): ...
    def dbscan_clustering(self, cut_distance, min_cluster_size: int = 5): ...
    def __sklearn_tags__(self): ...
