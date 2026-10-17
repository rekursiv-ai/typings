from _typeshed import Incomplete
from sklearn.decomposition._base import _BasePCA
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._array_api import (
    device as device,
    get_namespace as get_namespace,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import (
    fast_logdet as fast_logdet,
    svd_flip as svd_flip,
)
from sklearn.utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class PCA(_BasePCA):
    n_components: Incomplete
    copy: Incomplete
    whiten: Incomplete
    svd_solver: Incomplete
    tol: Incomplete
    iterated_power: Incomplete
    n_oversamples: Incomplete
    power_iteration_normalizer: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        copy: bool = True,
        whiten: bool = False,
        svd_solver: str = "auto",
        tol: float = 0.0,
        iterated_power: str = "auto",
        n_oversamples: int = 10,
        power_iteration_normalizer: str = "auto",
        random_state=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
    def score_samples(self, X): ...
    def score(self, X, y=None): ...
    def __sklearn_tags__(self): ...
