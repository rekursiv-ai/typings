from abc import ABCMeta

import abc

from _typeshed import Incomplete
from sklearn.base import BaseEstimator, ClassifierMixin

__all__ = [
    "BernoulliNB",
    "CategoricalNB",
    "ComplementNB",
    "GaussianNB",
    "MultinomialNB",
]

class _BaseNB(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    def predict_joint_log_proba(self, X): ...
    def predict(self, X): ...
    def predict_log_proba(self, X): ...
    def predict_proba(self, X): ...

class GaussianNB(_BaseNB):
    priors: Incomplete
    var_smoothing: Incomplete
    def __init__(self, *, priors=None, var_smoothing: float = 1e-09) -> None: ...
    def fit(self, X, y, sample_weight=None): ...
    def partial_fit(self, X, y, classes=None, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class _BaseDiscreteNB(_BaseNB, metaclass=abc.ABCMeta):
    alpha: Incomplete
    fit_prior: Incomplete
    class_prior: Incomplete
    force_alpha: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        fit_prior: bool = True,
        class_prior=None,
        force_alpha: bool = True,
    ) -> None: ...
    def partial_fit(self, X, y, classes=None, sample_weight=None): ...
    classes_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class MultinomialNB(_BaseDiscreteNB):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        force_alpha: bool = True,
        fit_prior: bool = True,
        class_prior=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...

class ComplementNB(_BaseDiscreteNB):
    norm: Incomplete
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        force_alpha: bool = True,
        fit_prior: bool = True,
        class_prior=None,
        norm: bool = False,
    ) -> None: ...
    def __sklearn_tags__(self): ...

class BernoulliNB(_BaseDiscreteNB):
    binarize: Incomplete
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        force_alpha: bool = True,
        binarize: float = 0.0,
        fit_prior: bool = True,
        class_prior=None,
    ) -> None: ...

class CategoricalNB(_BaseDiscreteNB):
    min_categories: Incomplete
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        force_alpha: bool = True,
        fit_prior: bool = True,
        class_prior=None,
        min_categories=None,
    ) -> None: ...
    def fit(self, X, y, sample_weight=None): ...
    def partial_fit(self, X, y, classes=None, sample_weight=None): ...
    def __sklearn_tags__(self): ...
