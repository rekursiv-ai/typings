from _typeshed import Incomplete
from sklearn.impute._base import _BaseImputer
from sklearn.metrics import pairwise_distances_chunked as pairwise_distances_chunked
from sklearn.utils._missing import is_scalar_nan as is_scalar_nan
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class KNNImputer(_BaseImputer):
    n_neighbors: Incomplete
    weights: Incomplete
    metric: Incomplete
    copy: Incomplete
    def __init__(
        self,
        *,
        missing_values=...,
        n_neighbors: int = 5,
        weights: str = "uniform",
        metric: str = "nan_euclidean",
        copy: bool = True,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
