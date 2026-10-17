from _typeshed import Incomplete
from sklearn._config import config_context as config_context
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClusterMixin as ClusterMixin,
)
from sklearn.metrics.pairwise import (
    pairwise_distances_argmin as pairwise_distances_argmin,
)
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    gen_batches as gen_batches,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    validate_params as validate_params,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def estimate_bandwidth(
    X,
    *,
    quantile: float = 0.3,
    n_samples=None,
    random_state: int = 0,
    n_jobs=None,
): ...
def mean_shift(
    X,
    *,
    bandwidth=None,
    seeds=None,
    bin_seeding: bool = False,
    min_bin_freq: int = 1,
    cluster_all: bool = True,
    max_iter: int = 300,
    n_jobs=None,
): ...
def get_bin_seeds(X, bin_size, min_bin_freq: int = 1): ...

class MeanShift(ClusterMixin, BaseEstimator):
    bandwidth: Incomplete
    seeds: Incomplete
    bin_seeding: Incomplete
    cluster_all: Incomplete
    min_bin_freq: Incomplete
    n_jobs: Incomplete
    max_iter: Incomplete
    def __init__(
        self,
        *,
        bandwidth=None,
        seeds=None,
        bin_seeding: bool = False,
        min_bin_freq: int = 1,
        cluster_all: bool = True,
        n_jobs=None,
        max_iter: int = 300,
    ) -> None: ...
    n_iter_: Incomplete
    def fit(self, X, y=None): ...
    def predict(self, X): ...
