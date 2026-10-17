from sklearn.preprocessing import LabelBinarizer as LabelBinarizer
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
)

def l1_min_c(
    X,
    y,
    *,
    loss: str = "squared_hinge",
    fit_intercept: bool = True,
    intercept_scaling: float = 1.0,
): ...
