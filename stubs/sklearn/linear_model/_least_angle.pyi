from _typeshed import Incomplete
from sklearn.base import (
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import (
    LinearModel as LinearModel,
    LinearRegression as LinearRegression,
)
from sklearn.model_selection import check_cv as check_cv
from sklearn.utils import (
    Bunch as Bunch,
    arrayfuncs as arrayfuncs,
    as_float_array as as_float_array,
    check_random_state as check_random_state,
)
from sklearn.utils._metadata_requests import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import validate_data as validate_data

SOLVE_TRIANGULAR_ARGS: Incomplete

def lars_path(
    X,
    y,
    Xy=None,
    *,
    Gram=None,
    max_iter: int = 500,
    alpha_min: int = 0,
    method: str = "lar",
    copy_X: bool = True,
    eps=...,
    copy_Gram: bool = True,
    verbose: int = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
): ...
def lars_path_gram(
    Xy,
    Gram,
    *,
    n_samples,
    max_iter: int = 500,
    alpha_min: int = 0,
    method: str = "lar",
    copy_X: bool = True,
    eps=...,
    copy_Gram: bool = True,
    verbose: int = 0,
    return_path: bool = True,
    return_n_iter: bool = False,
    positive: bool = False,
): ...

class Lars(MultiOutputMixin, RegressorMixin, LinearModel):
    method: str
    positive: bool
    fit_intercept: Incomplete
    verbose: Incomplete
    precompute: Incomplete
    n_nonzero_coefs: Incomplete
    eps: Incomplete
    copy_X: Incomplete
    fit_path: Incomplete
    jitter: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool = False,
        precompute: str = "auto",
        n_nonzero_coefs: int = 500,
        eps=...,
        copy_X: bool = True,
        fit_path: bool = True,
        jitter=None,
        random_state=None,
    ) -> None: ...
    def fit(self, X, y, Xy=None): ...

class LassoLars(Lars):
    method: str
    alpha: Incomplete
    fit_intercept: Incomplete
    max_iter: Incomplete
    verbose: Incomplete
    positive: Incomplete
    precompute: Incomplete
    copy_X: Incomplete
    eps: Incomplete
    fit_path: Incomplete
    jitter: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        verbose: bool = False,
        precompute: str = "auto",
        max_iter: int = 500,
        eps=...,
        copy_X: bool = True,
        fit_path: bool = True,
        positive: bool = False,
        jitter=None,
        random_state=None,
    ) -> None: ...

class LarsCV(Lars):
    method: str
    max_iter: Incomplete
    cv: Incomplete
    max_n_alphas: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool = False,
        max_iter: int = 500,
        precompute: str = "auto",
        cv=None,
        max_n_alphas: int = 1000,
        n_jobs=None,
        eps=...,
        copy_X: bool = True,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    alpha_: Incomplete
    cv_alphas_: Incomplete
    mse_path_: Incomplete
    def fit(self, X, y, **params): ...
    def get_metadata_routing(self): ...

class LassoLarsCV(LarsCV):
    method: str
    fit_intercept: Incomplete
    verbose: Incomplete
    max_iter: Incomplete
    precompute: Incomplete
    cv: Incomplete
    max_n_alphas: Incomplete
    n_jobs: Incomplete
    eps: Incomplete
    copy_X: Incomplete
    positive: Incomplete
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        verbose: bool = False,
        max_iter: int = 500,
        precompute: str = "auto",
        cv=None,
        max_n_alphas: int = 1000,
        n_jobs=None,
        eps=...,
        copy_X: bool = True,
        positive: bool = False,
    ) -> None: ...

class LassoLarsIC(LassoLars):
    criterion: Incomplete
    fit_intercept: Incomplete
    positive: Incomplete
    max_iter: Incomplete
    verbose: Incomplete
    copy_X: Incomplete
    precompute: Incomplete
    eps: Incomplete
    fit_path: bool
    noise_variance: Incomplete
    def __init__(
        self,
        criterion: str = "aic",
        *,
        fit_intercept: bool = True,
        verbose: bool = False,
        precompute: str = "auto",
        max_iter: int = 500,
        eps=...,
        copy_X: bool = True,
        positive: bool = False,
        noise_variance=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    alphas_: Incomplete
    noise_variance_: Incomplete
    criterion_: Incomplete
    alpha_: Incomplete
    coef_: Incomplete
    def fit(self, X, y, copy_X=None): ...
