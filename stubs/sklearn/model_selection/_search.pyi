from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import BaseEstimator, MetaEstimatorMixin

__all__ = ["GridSearchCV", "ParameterGrid", "ParameterSampler", "RandomizedSearchCV"]

class ParameterGrid:
    param_grid: Incomplete
    def __init__(self, param_grid) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, ind): ...

class ParameterSampler:
    n_iter: Incomplete
    random_state: Incomplete
    param_distributions: Incomplete
    def __init__(self, param_distributions, n_iter, *, random_state=None) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class BaseSearchCV(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    scoring: Incomplete
    estimator: Incomplete
    n_jobs: Incomplete
    refit: Incomplete
    cv: Incomplete
    verbose: Incomplete
    pre_dispatch: Incomplete
    error_score: Incomplete
    return_train_score: Incomplete
    @abstractmethod
    def __init__(
        self,
        estimator,
        *,
        scoring=None,
        n_jobs=None,
        refit: bool = True,
        cv=None,
        verbose: int = 0,
        pre_dispatch: str = "2*n_jobs",
        error_score=...,
        return_train_score: bool = True,
    ): ...
    def __sklearn_tags__(self): ...
    def score(self, X, y=None, **params): ...
    def score_samples(self, X): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def decision_function(self, X): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    @property
    def n_features_in_(self): ...
    @property
    def classes_(self): ...
    multimetric_: Incomplete
    best_index_: Incomplete
    best_score_: Incomplete
    best_params_: Incomplete
    best_estimator_: Incomplete
    refit_time_: Incomplete
    feature_names_in_: Incomplete
    scorer_: Incomplete
    cv_results_: Incomplete
    n_splits_: Incomplete
    def fit(self, X, y=None, **params): ...
    def get_metadata_routing(self): ...

class GridSearchCV(BaseSearchCV):
    param_grid: Incomplete
    def __init__(
        self,
        estimator,
        param_grid,
        *,
        scoring=None,
        n_jobs=None,
        refit: bool = True,
        cv=None,
        verbose: int = 0,
        pre_dispatch: str = "2*n_jobs",
        error_score=...,
        return_train_score: bool = False,
    ) -> None: ...

class RandomizedSearchCV(BaseSearchCV):
    param_distributions: Incomplete
    n_iter: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        estimator,
        param_distributions,
        *,
        n_iter: int = 10,
        scoring=None,
        n_jobs=None,
        refit: bool = True,
        cv=None,
        verbose: int = 0,
        pre_dispatch: str = "2*n_jobs",
        random_state=None,
        error_score=...,
        return_train_score: bool = False,
    ) -> None: ...
