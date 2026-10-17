from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MultiOutputMixin as MultiOutputMixin,
    is_classifier as is_classifier,
)
from sklearn.exceptions import (
    DataConversionWarning as DataConversionWarning,
    EfficiencyWarning as EfficiencyWarning,
)
from sklearn.metrics import (
    DistanceMetric as DistanceMetric,
    pairwise_distances_chunked as pairwise_distances_chunked,
)
from sklearn.metrics._pairwise_distances_reduction import (
    ArgKmin as ArgKmin,
    RadiusNeighbors as RadiusNeighbors,
)
from sklearn.metrics.pairwise import (
    PAIRWISE_DISTANCE_FUNCTIONS as PAIRWISE_DISTANCE_FUNCTIONS,
)
from sklearn.neighbors._ball_tree import BallTree as BallTree
from sklearn.neighbors._kd_tree import KDTree as KDTree
from sklearn.utils import (
    check_array as check_array,
    gen_even_slices as gen_even_slices,
    get_tags as get_tags,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.fixes import (
    parse_version as parse_version,
    sp_base_version as sp_base_version,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

SCIPY_METRICS: Incomplete
VALID_METRICS: Incomplete
VALID_METRICS_SPARSE: Incomplete

def sort_graph_by_row_values(
    graph,
    copy: bool = False,
    warn_when_not_sorted: bool = True,
): ...

class NeighborsBase(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    n_neighbors: Incomplete
    radius: Incomplete
    algorithm: Incomplete
    leaf_size: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    p: Incomplete
    n_jobs: Incomplete
    @abstractmethod
    def __init__(
        self,
        n_neighbors=None,
        radius=None,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
        n_jobs=None,
    ): ...
    def __sklearn_tags__(self): ...

class KNeighborsMixin:
    def kneighbors(self, X=None, n_neighbors=None, return_distance: bool = True): ...
    def kneighbors_graph(
        self,
        X=None,
        n_neighbors=None,
        mode: str = "connectivity",
    ): ...

class RadiusNeighborsMixin:
    def radius_neighbors(
        self,
        X=None,
        radius=None,
        return_distance: bool = True,
        sort_results: bool = False,
    ): ...
    def radius_neighbors_graph(
        self,
        X=None,
        radius=None,
        mode: str = "connectivity",
        sort_results: bool = False,
    ): ...
    def __sklearn_tags__(self): ...
