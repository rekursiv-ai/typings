from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import BaseEstimator, BiclusterMixin

__all__ = ["SpectralBiclustering", "SpectralCoclustering"]

class BaseSpectral(BiclusterMixin, BaseEstimator, metaclass=ABCMeta):
    n_clusters: Incomplete
    svd_method: Incomplete
    n_svd_vecs: Incomplete
    mini_batch: Incomplete
    init: Incomplete
    n_init: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(
        self,
        n_clusters: int = 3,
        svd_method: str = "randomized",
        n_svd_vecs=None,
        mini_batch: bool = False,
        init: str = "k-means++",
        n_init: int = 10,
        random_state=None,
    ): ...
    def fit(self, X, y=None): ...
    def __sklearn_tags__(self): ...

class SpectralCoclustering(BaseSpectral):
    def __init__(
        self,
        n_clusters: int = 3,
        *,
        svd_method: str = "randomized",
        n_svd_vecs=None,
        mini_batch: bool = False,
        init: str = "k-means++",
        n_init: int = 10,
        random_state=None,
    ) -> None: ...

class SpectralBiclustering(BaseSpectral):
    method: Incomplete
    n_components: Incomplete
    n_best: Incomplete
    def __init__(
        self,
        n_clusters: int = 3,
        *,
        method: str = "bistochastic",
        n_components: int = 6,
        n_best: int = 3,
        svd_method: str = "randomized",
        n_svd_vecs=None,
        mini_batch: bool = False,
        init: str = "k-means++",
        n_init: int = 10,
        random_state=None,
    ) -> None: ...
