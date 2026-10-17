from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    RegressorMixin as RegressorMixin,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import LinearModel as LinearModel
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.fixes import (
    parse_version as parse_version,
    sp_version as sp_version,
)
from sklearn.utils.validation import validate_data as validate_data

class QuantileRegressor(LinearModel, RegressorMixin, BaseEstimator):
    quantile: Incomplete
    alpha: Incomplete
    fit_intercept: Incomplete
    solver: Incomplete
    solver_options: Incomplete
    def __init__(
        self,
        *,
        quantile: float = 0.5,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: str = "highs",
        solver_options=None,
    ) -> None: ...
    n_iter_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...
