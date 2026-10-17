from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils._dataframe import (
    is_pandas_df as is_pandas_df,
    is_polars_df as is_polars_df,
)
from sklearn.utils._param_validation import StrOptions as StrOptions
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.validation import (
    check_array as check_array,
    validate_data as validate_data,
)

class FunctionTransformer(TransformerMixin, BaseEstimator):
    func: Incomplete
    inverse_func: Incomplete
    validate: Incomplete
    accept_sparse: Incomplete
    check_inverse: Incomplete
    feature_names_out: Incomplete
    kw_args: Incomplete
    inv_kw_args: Incomplete
    def __init__(
        self,
        func=None,
        inverse_func=None,
        *,
        validate: bool = False,
        accept_sparse: bool = False,
        check_inverse: bool = True,
        feature_names_out=None,
        kw_args=None,
        inv_kw_args=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_is_fitted__(self): ...
    def __sklearn_tags__(self): ...
    def set_output(self, *, transform=None): ...
