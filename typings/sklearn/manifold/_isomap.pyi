from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.decomposition import KernelPCA as KernelPCA
from sklearn.neighbors import (
    NearestNeighbors as NearestNeighbors,
    kneighbors_graph as kneighbors_graph,
    radius_neighbors_graph as radius_neighbors_graph,
)
from sklearn.preprocessing import KernelCenterer as KernelCenterer
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import check_is_fitted as check_is_fitted

class Isomap(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_neighbors: Incomplete
    radius: Incomplete
    n_components: Incomplete
    eigen_solver: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    path_method: Incomplete
    neighbors_algorithm: Incomplete
    n_jobs: Incomplete
    metric: Incomplete
    p: Incomplete
    metric_params: Incomplete
    def __init__(
        self,
        *,
        n_neighbors: int = 5,
        radius=None,
        n_components: int = 2,
        eigen_solver: str = "auto",
        tol: int = 0,
        max_iter=None,
        path_method: str = "auto",
        neighbors_algorithm: str = "auto",
        n_jobs=None,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
    ) -> None: ...
    def reconstruction_error(self): ...
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
