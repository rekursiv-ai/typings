from collections.abc import Generator

from _typeshed import Incomplete
from sklearn.cluster._kmeans import _BaseKMeans
from sklearn.utils._param_validation import (
    Integral as Integral,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import row_norms as row_norms
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
    validate_data as validate_data,
)

class _BisectingTree:
    center: Incomplete
    indices: Incomplete
    score: Incomplete
    left: Incomplete
    right: Incomplete
    def __init__(self, center, indices, score) -> None: ...
    def split(self, labels, centers, scores) -> None: ...
    def get_cluster_to_bisect(self): ...
    def iter_leaves(self) -> Generator[Incomplete, Incomplete]: ...

class BisectingKMeans(_BaseKMeans):
    copy_x: Incomplete
    algorithm: Incomplete
    bisecting_strategy: Incomplete
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        init: str = "random",
        n_init: int = 1,
        random_state=None,
        max_iter: int = 300,
        verbose: int = 0,
        tol: float = 0.0001,
        copy_x: bool = True,
        algorithm: str = "lloyd",
        bisecting_strategy: str = "biggest_inertia",
    ) -> None: ...
    labels_: Incomplete
    cluster_centers_: Incomplete
    inertia_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...
