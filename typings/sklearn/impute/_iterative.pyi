from typing import NamedTuple

from _typeshed import Incomplete
from sklearn.base import clone as clone
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.impute._base import (
    SimpleImputer as SimpleImputer,
    _BaseImputer,
)
from sklearn.preprocessing import normalize as normalize
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._missing import is_scalar_nan as is_scalar_nan
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class _ImputerTriplet(NamedTuple):
    feat_idx: Incomplete
    neighbor_feat_idx: Incomplete
    estimator: Incomplete

class IterativeImputer(_BaseImputer):
    estimator: Incomplete
    sample_posterior: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    n_nearest_features: Incomplete
    initial_strategy: Incomplete
    fill_value: Incomplete
    imputation_order: Incomplete
    skip_complete: Incomplete
    min_value: Incomplete
    max_value: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        estimator=None,
        *,
        missing_values=...,
        sample_posterior: bool = False,
        max_iter: int = 10,
        tol: float = 0.001,
        n_nearest_features=None,
        initial_strategy: str = "mean",
        fill_value=None,
        imputation_order: str = "ascending",
        skip_complete: bool = False,
        min_value=...,
        max_value=...,
        verbose: int = 0,
        random_state=None,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None: ...
    random_state_: Incomplete
    imputation_sequence_: Incomplete
    initial_imputer_: Incomplete
    n_iter_: int
    n_features_with_missing_: Incomplete
    def fit_transform(self, X, y=None, **params): ...
    def transform(self, X): ...
    def fit(self, X, y=None, **fit_params): ...
    def get_feature_names_out(self, input_features=None): ...
    def get_metadata_routing(self): ...
