from abc import ABCMeta, abstractmethod

import abc

from _typeshed import Incomplete
from sklearn._loss._loss import (
    CyHalfBinomialLoss as CyHalfBinomialLoss,
    CyHalfSquaredError as CyHalfSquaredError,
    CyHuberLoss as CyHuberLoss,
)
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    OutlierMixin as OutlierMixin,
    RegressorMixin as RegressorMixin,
    clone as clone,
    is_classifier as is_classifier,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import (
    LinearClassifierMixin as LinearClassifierMixin,
    SparseCoefMixin as SparseCoefMixin,
    make_dataset as make_dataset,
)
from sklearn.linear_model._sgd_fast import (
    EpsilonInsensitive as EpsilonInsensitive,
    Hinge as Hinge,
    ModifiedHuber as ModifiedHuber,
    SquaredEpsilonInsensitive as SquaredEpsilonInsensitive,
    SquaredHinge as SquaredHinge,
)
from sklearn.model_selection import (
    ShuffleSplit as ShuffleSplit,
    StratifiedShuffleSplit as StratifiedShuffleSplit,
)
from sklearn.utils import (
    check_random_state as check_random_state,
    compute_class_weight as compute_class_weight,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

LEARNING_RATE_TYPES: Incomplete
PENALTY_TYPES: Incomplete
DEFAULT_EPSILON: float
MAX_INT: Incomplete

class _ValidationScoreCallback:
    estimator: Incomplete
    X_val: Incomplete
    y_val: Incomplete
    sample_weight_val: Incomplete
    def __init__(
        self,
        estimator,
        X_val,
        y_val,
        sample_weight_val,
        classes=None,
    ) -> None: ...
    def __call__(self, coef, intercept): ...

class BaseSGD(SparseCoefMixin, BaseEstimator, metaclass=ABCMeta):
    loss: Incomplete
    penalty: Incomplete
    learning_rate: Incomplete
    epsilon: Incomplete
    alpha: Incomplete
    l1_ratio: Incomplete
    fit_intercept: Incomplete
    shuffle: Incomplete
    random_state: Incomplete
    verbose: Incomplete
    eta0: Incomplete
    power_t: Incomplete
    early_stopping: Incomplete
    validation_fraction: Incomplete
    n_iter_no_change: Incomplete
    warm_start: Incomplete
    average: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    def __init__(
        self,
        loss,
        *,
        penalty: str = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon: float = 0.1,
        random_state=None,
        learning_rate: str = "optimal",
        eta0: float = 0.01,
        power_t: float = 0.5,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        warm_start: bool = False,
        average: bool = False,
    ) -> None: ...
    @abstractmethod
    def fit(self, X, y): ...

def fit_binary(
    est,
    i,
    X,
    y,
    alpha,
    learning_rate,
    max_iter,
    pos_weight,
    neg_weight,
    sample_weight,
    validation_mask=None,
    random_state=None,
): ...

class BaseSGDClassifier(LinearClassifierMixin, BaseSGD, metaclass=ABCMeta):
    loss_functions: Incomplete
    class_weight: Incomplete
    n_jobs: Incomplete
    @abstractmethod
    def __init__(
        self,
        loss: str = "hinge",
        *,
        penalty: str = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon=...,
        n_jobs=None,
        random_state=None,
        learning_rate: str = "optimal",
        eta0: float = 0.01,
        power_t: float = 0.5,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        class_weight=None,
        warm_start: bool = False,
        average: bool = False,
    ): ...
    def partial_fit(self, X, y, classes=None, sample_weight=None): ...
    def fit(self, X, y, coef_init=None, intercept_init=None, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class SGDClassifier(BaseSGDClassifier):
    def __init__(
        self,
        loss: str = "hinge",
        *,
        penalty: str = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon=...,
        n_jobs=None,
        random_state=None,
        learning_rate: str = "optimal",
        eta0: float = 0.01,
        power_t: float = 0.5,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        class_weight=None,
        warm_start: bool = False,
        average: bool = False,
    ) -> None: ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...

class BaseSGDRegressor(RegressorMixin, BaseSGD, metaclass=abc.ABCMeta):
    loss_functions: Incomplete
    @abstractmethod
    def __init__(
        self,
        loss: str = "squared_error",
        *,
        penalty: str = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon=...,
        random_state=None,
        learning_rate: str = "invscaling",
        eta0: float = 0.01,
        power_t: float = 0.25,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        warm_start: bool = False,
        average: bool = False,
    ): ...
    def partial_fit(self, X, y, sample_weight=None): ...
    def fit(self, X, y, coef_init=None, intercept_init=None, sample_weight=None): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...

class SGDRegressor(BaseSGDRegressor):
    def __init__(
        self,
        loss: str = "squared_error",
        *,
        penalty: str = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon=...,
        random_state=None,
        learning_rate: str = "invscaling",
        eta0: float = 0.01,
        power_t: float = 0.25,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        warm_start: bool = False,
        average: bool = False,
    ) -> None: ...

class SGDOneClassSVM(OutlierMixin, BaseSGD):
    loss_functions: Incomplete
    nu: Incomplete
    def __init__(
        self,
        nu: float = 0.5,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        random_state=None,
        learning_rate: str = "optimal",
        eta0: float = 0.01,
        power_t: float = 0.5,
        warm_start: bool = False,
        average: bool = False,
    ) -> None: ...
    def partial_fit(self, X, y=None, sample_weight=None): ...
    def fit(self, X, y=None, coef_init=None, offset_init=None, sample_weight=None): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...
