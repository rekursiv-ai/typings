from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from sklearn.preprocessing._encoders import OneHotEncoder as OneHotEncoder
from sklearn.utils import resample as resample
from sklearn.utils._param_validation import (
    Interval as Interval,
    Options as Options,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class KBinsDiscretizer(TransformerMixin, BaseEstimator):
    n_bins: Incomplete
    encode: Incomplete
    strategy: Incomplete
    quantile_method: Incomplete
    dtype: Incomplete
    subsample: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_bins: int = 5,
        *,
        encode: str = "onehot",
        strategy: str = "quantile",
        quantile_method: str = "warn",
        dtype=None,
        subsample: int = 200000,
        random_state=None,
    ) -> None: ...
    bin_edges_: Incomplete
    n_bins_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
