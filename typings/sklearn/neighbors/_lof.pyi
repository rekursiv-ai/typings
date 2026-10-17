from _typeshed import Incomplete
from sklearn.base import OutlierMixin
from sklearn.neighbors._base import KNeighborsMixin, NeighborsBase

__all__ = ["LocalOutlierFactor"]

class LocalOutlierFactor(KNeighborsMixin, OutlierMixin, NeighborsBase):
    contamination: Incomplete
    novelty: Incomplete
    def __init__(
        self,
        n_neighbors: int = 20,
        *,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
        contamination: str = "auto",
        novelty: bool = False,
        n_jobs=None,
    ) -> None: ...
    def fit_predict(self, X, y=None): ...
    n_neighbors_: Incomplete
    negative_outlier_factor_: Incomplete
    offset_: float
    def fit(self, X, y=None): ...
    def predict(self, X=None): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
