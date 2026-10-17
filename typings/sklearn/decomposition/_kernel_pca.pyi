from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.metrics.pairwise import pairwise_kernels as pairwise_kernels
from sklearn.preprocessing import KernelCenterer as KernelCenterer
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import svd_flip as svd_flip
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class KernelPCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    kernel: Incomplete
    kernel_params: Incomplete
    gamma: Incomplete
    degree: Incomplete
    coef0: Incomplete
    alpha: Incomplete
    fit_inverse_transform: Incomplete
    eigen_solver: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    iterated_power: Incomplete
    remove_zero_eig: Incomplete
    random_state: Incomplete
    n_jobs: Incomplete
    copy_X: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        kernel: str = "linear",
        gamma=None,
        degree: int = 3,
        coef0: int = 1,
        kernel_params=None,
        alpha: float = 1.0,
        fit_inverse_transform: bool = False,
        eigen_solver: str = "auto",
        tol: int = 0,
        max_iter=None,
        iterated_power: str = "auto",
        remove_zero_eig: bool = False,
        random_state=None,
        copy_X: bool = True,
        n_jobs=None,
    ) -> None: ...
    gamma_: Incomplete
    X_fit_: Incomplete
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None, **params): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...
