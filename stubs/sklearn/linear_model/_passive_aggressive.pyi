from _typeshed import Incomplete
from sklearn.linear_model._stochastic_gradient import (
    DEFAULT_EPSILON as DEFAULT_EPSILON,
    BaseSGDClassifier as BaseSGDClassifier,
    BaseSGDRegressor as BaseSGDRegressor,
)
from sklearn.utils import deprecated as deprecated
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)

class PassiveAggressiveClassifier(BaseSGDClassifier):
    C: Incomplete
    loss: Incomplete
    def __init__(
        self,
        *,
        C: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        shuffle: bool = True,
        verbose: int = 0,
        loss: str = "hinge",
        n_jobs=None,
        random_state=None,
        warm_start: bool = False,
        class_weight=None,
        average: bool = False,
    ) -> None: ...
    def partial_fit(self, X, y, classes=None): ...
    def fit(self, X, y, coef_init=None, intercept_init=None): ...

class PassiveAggressiveRegressor(BaseSGDRegressor):
    C: Incomplete
    def __init__(
        self,
        *,
        C: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        shuffle: bool = True,
        verbose: int = 0,
        loss: str = "epsilon_insensitive",
        epsilon=...,
        random_state=None,
        warm_start: bool = False,
        average: bool = False,
    ) -> None: ...
    def partial_fit(self, X, y): ...
    def fit(self, X, y, coef_init=None, intercept_init=None): ...
