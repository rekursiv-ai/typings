from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    clone as clone,
)
from sklearn.gaussian_process.kernels import (
    RBF as RBF,
    CompoundKernel as CompoundKernel,
    Kernel as Kernel,
)
from sklearn.multiclass import (
    OneVsOneClassifier as OneVsOneClassifier,
    OneVsRestClassifier as OneVsRestClassifier,
)
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

LAMBDAS: Incomplete
COEFS: Incomplete

class _BinaryGaussianProcessClassifierLaplace(BaseEstimator):
    kernel: Incomplete
    optimizer: Incomplete
    n_restarts_optimizer: Incomplete
    max_iter_predict: Incomplete
    warm_start: Incomplete
    copy_X_train: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        kernel=None,
        *,
        optimizer: str = "fmin_l_bfgs_b",
        n_restarts_optimizer: int = 0,
        max_iter_predict: int = 100,
        warm_start: bool = False,
        copy_X_train: bool = True,
        random_state=None,
    ) -> None: ...
    kernel_: Incomplete
    rng: Incomplete
    X_train_: Incomplete
    y_train_: Incomplete
    classes_: Incomplete
    log_marginal_likelihood_value_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def log_marginal_likelihood(
        self,
        theta=None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ): ...
    def latent_mean_and_variance(self, X): ...

class GaussianProcessClassifier(ClassifierMixin, BaseEstimator):
    kernel: Incomplete
    optimizer: Incomplete
    n_restarts_optimizer: Incomplete
    max_iter_predict: Incomplete
    warm_start: Incomplete
    copy_X_train: Incomplete
    random_state: Incomplete
    multi_class: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        kernel=None,
        *,
        optimizer: str = "fmin_l_bfgs_b",
        n_restarts_optimizer: int = 0,
        max_iter_predict: int = 100,
        warm_start: bool = False,
        copy_X_train: bool = True,
        random_state=None,
        multi_class: str = "one_vs_rest",
        n_jobs=None,
    ) -> None: ...
    base_estimator_: Incomplete
    classes_: Incomplete
    n_classes_: Incomplete
    log_marginal_likelihood_value_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    @property
    def kernel_(self): ...
    def log_marginal_likelihood(
        self,
        theta=None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ): ...
    def latent_mean_and_variance(self, X): ...
