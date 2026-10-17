from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    ClusterMixin as ClusterMixin,
)
from sklearn.cluster._feature_agglomeration import (
    AgglomerationTransform as AgglomerationTransform,
)
from sklearn.metrics import DistanceMetric as DistanceMetric
from sklearn.metrics._dist_metrics import METRIC_MAPPING64 as METRIC_MAPPING64
from sklearn.metrics.pairwise import paired_distances as paired_distances
from sklearn.utils import check_array as check_array
from sklearn.utils._fast_dict import IntFloatDict as IntFloatDict
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    check_memory as check_memory,
    validate_data as validate_data,
)

def ward_tree(
    X,
    *,
    connectivity=None,
    n_clusters=None,
    return_distance: bool = False,
): ...
def linkage_tree(
    X,
    connectivity=None,
    n_clusters=None,
    linkage: str = "complete",
    affinity: str = "euclidean",
    return_distance: bool = False,
): ...

class AgglomerativeClustering(ClusterMixin, BaseEstimator):
    n_clusters: Incomplete
    distance_threshold: Incomplete
    memory: Incomplete
    connectivity: Incomplete
    compute_full_tree: Incomplete
    linkage: Incomplete
    metric: Incomplete
    compute_distances: Incomplete
    def __init__(
        self,
        n_clusters: int = 2,
        *,
        metric: str = "euclidean",
        memory=None,
        connectivity=None,
        compute_full_tree: str = "auto",
        linkage: str = "ward",
        distance_threshold=None,
        compute_distances: bool = False,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def fit_predict(self, X, y=None): ...

class FeatureAgglomeration(
    ClassNamePrefixFeaturesOutMixin,
    AgglomerationTransform,
    AgglomerativeClustering,
):
    pooling_func: Incomplete
    def __init__(
        self,
        n_clusters: int = 2,
        *,
        metric: str = "euclidean",
        memory=None,
        connectivity=None,
        compute_full_tree: str = "auto",
        linkage: str = "ward",
        pooling_func=...,
        distance_threshold=None,
        compute_distances: bool = False,
    ) -> None: ...
    def fit(self, X, y=None): ...
    @property
    def fit_predict(self) -> None: ...
