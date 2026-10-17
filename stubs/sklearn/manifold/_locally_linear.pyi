from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
    _UnstableArchMixin,
)
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def barycenter_weights(X, Y, indices, reg: float = 0.001): ...
def barycenter_kneighbors_graph(X, n_neighbors, reg: float = 0.001, n_jobs=None): ...
def null_space(
    M,
    k,
    k_skip: int = 1,
    eigen_solver: str = "arpack",
    tol: float = 1e-06,
    max_iter: int = 100,
    random_state=None,
): ...
def locally_linear_embedding(
    X,
    *,
    n_neighbors,
    n_components,
    reg: float = 0.001,
    eigen_solver: str = "auto",
    tol: float = 1e-06,
    max_iter: int = 100,
    method: str = "standard",
    hessian_tol: float = 0.0001,
    modified_tol: float = 1e-12,
    random_state=None,
    n_jobs=None,
): ...

class LocallyLinearEmbedding(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    _UnstableArchMixin,
    BaseEstimator,
):
    n_neighbors: Incomplete
    n_components: Incomplete
    reg: Incomplete
    eigen_solver: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    method: Incomplete
    hessian_tol: Incomplete
    modified_tol: Incomplete
    random_state: Incomplete
    neighbors_algorithm: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        *,
        n_neighbors: int = 5,
        n_components: int = 2,
        reg: float = 0.001,
        eigen_solver: str = "auto",
        tol: float = 1e-06,
        max_iter: int = 100,
        method: str = "standard",
        hessian_tol: float = 0.0001,
        modified_tol: float = 1e-12,
        neighbors_algorithm: str = "auto",
        random_state=None,
        n_jobs=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
    def transform(self, X): ...
