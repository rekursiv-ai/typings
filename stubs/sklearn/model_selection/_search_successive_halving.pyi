from collections.abc import Generator

import abc

from _typeshed import Incomplete
from sklearn.model_selection._search import BaseSearchCV

__all__ = ["HalvingGridSearchCV", "HalvingRandomSearchCV"]

class _SubsampleMetaSplitter:
    base_cv: Incomplete
    fraction: Incomplete
    subsample_test: Incomplete
    random_state: Incomplete
    def __init__(self, *, base_cv, fraction, subsample_test, random_state) -> None: ...
    def split(self, X, y, **kwargs) -> Generator[Incomplete]: ...

class BaseSuccessiveHalving(BaseSearchCV, metaclass=abc.ABCMeta):
    random_state: Incomplete
    max_resources: Incomplete
    resource: Incomplete
    factor: Incomplete
    min_resources: Incomplete
    aggressive_elimination: Incomplete
    def __init__(
        self,
        estimator,
        *,
        scoring=None,
        n_jobs=None,
        refit: bool = True,
        cv: int = 5,
        verbose: int = 0,
        random_state=None,
        error_score=...,
        return_train_score: bool = True,
        max_resources: str = "auto",
        min_resources: str = "exhaust",
        resource: str = "n_samples",
        factor: int = 3,
        aggressive_elimination: bool = False,
    ) -> None: ...
    best_score_: Incomplete
    def fit(self, X, y=None, **params): ...

class HalvingGridSearchCV(BaseSuccessiveHalving):
    param_grid: Incomplete
    def __init__(
        self,
        estimator,
        param_grid,
        *,
        factor: int = 3,
        resource: str = "n_samples",
        max_resources: str = "auto",
        min_resources: str = "exhaust",
        aggressive_elimination: bool = False,
        cv: int = 5,
        scoring=None,
        refit: bool = True,
        error_score=...,
        return_train_score: bool = True,
        random_state=None,
        n_jobs=None,
        verbose: int = 0,
    ) -> None: ...

class HalvingRandomSearchCV(BaseSuccessiveHalving):
    param_distributions: Incomplete
    n_candidates: Incomplete
    def __init__(
        self,
        estimator,
        param_distributions,
        *,
        n_candidates: str = "exhaust",
        factor: int = 3,
        resource: str = "n_samples",
        max_resources: str = "auto",
        min_resources: str = "smallest",
        aggressive_elimination: bool = False,
        cv: int = 5,
        scoring=None,
        refit: bool = True,
        error_score=...,
        return_train_score: bool = True,
        random_state=None,
        n_jobs=None,
        verbose: int = 0,
    ) -> None: ...
