from _typeshed import Incomplete
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.neighbors._ball_tree import BallTree as BallTree
from sklearn.neighbors._base import VALID_METRICS as VALID_METRICS
from sklearn.neighbors._kd_tree import KDTree as KDTree
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import row_norms as row_norms
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

VALID_KERNELS: Incomplete
TREE_DICT: Incomplete

class KernelDensity(BaseEstimator):
    algorithm: Incomplete
    bandwidth: Incomplete
    kernel: Incomplete
    metric: Incomplete
    atol: Incomplete
    rtol: Incomplete
    breadth_first: Incomplete
    leaf_size: Incomplete
    metric_params: Incomplete
    def __init__(
        self,
        *,
        bandwidth: float = 1.0,
        algorithm: str = "auto",
        kernel: str = "gaussian",
        metric: str = "euclidean",
        atol: int = 0,
        rtol: int = 0,
        breadth_first: bool = True,
        leaf_size: int = 40,
        metric_params=None,
    ) -> None: ...
    bandwidth_: Incomplete
    tree_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def score_samples(self, X): ...
    def score(self, X, y=None): ...
    def sample(self, n_samples: int = 1, random_state=None): ...
