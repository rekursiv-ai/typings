from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
    MultiOutputMixin,
    RegressorMixin,
    TransformerMixin,
)

__all__ = ["PLSSVD", "PLSCanonical", "PLSRegression"]

class _PLS(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    RegressorMixin,
    MultiOutputMixin,
    BaseEstimator,
    metaclass=ABCMeta,
):
    n_components: Incomplete
    deflation_mode: Incomplete
    mode: Incomplete
    scale: Incomplete
    algorithm: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    copy: Incomplete
    @abstractmethod
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        deflation_mode: str = "regression",
        mode: str = "A",
        algorithm: str = "nipals",
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ): ...
    x_weights_: Incomplete
    y_weights_: Incomplete
    x_loadings_: Incomplete
    y_loadings_: Incomplete
    n_iter_: Incomplete
    x_rotations_: Incomplete
    y_rotations_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y): ...
    def transform(self, X, y=None, copy: bool = True): ...
    def inverse_transform(self, X, y=None): ...
    def predict(self, X, copy: bool = True): ...
    def fit_transform(self, X, y=None): ...
    def __sklearn_tags__(self): ...

class PLSRegression(_PLS):
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...
    x_scores_: Incomplete
    y_scores_: Incomplete
    def fit(self, X, y): ...

class PLSCanonical(_PLS):
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        algorithm: str = "nipals",
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...

class CCA(_PLS):
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        max_iter: int = 500,
        tol: float = 1e-06,
        copy: bool = True,
    ) -> None: ...

class PLSSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    scale: Incomplete
    copy: Incomplete
    def __init__(
        self,
        n_components: int = 2,
        *,
        scale: bool = True,
        copy: bool = True,
    ) -> None: ...
    x_weights_: Incomplete
    y_weights_: Incomplete
    def fit(self, X, y): ...
    def transform(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
