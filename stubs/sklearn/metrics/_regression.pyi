from _typeshed import Incomplete
from sklearn.exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
    size as size,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    column_or_1d as column_or_1d,
)

__ALL__: Incomplete

def mean_absolute_error(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
def mean_pinball_loss(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    alpha: float = 0.5,
    multioutput: str = "uniform_average",
): ...
def mean_absolute_percentage_error(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
def mean_squared_error(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
def root_mean_squared_error(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
def mean_squared_log_error(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
def root_mean_squared_log_error(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
def median_absolute_error(
    y_true,
    y_pred,
    *,
    multioutput: str = "uniform_average",
    sample_weight=None,
): ...
def explained_variance_score(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
    force_finite: bool = True,
): ...
def r2_score(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
    force_finite: bool = True,
): ...
def max_error(y_true, y_pred): ...
def mean_tweedie_deviance(y_true, y_pred, *, sample_weight=None, power: int = 0): ...
def mean_poisson_deviance(y_true, y_pred, *, sample_weight=None): ...
def mean_gamma_deviance(y_true, y_pred, *, sample_weight=None): ...
def d2_tweedie_score(y_true, y_pred, *, sample_weight=None, power: int = 0): ...
def d2_pinball_score(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    alpha: float = 0.5,
    multioutput: str = "uniform_average",
): ...
def d2_absolute_error_score(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    multioutput: str = "uniform_average",
): ...
