from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.multiclass import class_distribution as class_distribution
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class DummyClassifier(MultiOutputMixin, ClassifierMixin, BaseEstimator):
    strategy: Incomplete
    random_state: Incomplete
    constant: Incomplete
    def __init__(
        self,
        *,
        strategy: str = "prior",
        random_state=None,
        constant=None,
    ) -> None: ...
    sparse_output_: Incomplete
    n_outputs_: Incomplete
    n_classes_: Incomplete
    classes_: Incomplete
    class_prior_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def __sklearn_tags__(self): ...
    def score(self, X, y, sample_weight=None): ...

class DummyRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    strategy: Incomplete
    constant: Incomplete
    quantile: Incomplete
    def __init__(
        self,
        *,
        strategy: str = "mean",
        constant=None,
        quantile=None,
    ) -> None: ...
    n_outputs_: Incomplete
    constant_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X, return_std: bool = False): ...
    def __sklearn_tags__(self): ...
    def score(self, X, y, sample_weight=None): ...
