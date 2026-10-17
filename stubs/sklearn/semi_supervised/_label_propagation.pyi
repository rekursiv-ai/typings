from abc import ABCMeta

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.metrics.pairwise import rbf_kernel as rbf_kernel
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class BaseLabelPropagation(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    max_iter: Incomplete
    tol: Incomplete
    kernel: Incomplete
    gamma: Incomplete
    n_neighbors: Incomplete
    alpha: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        kernel: str = "rbf",
        *,
        gamma: int = 20,
        n_neighbors: int = 7,
        alpha: int = 1,
        max_iter: int = 30,
        tol: float = 0.001,
        n_jobs=None,
    ) -> None: ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    X_: Incomplete
    classes_: Incomplete
    label_distributions_: Incomplete
    transduction_: Incomplete
    def fit(self, X, y): ...
    def __sklearn_tags__(self): ...

class LabelPropagation(BaseLabelPropagation):
    def __init__(
        self,
        kernel: str = "rbf",
        *,
        gamma: int = 20,
        n_neighbors: int = 7,
        max_iter: int = 1000,
        tol: float = 0.001,
        n_jobs=None,
    ) -> None: ...
    def fit(self, X, y): ...

class LabelSpreading(BaseLabelPropagation):
    def __init__(
        self,
        kernel: str = "rbf",
        *,
        gamma: int = 20,
        n_neighbors: int = 7,
        alpha: float = 0.2,
        max_iter: int = 30,
        tol: float = 0.001,
        n_jobs=None,
    ) -> None: ...
