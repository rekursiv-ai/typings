from _typeshed import Incomplete
from sklearn.base import BaseEstimator, OneToOneFeatureMixin, TransformerMixin

__all__ = ["OneHotEncoder", "OrdinalEncoder"]

class _BaseEncoder(TransformerMixin, BaseEstimator):
    @property
    def infrequent_categories_(self): ...
    def __sklearn_tags__(self): ...

class OneHotEncoder(_BaseEncoder):
    categories: Incomplete
    sparse_output: Incomplete
    dtype: Incomplete
    handle_unknown: Incomplete
    drop: Incomplete
    min_frequency: Incomplete
    max_categories: Incomplete
    feature_name_combiner: Incomplete
    def __init__(
        self,
        *,
        categories: str = "auto",
        drop=None,
        sparse_output: bool = True,
        dtype=...,
        handle_unknown: str = "error",
        min_frequency=None,
        max_categories=None,
        feature_name_combiner: str = "concat",
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...

class OrdinalEncoder(OneToOneFeatureMixin, _BaseEncoder):
    categories: Incomplete
    dtype: Incomplete
    handle_unknown: Incomplete
    unknown_value: Incomplete
    encoded_missing_value: Incomplete
    min_frequency: Incomplete
    max_categories: Incomplete
    def __init__(
        self,
        *,
        categories: str = "auto",
        dtype=...,
        handle_unknown: str = "error",
        unknown_value=None,
        encoded_missing_value=...,
        min_frequency=None,
        max_categories=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
