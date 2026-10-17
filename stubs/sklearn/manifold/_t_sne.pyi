from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.decomposition import PCA as PCA
from sklearn.metrics.pairwise import pairwise_distances as pairwise_distances
from sklearn.neighbors import NearestNeighbors as NearestNeighbors
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    check_non_negative as check_non_negative,
    validate_data as validate_data,
)

MACHINE_EPSILON: Incomplete

def trustworthiness(
    X,
    X_embedded,
    *,
    n_neighbors: int = 5,
    metric: str = "euclidean",
): ...

class TSNE(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    perplexity: Incomplete
    early_exaggeration: Incomplete
    learning_rate: Incomplete
    max_iter: Incomplete
    n_iter_without_progress: Incomplete
    min_grad_norm: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    init: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    method: Incomplete
    angle: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        n_components: int = 2,
        *,
        perplexity: float = 30.0,
        early_exaggeration: float = 12.0,
        learning_rate: str = "auto",
        max_iter: int = 1000,
        n_iter_without_progress: int = 300,
        min_grad_norm: float = 1e-07,
        metric: str = "euclidean",
        metric_params=None,
        init: str = "pca",
        verbose: int = 0,
        random_state=None,
        method: str = "barnes_hut",
        angle: float = 0.5,
        n_jobs=None,
    ) -> None: ...
    embedding_: Incomplete
    def fit_transform(self, X, y=None): ...
    def fit(self, X, y=None): ...
    def __sklearn_tags__(self): ...
