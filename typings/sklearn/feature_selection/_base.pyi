from abc import ABCMeta

from sklearn.base import TransformerMixin as TransformerMixin
from sklearn.utils import (
    check_array as check_array,
    safe_sqr as safe_sqr,
)
from sklearn.utils._dataframe import is_pandas_df as is_pandas_df
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class SelectorMixin(TransformerMixin, metaclass=ABCMeta):
    def get_support(self, indices: bool = False): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
