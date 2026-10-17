from sklearn.base import TransformerMixin as TransformerMixin
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class AgglomerationTransform(TransformerMixin):
    def transform(self, X): ...
    def inverse_transform(self, X): ...
