from _typeshed import Incomplete
from sklearn.base import OutlierMixin
from sklearn.ensemble._bagging import BaseBagging

__all__ = ["IsolationForest"]

class IsolationForest(OutlierMixin, BaseBagging):
    contamination: Incomplete
    def __init__(
        self,
        *,
        n_estimators: int = 100,
        max_samples: str = "auto",
        contamination: str = "auto",
        max_features: float = 1.0,
        bootstrap: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
    ) -> None: ...
    max_samples_: Incomplete
    offset_: float
    def fit(self, X, y=None, sample_weight=None): ...
    def predict(self, X): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
    def __sklearn_tags__(self): ...
