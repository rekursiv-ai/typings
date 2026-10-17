from abc import ABC, abstractmethod
from dataclasses import dataclass

import abc

from _typeshed import Incomplete
from sklearn.utils.extmath import softmax as softmax

@dataclass
class Interval:
    low: float
    high: float
    low_inclusive: bool
    high_inclusive: bool
    def __post_init__(self) -> None: ...
    def includes(self, x): ...

class BaseLink(ABC, metaclass=abc.ABCMeta):
    is_multiclass: bool
    interval_y_pred: Incomplete
    @abstractmethod
    def link(self, y_pred, out=None): ...
    @abstractmethod
    def inverse(self, raw_prediction, out=None): ...

class IdentityLink(BaseLink):
    def link(self, y_pred, out=None): ...
    inverse = link

class LogLink(BaseLink):
    interval_y_pred: Incomplete
    def link(self, y_pred, out=None): ...
    def inverse(self, raw_prediction, out=None): ...

class LogitLink(BaseLink):
    interval_y_pred: Incomplete
    def link(self, y_pred, out=None): ...
    def inverse(self, raw_prediction, out=None): ...

class HalfLogitLink(BaseLink):
    interval_y_pred: Incomplete
    def link(self, y_pred, out=None): ...
    def inverse(self, raw_prediction, out=None): ...

class MultinomialLogit(BaseLink):
    is_multiclass: bool
    interval_y_pred: Incomplete
    def symmetrize_raw_prediction(self, raw_prediction): ...
    def link(self, y_pred, out=None): ...
    def inverse(self, raw_prediction, out=None): ...
