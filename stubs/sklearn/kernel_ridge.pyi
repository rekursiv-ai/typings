from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.metrics.pairwise import (
    PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS,
    pairwise_kernels as pairwise_kernels,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class KernelRidge(MultiOutputMixin, RegressorMixin, BaseEstimator):
    alpha: Incomplete
    kernel: Incomplete
    gamma: Incomplete
    degree: Incomplete
    coef0: Incomplete
    kernel_params: Incomplete
    def __init__(
        self,
        alpha: int = 1,
        *,
        kernel: str = "linear",
        gamma=None,
        degree: int = 3,
        coef0: int = 1,
        kernel_params=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    dual_coef_: Incomplete
    X_fit_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X): ...
