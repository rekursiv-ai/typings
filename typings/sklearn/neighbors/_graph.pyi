from _typeshed import Incomplete
from sklearn.base import (
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.neighbors._base import (
    VALID_METRICS as VALID_METRICS,
    KNeighborsMixin as KNeighborsMixin,
    NeighborsBase as NeighborsBase,
    RadiusNeighborsMixin as RadiusNeighborsMixin,
)
from sklearn.neighbors._unsupervised import NearestNeighbors as NearestNeighbors
from sklearn.utils._param_validation import (
    Integral as Integral,
    Interval as Interval,
    Real as Real,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import check_is_fitted as check_is_fitted

def kneighbors_graph(
    X,
    n_neighbors,
    *,
    mode: str = "connectivity",
    metric: str = "minkowski",
    p: int = 2,
    metric_params=None,
    include_self: bool = False,
    n_jobs=None,
): ...
def radius_neighbors_graph(
    X,
    radius,
    *,
    mode: str = "connectivity",
    metric: str = "minkowski",
    p: int = 2,
    metric_params=None,
    include_self: bool = False,
    n_jobs=None,
): ...

class KNeighborsTransformer(
    ClassNamePrefixFeaturesOutMixin,
    KNeighborsMixin,
    TransformerMixin,
    NeighborsBase,
):
    mode: Incomplete
    def __init__(
        self,
        *,
        mode: str = "distance",
        n_neighbors: int = 5,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
        n_jobs=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def fit_transform(self, X, y=None): ...

class RadiusNeighborsTransformer(
    ClassNamePrefixFeaturesOutMixin,
    RadiusNeighborsMixin,
    TransformerMixin,
    NeighborsBase,
):
    mode: Incomplete
    def __init__(
        self,
        *,
        mode: str = "distance",
        radius: float = 1.0,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
        n_jobs=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def fit_transform(self, X, y=None): ...
