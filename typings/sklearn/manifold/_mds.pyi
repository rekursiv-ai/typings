from _typeshed import Incomplete
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.isotonic import IsotonicRegression as IsotonicRegression
from sklearn.manifold import ClassicalMDS as ClassicalMDS
from sklearn.metrics import (
    euclidean_distances as euclidean_distances,
    pairwise_distances as pairwise_distances,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    check_symmetric as check_symmetric,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import validate_data as validate_data

def smacof(
    dissimilarities,
    *,
    metric: bool = True,
    n_components: int = 2,
    init=None,
    n_init: str = "warn",
    n_jobs=None,
    max_iter: int = 300,
    verbose: int = 0,
    eps: float = 1e-06,
    random_state=None,
    return_n_iter: bool = False,
    normalized_stress: str = "auto",
): ...

class MDS(BaseEstimator):
    n_components: Incomplete
    dissimilarity: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    metric_mds: Incomplete
    n_init: Incomplete
    init: Incomplete
    max_iter: Incomplete
    eps: Incomplete
    verbose: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    normalized_stress: Incomplete
    def __init__(
        self,
        n_components: int = 2,
        *,
        metric_mds: bool = True,
        n_init: str = "warn",
        init: str = "warn",
        max_iter: int = 300,
        verbose: int = 0,
        eps: float = 1e-06,
        n_jobs=None,
        random_state=None,
        dissimilarity: str = "deprecated",
        metric: str = "euclidean",
        metric_params=None,
        normalized_stress: str = "auto",
    ) -> None: ...
    def __sklearn_tags__(self): ...
    def fit(self, X, y=None, init=None): ...
    dissimilarity_matrix_: Incomplete
    def fit_transform(self, X, y=None, init=None): ...
