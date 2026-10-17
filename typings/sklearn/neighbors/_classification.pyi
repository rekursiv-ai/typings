from _typeshed import Incomplete
from sklearn.base import ClassifierMixin as ClassifierMixin
from sklearn.metrics._pairwise_distances_reduction import (
    ArgKminClassMode as ArgKminClassMode,
    RadiusNeighborsClassMode as RadiusNeighborsClassMode,
)
from sklearn.neighbors._base import (
    KNeighborsMixin as KNeighborsMixin,
    NeighborsBase as NeighborsBase,
    RadiusNeighborsMixin as RadiusNeighborsMixin,
)
from sklearn.utils._param_validation import StrOptions as StrOptions
from sklearn.utils.extmath import weighted_mode as weighted_mode
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class KNeighborsClassifier(KNeighborsMixin, ClassifierMixin, NeighborsBase):
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
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def score(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class RadiusNeighborsClassifier(RadiusNeighborsMixin, ClassifierMixin, NeighborsBase):
    weights: Incomplete
    outlier_label: Incomplete
    def __init__(
        self,
        radius: float = 1.0,
        *,
        weights: str = "uniform",
        algorithm: str = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str = "minkowski",
        outlier_label=None,
        metric_params=None,
        n_jobs=None,
    ) -> None: ...
    outlier_label_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def score(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...
