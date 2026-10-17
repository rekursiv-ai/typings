from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassifierMixin,
    MetaEstimatorMixin,
    RegressorMixin,
)

__all__ = [
    "ClassifierChain",
    "MultiOutputClassifier",
    "MultiOutputRegressor",
    "RegressorChain",
]

class _MultiOutputEstimator(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    estimator: Incomplete
    n_jobs: Incomplete
    @abstractmethod
    def __init__(self, estimator, *, n_jobs=None): ...
    estimators_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def partial_fit(
        self,
        X,
        y,
        classes=None,
        sample_weight=None,
        **partial_fit_params,
    ): ...
    def fit(self, X, y, sample_weight=None, **fit_params): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...
    def get_metadata_routing(self): ...

class MultiOutputRegressor(RegressorMixin, _MultiOutputEstimator):
    def __init__(self, estimator, *, n_jobs=None) -> None: ...
    def partial_fit(self, X, y, sample_weight=None, **partial_fit_params) -> None: ...

class MultiOutputClassifier(ClassifierMixin, _MultiOutputEstimator):
    def __init__(self, estimator, *, n_jobs=None) -> None: ...
    classes_: Incomplete
    def fit(self, X, Y, sample_weight=None, **fit_params): ...
    def predict_proba(self, X): ...
    def score(self, X, y): ...
    def __sklearn_tags__(self): ...

class _BaseChain(BaseEstimator, metaclass=ABCMeta):
    estimator: Incomplete
    base_estimator: Incomplete
    order: Incomplete
    cv: Incomplete
    random_state: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        estimator=None,
        *,
        order=None,
        cv=None,
        random_state=None,
        verbose: bool = False,
        base_estimator: str = "deprecated",
    ) -> None: ...
    order_: Incomplete
    estimators_: Incomplete
    chain_method_: Incomplete
    @abstractmethod
    def fit(self, X, Y, **fit_params): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...

class ClassifierChain(MetaEstimatorMixin, ClassifierMixin, _BaseChain):
    chain_method: Incomplete
    def __init__(
        self,
        estimator=None,
        *,
        order=None,
        cv=None,
        chain_method: str = "predict",
        random_state=None,
        verbose: bool = False,
        base_estimator: str = "deprecated",
    ) -> None: ...
    classes_: Incomplete
    def fit(self, X, Y, **fit_params): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def decision_function(self, X): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...

class RegressorChain(MetaEstimatorMixin, RegressorMixin, _BaseChain):
    def fit(self, X, Y, **fit_params): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...
