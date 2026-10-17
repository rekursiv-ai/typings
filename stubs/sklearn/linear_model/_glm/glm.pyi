from _typeshed import Incomplete
from sklearn._loss.loss import (
    HalfGammaLoss as HalfGammaLoss,
    HalfPoissonLoss as HalfPoissonLoss,
    HalfSquaredError as HalfSquaredError,
    HalfTweedieLoss as HalfTweedieLoss,
    HalfTweedieLossIdentity as HalfTweedieLossIdentity,
)
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    RegressorMixin as RegressorMixin,
)
from sklearn.linear_model._glm._newton_solver import (
    NewtonCholeskySolver as NewtonCholeskySolver,
    NewtonSolver as NewtonSolver,
)
from sklearn.linear_model._linear_loss import LinearModelLoss as LinearModelLoss
from sklearn.utils import check_array as check_array
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class _GeneralizedLinearRegressor(RegressorMixin, BaseEstimator):
    alpha: Incomplete
    fit_intercept: Incomplete
    solver: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    warm_start: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: str = "lbfgs",
        max_iter: int = 100,
        tol: float = 0.0001,
        warm_start: bool = False,
        verbose: int = 0,
    ) -> None: ...
    n_iter_: Incomplete
    intercept_: Incomplete
    coef_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X): ...
    def score(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class PoissonRegressor(_GeneralizedLinearRegressor):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: str = "lbfgs",
        max_iter: int = 100,
        tol: float = 0.0001,
        warm_start: bool = False,
        verbose: int = 0,
    ) -> None: ...

class GammaRegressor(_GeneralizedLinearRegressor):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: str = "lbfgs",
        max_iter: int = 100,
        tol: float = 0.0001,
        warm_start: bool = False,
        verbose: int = 0,
    ) -> None: ...

class TweedieRegressor(_GeneralizedLinearRegressor):
    link: Incomplete
    power: Incomplete
    def __init__(
        self,
        *,
        power: float = 0.0,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        link: str = "auto",
        solver: str = "lbfgs",
        max_iter: int = 100,
        tol: float = 0.0001,
        warm_start: bool = False,
        verbose: int = 0,
    ) -> None: ...
