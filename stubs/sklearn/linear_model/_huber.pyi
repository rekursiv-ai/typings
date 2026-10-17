from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    RegressorMixin as RegressorMixin,
)
from sklearn.linear_model._base import LinearModel as LinearModel
from sklearn.utils._mask import axis0_safe_slice as axis0_safe_slice
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.validation import validate_data as validate_data

class HuberRegressor(LinearModel, RegressorMixin, BaseEstimator):
    epsilon: Incomplete
    max_iter: Incomplete
    alpha: Incomplete
    warm_start: Incomplete
    fit_intercept: Incomplete
    tol: Incomplete
    def __init__(
        self,
        *,
        epsilon: float = 1.35,
        max_iter: int = 100,
        alpha: float = 0.0001,
        warm_start: bool = False,
        fit_intercept: bool = True,
        tol: float = 1e-05,
    ) -> None: ...
    n_iter_: Incomplete
    scale_: Incomplete
    intercept_: Incomplete
    coef_: Incomplete
    outliers_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...
