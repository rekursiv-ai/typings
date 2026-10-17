from _typeshed import Incomplete
from sklearn.exceptions import (
    DataConversionWarning as DataConversionWarning,
    NotFittedError as NotFittedError,
    PositiveSpectrumWarning as PositiveSpectrumWarning,
)
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
)
from sklearn.utils._dataframe import (
    is_pandas_df as is_pandas_df,
    is_pandas_df_or_series as is_pandas_df_or_series,
)
from sklearn.utils._isfinite import (
    FiniteStatus as FiniteStatus,
    cy_isfinite as cy_isfinite,
)
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils.fixes import ComplexWarning as ComplexWarning

FLOAT_DTYPES: Incomplete

def assert_all_finite(
    X,
    *,
    allow_nan: bool = False,
    estimator_name=None,
    input_name: str = "",
) -> None: ...
def as_float_array(X, *, copy: bool = True, ensure_all_finite: bool = True): ...
def check_memory(memory): ...
def check_consistent_length(*arrays) -> None: ...
def indexable(*iterables): ...
def check_array(
    array,
    accept_sparse: bool = False,
    *,
    accept_large_sparse: bool = True,
    dtype: str = "numeric",
    order=None,
    copy: bool = False,
    force_writeable: bool = False,
    ensure_all_finite: bool = True,
    ensure_non_negative: bool = False,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    ensure_min_samples: int = 1,
    ensure_min_features: int = 1,
    estimator=None,
    input_name: str = "",
): ...
def check_X_y(
    X,
    y,
    accept_sparse: bool = False,
    *,
    accept_large_sparse: bool = True,
    dtype: str = "numeric",
    order=None,
    copy: bool = False,
    force_writeable: bool = False,
    ensure_all_finite: bool = True,
    ensure_2d: bool = True,
    allow_nd: bool = False,
    multi_output: bool = False,
    ensure_min_samples: int = 1,
    ensure_min_features: int = 1,
    y_numeric: bool = False,
    estimator=None,
): ...
def column_or_1d(
    y,
    *,
    dtype=None,
    input_name: str = "y",
    warn: bool = False,
    device=None,
): ...
def check_random_state(seed): ...
def has_fit_parameter(estimator, parameter): ...
def check_symmetric(
    array,
    *,
    tol: float = 1e-10,
    raise_warning: bool = True,
    raise_exception: bool = False,
): ...
def check_is_fitted(
    estimator,
    attributes=None,
    *,
    msg=None,
    all_or_any=...,
) -> None: ...
def check_non_negative(X, whom) -> None: ...
def check_scalar(
    x,
    name,
    target_type,
    *,
    min_val=None,
    max_val=None,
    include_boundaries: str = "both",
): ...
def validate_data(
    _estimator,
    /,
    X: str = "no_validation",
    y: str = "no_validation",
    reset: bool = True,
    validate_separately: bool = False,
    skip_check_array: bool = False,
    **check_params,
): ...
