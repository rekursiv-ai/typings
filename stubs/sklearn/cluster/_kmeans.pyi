from abc import ABC
from typing import Self

import abc

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    ClusterMixin as ClusterMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.cluster._k_means_common import CHUNK_SIZE as CHUNK_SIZE
from sklearn.cluster._k_means_elkan import (
    elkan_iter_chunked_dense as elkan_iter_chunked_dense,
    elkan_iter_chunked_sparse as elkan_iter_chunked_sparse,
    init_bounds_dense as init_bounds_dense,
    init_bounds_sparse as init_bounds_sparse,
)
from sklearn.cluster._k_means_lloyd import (
    lloyd_iter_chunked_dense as lloyd_iter_chunked_dense,
    lloyd_iter_chunked_sparse as lloyd_iter_chunked_sparse,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.metrics.pairwise import euclidean_distances as euclidean_distances
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import row_norms as row_norms
from sklearn.utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from sklearn.utils.sparsefuncs_fast import assign_rows_csr as assign_rows_csr
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def kmeans_plusplus(
    X,
    n_clusters,
    *,
    sample_weight=None,
    x_squared_norms=None,
    random_state=None,
    n_local_trials=None,
): ...
def k_means(
    X,
    n_clusters,
    *,
    sample_weight=None,
    init: str = "k-means++",
    n_init: str = "auto",
    max_iter: int = 300,
    verbose: bool = False,
    tol: float = 0.0001,
    random_state=None,
    copy_x: bool = True,
    algorithm: str = "lloyd",
    return_n_iter: bool = False,
): ...

class _BaseKMeans(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    ClusterMixin,
    BaseEstimator,
    ABC,
    metaclass=abc.ABCMeta,
):
    n_clusters: Incomplete
    init: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    n_init: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_clusters,
        *,
        init,
        n_init,
        max_iter,
        tol,
        verbose,
        random_state,
    ) -> None: ...
    def fit_predict(self, X, y=None, sample_weight=None): ...
    def predict(self, X): ...
    def fit_transform(self, X, y=None, sample_weight=None): ...
    def transform(self, X): ...
    def score(self, X, y=None, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class KMeans(_BaseKMeans):
    copy_x: Incomplete
    algorithm: Incomplete
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        init: str = "k-means++",
        n_init: str = "auto",
        max_iter: int = 300,
        tol: float = 0.0001,
        verbose: int = 0,
        random_state=None,
        copy_x: bool = True,
        algorithm: str = "lloyd",
    ) -> None: ...
    cluster_centers_: Incomplete
    labels_: Incomplete
    inertia_: Incomplete
    n_iter_: Incomplete
    def fit(
        self,
        X: Incomplete,
        y: Incomplete = ...,
        sample_weight: Incomplete = ...,
    ) -> Self: ...

class MiniBatchKMeans(_BaseKMeans):
    max_no_improvement: Incomplete
    batch_size: Incomplete
    compute_labels: Incomplete
    init_size: Incomplete
    reassignment_ratio: Incomplete
    def __init__(
        self,
        n_clusters: int = 8,
        *,
        init: str = "k-means++",
        max_iter: int = 100,
        batch_size: int = 1024,
        verbose: int = 0,
        compute_labels: bool = True,
        random_state=None,
        tol: float = 0.0,
        max_no_improvement: int = 10,
        init_size=None,
        n_init: str = "auto",
        reassignment_ratio: float = 0.01,
    ) -> None: ...
    cluster_centers_: Incomplete
    n_steps_: Incomplete
    n_iter_: Incomplete
    inertia_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def partial_fit(self, X, y=None, sample_weight=None): ...
