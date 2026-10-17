from _typeshed import Incomplete
from sklearn._config import config_context as config_context
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    ClusterMixin as ClusterMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.cluster import AgglomerativeClustering as AgglomerativeClustering
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.metrics import pairwise_distances_argmin as pairwise_distances_argmin
from sklearn.metrics.pairwise import euclidean_distances as euclidean_distances
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import row_norms as row_norms
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class _CFNode:
    threshold: Incomplete
    branching_factor: Incomplete
    is_leaf: Incomplete
    n_features: Incomplete
    subclusters_: Incomplete
    init_centroids_: Incomplete
    init_sq_norm_: Incomplete
    squared_norm_: Incomplete
    prev_leaf_: Incomplete
    next_leaf_: Incomplete
    def __init__(
        self,
        *,
        threshold,
        branching_factor,
        is_leaf,
        n_features,
        dtype,
    ) -> None: ...
    centroids_: Incomplete
    def append_subcluster(self, subcluster) -> None: ...
    def update_split_subclusters(
        self,
        subcluster,
        new_subcluster1,
        new_subcluster2,
    ) -> None: ...
    def insert_cf_subcluster(self, subcluster): ...

class _CFSubcluster:
    n_samples_: int
    squared_sum_: float
    centroid_: int
    child_: Incomplete
    def __init__(self, *, linear_sum=None) -> None: ...
    sq_norm_: Incomplete
    def update(self, subcluster) -> None: ...
    def merge_subcluster(self, nominee_cluster, threshold): ...
    @property
    def radius(self): ...

class Birch(
    ClassNamePrefixFeaturesOutMixin,
    ClusterMixin,
    TransformerMixin,
    BaseEstimator,
):
    threshold: Incomplete
    branching_factor: Incomplete
    n_clusters: Incomplete
    compute_labels: Incomplete
    def __init__(
        self,
        *,
        threshold: float = 0.5,
        branching_factor: int = 50,
        n_clusters: int = 3,
        compute_labels: bool = True,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def partial_fit(self, X=None, y=None): ...
    def predict(self, X): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
