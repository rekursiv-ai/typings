from _typeshed import Incomplete
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.feature_selection._base import SelectorMixin as SelectorMixin
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.sparsefuncs import (
    mean_variance_axis as mean_variance_axis,
    min_max_axis as min_max_axis,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class VarianceThreshold(SelectorMixin, BaseEstimator):
    threshold: Incomplete
    def __init__(self, threshold: float = 0.0) -> None: ...
    variances_: Incomplete
    def fit(self, X, y=None): ...
    def __sklearn_tags__(self): ...
