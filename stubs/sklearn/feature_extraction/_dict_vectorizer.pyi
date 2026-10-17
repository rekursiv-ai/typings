from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils import (
    check_array as check_array,
    metadata_routing as metadata_routing,
)
from sklearn.utils.validation import check_is_fitted as check_is_fitted

class DictVectorizer(TransformerMixin, BaseEstimator):
    dtype: Incomplete
    separator: Incomplete
    sparse: Incomplete
    sort: Incomplete
    def __init__(
        self,
        *,
        dtype=...,
        separator: str = "=",
        sparse: bool = True,
        sort: bool = True,
    ) -> None: ...
    feature_names_: Incomplete
    vocabulary_: Incomplete
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
    def inverse_transform(self, X, dict_type=...): ...
    def transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
    def restrict(self, support, indices: bool = False): ...
    def __sklearn_tags__(self): ...
