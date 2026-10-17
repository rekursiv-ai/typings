from _typeshed import Incomplete
from sklearn.mixture._base import BaseMixture as BaseMixture
from sklearn.utils import check_array as check_array
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)

class BayesianGaussianMixture(BaseMixture):
    covariance_type: Incomplete
    weight_concentration_prior_type: Incomplete
    weight_concentration_prior: Incomplete
    mean_precision_prior: Incomplete
    mean_prior: Incomplete
    degrees_of_freedom_prior: Incomplete
    covariance_prior: Incomplete
    def __init__(
        self,
        *,
        n_components: int = 1,
        covariance_type: str = "full",
        tol: float = 0.001,
        reg_covar: float = 1e-06,
        max_iter: int = 100,
        n_init: int = 1,
        init_params: str = "kmeans",
        weight_concentration_prior_type: str = "dirichlet_process",
        weight_concentration_prior=None,
        mean_precision_prior=None,
        mean_prior=None,
        degrees_of_freedom_prior=None,
        covariance_prior=None,
        random_state=None,
        warm_start: bool = False,
        verbose: int = 0,
        verbose_interval: int = 10,
    ) -> None: ...
