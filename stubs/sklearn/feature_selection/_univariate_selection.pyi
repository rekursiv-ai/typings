import abc

from _typeshed import Incomplete
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.feature_selection._base import SelectorMixin as SelectorMixin
from sklearn.preprocessing import LabelBinarizer as LabelBinarizer
from sklearn.utils import (
    as_float_array as as_float_array,
    check_array as check_array,
    check_X_y as check_X_y,
    safe_mask as safe_mask,
    safe_sqr as safe_sqr,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import (
    row_norms as row_norms,
    safe_sparse_dot as safe_sparse_dot,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def f_oneway(*args): ...
def f_classif(X, y): ...
def chi2(X, y): ...
def r_regression(X, y, *, center: bool = True, force_finite: bool = True): ...
def f_regression(X, y, *, center: bool = True, force_finite: bool = True): ...

class _BaseFilter(SelectorMixin, BaseEstimator, metaclass=abc.ABCMeta):
    score_func: Incomplete
    def __init__(self, score_func) -> None: ...
    pvalues_: Incomplete
    scores_: Incomplete
    def fit(self, X, y=None): ...
    def __sklearn_tags__(self): ...

class SelectPercentile(_BaseFilter):
    percentile: Incomplete
    def __init__(self, score_func=..., *, percentile: int = 10) -> None: ...
    def __sklearn_tags__(self): ...

class SelectKBest(_BaseFilter):
    k: Incomplete
    def __init__(self, score_func=..., *, k: int = 10) -> None: ...
    def __sklearn_tags__(self): ...

class SelectFpr(_BaseFilter):
    alpha: Incomplete
    def __init__(self, score_func=..., *, alpha: float = 0.05) -> None: ...

class SelectFdr(_BaseFilter):
    alpha: Incomplete
    def __init__(self, score_func=..., *, alpha: float = 0.05) -> None: ...

class SelectFwe(_BaseFilter):
    alpha: Incomplete
    def __init__(self, score_func=..., *, alpha: float = 0.05) -> None: ...

class GenericUnivariateSelect(_BaseFilter):
    mode: Incomplete
    param: Incomplete
    def __init__(
        self,
        score_func=...,
        *,
        mode: str = "percentile",
        param: float = 1e-05,
    ) -> None: ...
    def __sklearn_tags__(self): ...
