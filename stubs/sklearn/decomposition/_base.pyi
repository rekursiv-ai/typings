from abc import ABCMeta, abstractmethod

from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils._array_api import (
    device as device,
    get_namespace as get_namespace,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class _BasePCA(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    BaseEstimator,
    metaclass=ABCMeta,
):
    def get_covariance(self): ...
    def get_precision(self): ...
    @abstractmethod
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
