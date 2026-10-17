from abc import ABCMeta, abstractmethod

from sklearn.base import BaseEstimator
from sklearn.utils._available_if import available_if as available_if

__all__ = ["available_if"]

class _BaseComposition(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self): ...
