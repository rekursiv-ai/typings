from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import ClassifierMixin, RegressorMixin
from sklearn.ensemble._base import BaseEnsemble

__all__ = ["BaggingClassifier", "BaggingRegressor"]

class BaseBagging(BaseEnsemble, metaclass=ABCMeta):
    max_samples: Incomplete
    max_features: Incomplete
    bootstrap: Incomplete
    bootstrap_features: Incomplete
    oob_score: Incomplete
    warm_start: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    verbose: Incomplete
    @abstractmethod
    def __init__(
        self,
        estimator=None,
        n_estimators: int = 10,
        *,
        max_samples=None,
        max_features: float = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
    ): ...
    def fit(self, X, y, sample_weight=None, **fit_params): ...
    @property
    def estimators_samples_(self): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...

class BaggingClassifier(ClassifierMixin, BaseBagging):
    def __init__(
        self,
        estimator=None,
        n_estimators: int = 10,
        *,
        max_samples=None,
        max_features: float = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
    ) -> None: ...
    def predict(self, X, **params): ...
    def predict_proba(self, X, **params): ...
    def predict_log_proba(self, X, **params): ...
    def decision_function(self, X, **params): ...

class BaggingRegressor(RegressorMixin, BaseBagging):
    def __init__(
        self,
        estimator=None,
        n_estimators: int = 10,
        *,
        max_samples=None,
        max_features: float = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
    ) -> None: ...
    def predict(self, X, **params): ...
