from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils._missing import (
    is_pandas_na as is_pandas_na,
    is_scalar_nan as is_scalar_nan,
)
from sklearn.utils._param_validation import (
    MissingValues as MissingValues,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class _BaseImputer(TransformerMixin, BaseEstimator):
    missing_values: Incomplete
    add_indicator: Incomplete
    keep_empty_features: Incomplete
    def __init__(
        self,
        *,
        missing_values=...,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...
    def __sklearn_tags__(self): ...

class SimpleImputer(_BaseImputer):
    strategy: Incomplete
    fill_value: Incomplete
    copy: Incomplete
    def __init__(
        self,
        *,
        missing_values=...,
        strategy: str = "mean",
        fill_value=None,
        copy: bool = True,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...
    statistics_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...
    def get_feature_names_out(self, input_features=None): ...

class MissingIndicator(TransformerMixin, BaseEstimator):
    missing_values: Incomplete
    features: Incomplete
    sparse: Incomplete
    error_on_new: Incomplete
    def __init__(
        self,
        *,
        missing_values=...,
        features: str = "missing-only",
        sparse: str = "auto",
        error_on_new: bool = True,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def fit_transform(self, X, y=None): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_tags__(self): ...
