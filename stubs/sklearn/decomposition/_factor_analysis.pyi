from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import (
    fast_logdet as fast_logdet,
    squared_norm as squared_norm,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class FactorAnalysis(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    copy: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    svd_method: Incomplete
    noise_variance_init: Incomplete
    iterated_power: Incomplete
    random_state: Incomplete
    rotation: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        tol: float = 0.01,
        copy: bool = True,
        max_iter: int = 1000,
        noise_variance_init=None,
        svd_method: str = "randomized",
        iterated_power: int = 3,
        rotation=None,
        random_state: int = 0,
    ) -> None: ...
    mean_: Incomplete
    components_: Incomplete
    noise_variance_: Incomplete
    loglike_: Incomplete
    n_iter_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def get_covariance(self): ...
    def get_precision(self): ...
    def score_samples(self, X): ...
    def score(self, X, y=None): ...
