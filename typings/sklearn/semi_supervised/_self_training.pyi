from _typeshed import Incomplete
from sklearn.base import BaseEstimator, ClassifierMixin, MetaEstimatorMixin

__all__ = ["SelfTrainingClassifier"]

class SelfTrainingClassifier(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Incomplete
    threshold: Incomplete
    criterion: Incomplete
    k_best: Incomplete
    max_iter: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        estimator=None,
        threshold: float = 0.75,
        criterion: str = "threshold",
        k_best: int = 10,
        max_iter: int = 10,
        verbose: bool = False,
    ) -> None: ...
    estimator_: Incomplete
    transduction_: Incomplete
    labeled_iter_: Incomplete
    n_iter_: int
    termination_condition_: str
    classes_: Incomplete
    def fit(self, X, y, **params): ...
    def predict(self, X, **params): ...
    def predict_proba(self, X, **params): ...
    def decision_function(self, X, **params): ...
    def predict_log_proba(self, X, **params): ...
    def score(self, X, y, **params): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...
