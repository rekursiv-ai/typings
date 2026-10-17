from _typeshed import Incomplete
from sklearn._config import get_config as get_config
from sklearn.mixture._base import BaseMixture as BaseMixture
from sklearn.utils import check_array as check_array
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
)
from sklearn.utils._param_validation import StrOptions as StrOptions
from sklearn.utils.extmath import row_norms as row_norms

class GaussianMixture(BaseMixture):
    covariance_type: Incomplete
    weights_init: Incomplete
    means_init: Incomplete
    precisions_init: Incomplete
    def __init__(
        self,
        n_components: int = 1,
        *,
        covariance_type: str = "full",
        tol: float = 0.001,
        reg_covar: float = 1e-06,
        max_iter: int = 100,
        n_init: int = 1,
        init_params: str = "kmeans",
        weights_init=None,
        means_init=None,
        precisions_init=None,
        random_state=None,
        warm_start: bool = False,
        verbose: int = 0,
        verbose_interval: int = 10,
    ) -> None: ...
    def bic(self, X): ...
    def aic(self, X): ...
    def __sklearn_tags__(self): ...
