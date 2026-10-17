from _typeshed import Incomplete
from sklearn.base import RegressorMixin as RegressorMixin
from sklearn.linear_model._base import LinearModel as LinearModel
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import fast_logdet as fast_logdet
from sklearn.utils.validation import validate_data as validate_data

class BayesianRidge(RegressorMixin, LinearModel):
    max_iter: Incomplete
    tol: Incomplete
    alpha_1: Incomplete
    alpha_2: Incomplete
    lambda_1: Incomplete
    lambda_2: Incomplete
    alpha_init: Incomplete
    lambda_init: Incomplete
    compute_score: Incomplete
    fit_intercept: Incomplete
    copy_X: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        max_iter: int = 300,
        tol: float = 0.001,
        alpha_1: float = 1e-06,
        alpha_2: float = 1e-06,
        lambda_1: float = 1e-06,
        lambda_2: float = 1e-06,
        alpha_init=None,
        lambda_init=None,
        compute_score: bool = False,
        fit_intercept: bool = True,
        copy_X: bool = True,
        verbose: bool = False,
    ) -> None: ...
    X_offset_: Incomplete
    X_scale_: Incomplete
    scores_: Incomplete
    n_iter_: Incomplete
    alpha_: Incomplete
    lambda_: Incomplete
    sigma_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X, return_std: bool = False): ...

class ARDRegression(RegressorMixin, LinearModel):
    max_iter: Incomplete
    tol: Incomplete
    fit_intercept: Incomplete
    alpha_1: Incomplete
    alpha_2: Incomplete
    lambda_1: Incomplete
    lambda_2: Incomplete
    compute_score: Incomplete
    threshold_lambda: Incomplete
    copy_X: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        max_iter: int = 300,
        tol: float = 0.001,
        alpha_1: float = 1e-06,
        alpha_2: float = 1e-06,
        lambda_1: float = 1e-06,
        lambda_2: float = 1e-06,
        compute_score: bool = False,
        threshold_lambda: float = 10000.0,
        fit_intercept: bool = True,
        copy_X: bool = True,
        verbose: bool = False,
    ) -> None: ...
    X_offset_: Incomplete
    X_scale_: Incomplete
    scores_: Incomplete
    n_iter_: Incomplete
    coef_: Incomplete
    alpha_: Incomplete
    sigma_: Incomplete
    lambda_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X, return_std: bool = False): ...
