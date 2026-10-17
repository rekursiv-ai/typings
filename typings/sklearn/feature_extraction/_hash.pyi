from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils import metadata_routing as metadata_routing
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)

class FeatureHasher(TransformerMixin, BaseEstimator):
    dtype: Incomplete
    input_type: Incomplete
    n_features: Incomplete
    alternate_sign: Incomplete
    def __init__(
        self,
        n_features=...,
        *,
        input_type: str = "dict",
        dtype=...,
        alternate_sign: bool = True,
    ) -> None: ...
    def fit(self, X=None, y=None): ...
    def transform(self, raw_X): ...
    def __sklearn_tags__(self): ...
