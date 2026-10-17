from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils import (
    check_random_state as check_random_state,
    gen_even_slices as gen_even_slices,
)
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class BernoulliRBM(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    learning_rate: Incomplete
    batch_size: Incomplete
    n_iter: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_components: int = 256,
        *,
        learning_rate: float = 0.1,
        batch_size: int = 10,
        n_iter: int = 10,
        verbose: int = 0,
        random_state=None,
    ) -> None: ...
    def transform(self, X): ...
    random_state_: Incomplete
    def gibbs(self, v): ...
    components_: Incomplete
    intercept_hidden_: Incomplete
    intercept_visible_: Incomplete
    h_samples_: Incomplete
    def partial_fit(self, X, y=None) -> None: ...
    def score_samples(self, X): ...
    def fit(self, X, y=None): ...
    def __sklearn_tags__(self): ...
