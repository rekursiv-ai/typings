from abc import ABCMeta, abstractmethod
from collections.abc import Generator

from _typeshed import Incomplete
from sklearn.base import ClassifierMixin, RegressorMixin
from sklearn.ensemble._base import BaseEnsemble
from sklearn.utils.metadata_routing import _RoutingNotSupportedMixin

__all__ = ["AdaBoostClassifier", "AdaBoostRegressor"]

class BaseWeightBoosting(BaseEnsemble, metaclass=ABCMeta):
    learning_rate: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(
        self,
        estimator=None,
        *,
        n_estimators: int = 50,
        estimator_params=...,
        learning_rate: float = 1.0,
        random_state=None,
    ): ...
    estimators_: Incomplete
    estimator_weights_: Incomplete
    estimator_errors_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def staged_score(self, X, y, sample_weight=None) -> Generator[Incomplete]: ...
    @property
    def feature_importances_(self): ...
    def __sklearn_tags__(self): ...

class AdaBoostClassifier(
    _RoutingNotSupportedMixin,
    ClassifierMixin,
    BaseWeightBoosting,
):
    def __init__(
        self,
        estimator=None,
        *,
        n_estimators: int = 50,
        learning_rate: float = 1.0,
        random_state=None,
    ) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> Generator[Incomplete]: ...
    def decision_function(self, X): ...
    def staged_decision_function(self, X) -> Generator[Incomplete]: ...
    def predict_proba(self, X): ...
    def staged_predict_proba(self, X) -> Generator[Incomplete]: ...
    def predict_log_proba(self, X): ...

class AdaBoostRegressor(_RoutingNotSupportedMixin, RegressorMixin, BaseWeightBoosting):
    loss: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        estimator=None,
        *,
        n_estimators: int = 50,
        learning_rate: float = 1.0,
        loss: str = "linear",
        random_state=None,
    ) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> Generator[Incomplete]: ...
