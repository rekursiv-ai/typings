from abc import ABCMeta

from _typeshed import Incomplete
from sklearn import cluster as cluster
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    DensityMixin as DensityMixin,
)
from sklearn.cluster import kmeans_plusplus as kmeans_plusplus
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class BaseMixture(DensityMixin, BaseEstimator, metaclass=ABCMeta):
    n_components: Incomplete
    tol: Incomplete
    reg_covar: Incomplete
    max_iter: Incomplete
    n_init: Incomplete
    init_params: Incomplete
    random_state: Incomplete
    warm_start: Incomplete
    verbose: Incomplete
    verbose_interval: Incomplete
    def __init__(
        self,
        n_components,
        tol,
        reg_covar,
        max_iter,
        n_init,
        init_params,
        random_state,
        warm_start,
        verbose,
        verbose_interval,
    ) -> None: ...
    def fit(self, X, y=None): ...
    converged_: bool
    n_iter_: Incomplete
    lower_bound_: Incomplete
    lower_bounds_: Incomplete
    def fit_predict(self, X, y=None): ...
    def score_samples(self, X): ...
    def score(self, X, y=None): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def sample(self, n_samples: int = 1): ...
