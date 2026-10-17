from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
    move_to as move_to,
)
from sklearn.utils._dataframe import (
    is_pandas_df as is_pandas_df,
    is_polars_df_or_series as is_polars_df_or_series,
    is_pyarrow_data as is_pyarrow_data,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    validate_params as validate_params,
)
from sklearn.utils.fixes import PYARROW_VERSION_BELOW_17 as PYARROW_VERSION_BELOW_17
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_random_state as check_random_state,
)

def resample(
    *arrays,
    replace: bool = True,
    n_samples=None,
    random_state=None,
    stratify=None,
    sample_weight=None,
): ...
def shuffle(*arrays, random_state=None, n_samples=None): ...
