from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MetaEstimatorMixin as MetaEstimatorMixin,
    clone as clone,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
)
from sklearn.utils import (
    Bunch as Bunch,
    check_random_state as check_random_state,
)
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils.metaestimators import _BaseComposition

class BaseEnsemble(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    estimator: Incomplete
    n_estimators: Incomplete
    estimator_params: Incomplete
    @abstractmethod
    def __init__(
        self,
        estimator=None,
        *,
        n_estimators: int = 10,
        estimator_params=...,
    ): ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __iter__(self): ...

class _BaseHeterogeneousEnsemble(
    MetaEstimatorMixin,
    _BaseComposition,
    metaclass=ABCMeta,
):
    @property
    def named_estimators(self): ...
    estimators: Incomplete
    @abstractmethod
    def __init__(self, estimators): ...
    def set_params(self, **params): ...
    def get_params(self, deep: bool = True): ...
    def __sklearn_tags__(self): ...
