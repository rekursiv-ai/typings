from abc import ABC, abstractmethod
from typing import Self

import abc

from _typeshed import Incomplete
from sklearn.base import (
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.linear_model._base import LinearModel as LinearModel
from sklearn.model_selection import check_cv as check_cv
from sklearn.utils import (
    Bunch as Bunch,
    check_array as check_array,
    check_scalar as check_scalar,
    metadata_routing as metadata_routing,
)
from sklearn.utils._metadata_requests import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    get_routing_for_object as get_routing_for_object,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.metadata_routing import process_routing as process_routing
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from sklearn.utils.validation import (
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    has_fit_parameter as has_fit_parameter,
    validate_data as validate_data,
)

def lasso_path(
    X,
    y,
    *,
    eps: float = 0.001,
    n_alphas: int = 100,
    alphas=None,
    precompute: str = "auto",
    Xy=None,
    copy_X: bool = True,
    coef_init=None,
    verbose: bool = False,
    return_n_iter: bool = False,
    positive: bool = False,
    **params,
): ...
def enet_path(
    X,
    y,
    *,
    l1_ratio: float = 0.5,
    eps: float = 0.001,
    n_alphas: int = 100,
    alphas=None,
    precompute: str = "auto",
    Xy=None,
    copy_X: bool = True,
    coef_init=None,
    verbose: bool = False,
    return_n_iter: bool = False,
    positive: bool = False,
    check_input: bool = True,
    **params,
): ...

class ElasticNet(MultiOutputMixin, RegressorMixin, LinearModel):
    path: Incomplete
    alpha: Incomplete
    l1_ratio: Incomplete
    fit_intercept: Incomplete
    precompute: Incomplete
    max_iter: Incomplete
    copy_X: Incomplete
    tol: Incomplete
    warm_start: Incomplete
    positive: Incomplete
    random_state: Incomplete
    selection: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        l1_ratio: float = 0.5,
        fit_intercept: bool = True,
        precompute: bool = False,
        max_iter: int = 1000,
        copy_X: bool = True,
        tol: float = 0.0001,
        warm_start: bool = False,
        positive: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...
    n_iter_: Incomplete
    coef_: Incomplete
    dual_gap_: Incomplete
    def fit(
        self,
        X: Incomplete,
        y: Incomplete,
        sample_weight: Incomplete = ...,
        check_input: bool = ...,
    ) -> Self: ...
    @property
    def sparse_coef_(self): ...
    def __sklearn_tags__(self): ...

class Lasso(ElasticNet):
    path: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        precompute: bool = False,
        copy_X: bool = True,
        max_iter: int = 1000,
        tol: float = 0.0001,
        warm_start: bool = False,
        positive: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...

class LinearModelCV(MultiOutputMixin, LinearModel, ABC, metaclass=abc.ABCMeta):
    eps: Incomplete
    n_alphas: Incomplete
    alphas: Incomplete
    fit_intercept: Incomplete
    precompute: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    copy_X: Incomplete
    cv: Incomplete
    verbose: Incomplete
    n_jobs: Incomplete
    positive: Incomplete
    random_state: Incomplete
    selection: Incomplete
    @abstractmethod
    def __init__(
        self,
        eps: float = 0.001,
        n_alphas: str = "deprecated",
        alphas: str = "warn",
        fit_intercept: bool = True,
        precompute: str = "auto",
        max_iter: int = 1000,
        tol: float = 0.0001,
        copy_X: bool = True,
        cv=None,
        verbose: bool = False,
        n_jobs=None,
        positive: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ): ...
    @staticmethod
    @abstractmethod
    def path(X, y, **kwargs): ...
    mse_path_: Incomplete
    l1_ratio_: Incomplete
    alpha_: Incomplete
    alphas_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    dual_gap_: Incomplete
    n_iter_: Incomplete
    def fit(self, X, y, sample_weight=None, **params): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...

class LassoCV(RegressorMixin, LinearModelCV):
    path: Incomplete
    def __init__(
        self,
        *,
        eps: float = 0.001,
        n_alphas: str = "deprecated",
        alphas: str = "warn",
        fit_intercept: bool = True,
        precompute: str = "auto",
        max_iter: int = 1000,
        tol: float = 0.0001,
        copy_X: bool = True,
        cv=None,
        verbose: bool = False,
        n_jobs=None,
        positive: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...
    def fit(self, X, y, sample_weight=None, **params): ...

class ElasticNetCV(RegressorMixin, LinearModelCV):
    path: Incomplete
    l1_ratio: Incomplete
    eps: Incomplete
    n_alphas: Incomplete
    alphas: Incomplete
    fit_intercept: Incomplete
    precompute: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    cv: Incomplete
    copy_X: Incomplete
    verbose: Incomplete
    n_jobs: Incomplete
    positive: Incomplete
    random_state: Incomplete
    selection: Incomplete
    def __init__(
        self,
        *,
        l1_ratio: float = 0.5,
        eps: float = 0.001,
        n_alphas: str = "deprecated",
        alphas: str = "warn",
        fit_intercept: bool = True,
        precompute: str = "auto",
        max_iter: int = 1000,
        tol: float = 0.0001,
        cv=None,
        copy_X: bool = True,
        verbose: int = 0,
        n_jobs=None,
        positive: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...
    def fit(self, X, y, sample_weight=None, **params): ...

class MultiTaskElasticNet(Lasso):
    l1_ratio: Incomplete
    alpha: Incomplete
    fit_intercept: Incomplete
    max_iter: Incomplete
    copy_X: Incomplete
    tol: Incomplete
    warm_start: Incomplete
    random_state: Incomplete
    selection: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        l1_ratio: float = 0.5,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: int = 1000,
        tol: float = 0.0001,
        warm_start: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...
    coef_: Incomplete
    def fit(self, X, y): ...
    def __sklearn_tags__(self): ...

class MultiTaskLasso(MultiTaskElasticNet):
    alpha: Incomplete
    fit_intercept: Incomplete
    max_iter: Incomplete
    copy_X: Incomplete
    tol: Incomplete
    warm_start: Incomplete
    l1_ratio: float
    random_state: Incomplete
    selection: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: int = 1000,
        tol: float = 0.0001,
        warm_start: bool = False,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...

class MultiTaskElasticNetCV(RegressorMixin, LinearModelCV):
    path: Incomplete
    l1_ratio: Incomplete
    eps: Incomplete
    n_alphas: Incomplete
    alphas: Incomplete
    fit_intercept: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    cv: Incomplete
    copy_X: Incomplete
    verbose: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    selection: Incomplete
    def __init__(
        self,
        *,
        l1_ratio: float = 0.5,
        eps: float = 0.001,
        n_alphas: str = "deprecated",
        alphas: str = "warn",
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.0001,
        cv=None,
        copy_X: bool = True,
        verbose: int = 0,
        n_jobs=None,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...
    def __sklearn_tags__(self): ...
    def fit(self, X, y, **params): ...

class MultiTaskLassoCV(RegressorMixin, LinearModelCV):
    path: Incomplete
    def __init__(
        self,
        *,
        eps: float = 0.001,
        n_alphas: str = "deprecated",
        alphas: str = "warn",
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.0001,
        copy_X: bool = True,
        cv=None,
        verbose: bool = False,
        n_jobs=None,
        random_state=None,
        selection: str = "cyclic",
    ) -> None: ...
    def __sklearn_tags__(self): ...
    def fit(self, X, y, **params): ...
