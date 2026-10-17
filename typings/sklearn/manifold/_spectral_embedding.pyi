from _typeshed import Incomplete
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.metrics.pairwise import rbf_kernel as rbf_kernel
from sklearn.neighbors import (
    NearestNeighbors as NearestNeighbors,
    kneighbors_graph as kneighbors_graph,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    check_symmetric as check_symmetric,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.fixes import (
    parse_version as parse_version,
    sp_version as sp_version,
)
from sklearn.utils.validation import validate_data as validate_data

def spectral_embedding(
    adjacency,
    *,
    n_components: int = 8,
    eigen_solver=None,
    random_state=None,
    eigen_tol: str = "auto",
    norm_laplacian: bool = True,
    drop_first: bool = True,
): ...

class SpectralEmbedding(BaseEstimator):
    n_components: Incomplete
    affinity: Incomplete
    gamma: Incomplete
    random_state: Incomplete
    eigen_solver: Incomplete
    eigen_tol: Incomplete
    n_neighbors: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        n_components: int = 2,
        *,
        affinity: str = "nearest_neighbors",
        gamma=None,
        random_state=None,
        eigen_solver=None,
        eigen_tol: str = "auto",
        n_neighbors=None,
        n_jobs=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    embedding_: Incomplete
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
