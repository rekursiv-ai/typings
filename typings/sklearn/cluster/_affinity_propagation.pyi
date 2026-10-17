from _typeshed import Incomplete
from sklearn._config import config_context as config_context
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClusterMixin as ClusterMixin,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.metrics import (
    euclidean_distances as euclidean_distances,
    pairwise_distances_argmin as pairwise_distances_argmin,
)
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def affinity_propagation(
    S,
    *,
    preference=None,
    convergence_iter: int = 15,
    max_iter: int = 200,
    damping: float = 0.5,
    copy: bool = True,
    verbose: bool = False,
    return_n_iter: bool = False,
    random_state=None,
): ...

class AffinityPropagation(ClusterMixin, BaseEstimator):
    damping: Incomplete
    max_iter: Incomplete
    convergence_iter: Incomplete
    copy: Incomplete
    verbose: Incomplete
    preference: Incomplete
    affinity: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        damping: float = 0.5,
        max_iter: int = 200,
        convergence_iter: int = 15,
        copy: bool = True,
        preference=None,
        affinity: str = "euclidean",
        verbose: bool = False,
        random_state=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    affinity_matrix_: Incomplete
    cluster_centers_: Incomplete
    def fit(self, X, y=None): ...
    def predict(self, X): ...
    def fit_predict(self, X, y=None): ...
