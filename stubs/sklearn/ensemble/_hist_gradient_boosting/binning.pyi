from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from sklearn.ensemble._hist_gradient_boosting._bitset import (
    set_bitset_memoryview as set_bitset_memoryview,
)
from sklearn.ensemble._hist_gradient_boosting.common import (
    ALMOST_INF as ALMOST_INF,
    X_BINNED_DTYPE as X_BINNED_DTYPE,
    X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE,
    X_DTYPE as X_DTYPE,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import check_is_fitted as check_is_fitted

class _BinMapper(TransformerMixin, BaseEstimator):
    n_bins: Incomplete
    subsample: Incomplete
    is_categorical: Incomplete
    known_categories: Incomplete
    random_state: Incomplete
    n_threads: Incomplete
    def __init__(
        self,
        n_bins: int = 256,
        subsample=...,
        is_categorical=None,
        known_categories=None,
        random_state=None,
        n_threads=None,
    ) -> None: ...
    is_categorical_: Incomplete
    missing_values_bin_idx_: Incomplete
    bin_thresholds_: Incomplete
    n_bins_non_missing_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def make_known_categories_bitsets(self): ...
