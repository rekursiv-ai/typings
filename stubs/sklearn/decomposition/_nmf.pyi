from abc import ABC

from _typeshed import Incomplete
from sklearn._config import config_context as config_context
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    gen_batches as gen_batches,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import (
    safe_sparse_dot as safe_sparse_dot,
    squared_norm as squared_norm,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
    validate_data as validate_data,
)

EPSILON: Incomplete

def norm(x): ...
def trace_dot(X, Y): ...
def non_negative_factorization(
    X,
    W=None,
    H=None,
    n_components: str = "auto",
    *,
    init=None,
    update_H: bool = True,
    solver: str = "cd",
    beta_loss: str = "frobenius",
    tol: float = 0.0001,
    max_iter: int = 200,
    alpha_W: float = 0.0,
    alpha_H: str = "same",
    l1_ratio: float = 0.0,
    random_state=None,
    verbose: int = 0,
    shuffle: bool = False,
): ...

class _BaseNMF(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator, ABC):
    n_components: Incomplete
    init: Incomplete
    beta_loss: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    random_state: Incomplete
    alpha_W: Incomplete
    alpha_H: Incomplete
    l1_ratio: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        n_components: str = "auto",
        *,
        init=None,
        beta_loss: str = "frobenius",
        tol: float = 0.0001,
        max_iter: int = 200,
        random_state=None,
        alpha_W: float = 0.0,
        alpha_H: str = "same",
        l1_ratio: float = 0.0,
        verbose: int = 0,
    ) -> None: ...
    def fit(self, X, y=None, **params): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

class NMF(_BaseNMF):
    solver: Incomplete
    shuffle: Incomplete
    def __init__(
        self,
        n_components: str = "auto",
        *,
        init=None,
        solver: str = "cd",
        beta_loss: str = "frobenius",
        tol: float = 0.0001,
        max_iter: int = 200,
        random_state=None,
        alpha_W: float = 0.0,
        alpha_H: str = "same",
        l1_ratio: float = 0.0,
        verbose: int = 0,
        shuffle: bool = False,
    ) -> None: ...
    reconstruction_err_: Incomplete
    n_components_: Incomplete
    components_: Incomplete
    n_iter_: Incomplete
    def fit_transform(self, X, y=None, W=None, H=None): ...
    def transform(self, X): ...

class MiniBatchNMF(_BaseNMF):
    max_no_improvement: Incomplete
    batch_size: Incomplete
    forget_factor: Incomplete
    fresh_restarts: Incomplete
    fresh_restarts_max_iter: Incomplete
    transform_max_iter: Incomplete
    def __init__(
        self,
        n_components: str = "auto",
        *,
        init=None,
        batch_size: int = 1024,
        beta_loss: str = "frobenius",
        tol: float = 0.0001,
        max_no_improvement: int = 10,
        max_iter: int = 200,
        alpha_W: float = 0.0,
        alpha_H: str = "same",
        l1_ratio: float = 0.0,
        forget_factor: float = 0.7,
        fresh_restarts: bool = False,
        fresh_restarts_max_iter: int = 30,
        transform_max_iter=None,
        random_state=None,
        verbose: int = 0,
    ) -> None: ...
    reconstruction_err_: Incomplete
    n_components_: Incomplete
    components_: Incomplete
    n_iter_: Incomplete
    n_steps_: Incomplete
    def fit_transform(self, X, y=None, W=None, H=None): ...
    def transform(self, X): ...
    def partial_fit(self, X, y=None, W=None, H=None): ...
