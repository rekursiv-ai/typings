from _typeshed import Incomplete
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.metrics import pairwise_distances as pairwise_distances
from sklearn.utils import check_symmetric as check_symmetric
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import svd_flip as svd_flip
from sklearn.utils.validation import validate_data as validate_data

class ClassicalMDS(BaseEstimator):
    n_components: Incomplete
    metric: Incomplete
    metric_params: Incomplete
    def __init__(
        self,
        n_components: int = 2,
        *,
        metric: str = "euclidean",
        metric_params=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    def fit(self, X, y=None): ...
    dissimilarity_matrix_: Incomplete
    embedding_: Incomplete
    eigenvalues_: Incomplete
    def fit_transform(self, X, y=None): ...
