from sklearn.neighbors._base import (
    KNeighborsMixin as KNeighborsMixin,
    NeighborsBase as NeighborsBase,
    RadiusNeighborsMixin as RadiusNeighborsMixin,
)

class NearestNeighbors(KNeighborsMixin, RadiusNeighborsMixin, NeighborsBase):
    def __init__(
        self,
        *,
        n_neighbors: int = 5,
        radius: float = 1.0,
        algorithm: str = "auto",
        leaf_size: int = 30,
        metric: str = "minkowski",
        p: int = 2,
        metric_params=None,
        n_jobs=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
