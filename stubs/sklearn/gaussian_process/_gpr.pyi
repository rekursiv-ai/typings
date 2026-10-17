from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
    clone as clone,
)
from sklearn.gaussian_process.kernels import (
    RBF as RBF,
    Kernel as Kernel,
)
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import validate_data as validate_data

GPR_CHOLESKY_LOWER: bool

class GaussianProcessRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    kernel: Incomplete
    alpha: Incomplete
    optimizer: Incomplete
    n_restarts_optimizer: Incomplete
    normalize_y: Incomplete
    copy_X_train: Incomplete
    n_targets: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        kernel=None,
        *,
        alpha: float = 1e-10,
        optimizer: str = "fmin_l_bfgs_b",
        n_restarts_optimizer: int = 0,
        normalize_y: bool = False,
        copy_X_train: bool = True,
        n_targets=None,
        random_state=None,
    ) -> None: ...
    kernel_: Incomplete
    X_train_: Incomplete
    y_train_: Incomplete
    log_marginal_likelihood_value_: Incomplete
    L_: Incomplete
    alpha_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X, return_std: bool = False, return_cov: bool = False): ...
    def sample_y(self, X, n_samples: int = 1, random_state: int = 0): ...
    def log_marginal_likelihood(
        self,
        theta=None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ): ...
    def __sklearn_tags__(self): ...
