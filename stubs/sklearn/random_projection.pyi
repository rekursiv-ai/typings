from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
)

__all__ = [
    "GaussianRandomProjection",
    "SparseRandomProjection",
    "johnson_lindenstrauss_min_dim",
]

def johnson_lindenstrauss_min_dim(n_samples, *, eps: float = 0.1): ...

class BaseRandomProjection(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    BaseEstimator,
    metaclass=ABCMeta,
):
    n_components: Incomplete
    eps: Incomplete
    compute_inverse_components: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(
        self,
        n_components: str = "auto",
        *,
        eps: float = 0.1,
        compute_inverse_components: bool = False,
        random_state=None,
    ): ...
    n_components_: Incomplete
    components_: Incomplete
    inverse_components_: Incomplete
    def fit(self, X, y=None): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

class GaussianRandomProjection(BaseRandomProjection):
    def __init__(
        self,
        n_components: str = "auto",
        *,
        eps: float = 0.1,
        compute_inverse_components: bool = False,
        random_state=None,
    ) -> None: ...
    def transform(self, X): ...

class SparseRandomProjection(BaseRandomProjection):
    dense_output: Incomplete
    density: Incomplete
    def __init__(
        self,
        n_components: str = "auto",
        *,
        density: str = "auto",
        eps: float = 0.1,
        dense_output: bool = False,
        compute_inverse_components: bool = False,
        random_state=None,
    ) -> None: ...
    def transform(self, X): ...
