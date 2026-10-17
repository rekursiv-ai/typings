from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
)

__all__ = ["FastICA", "fastica"]

def fastica(
    X,
    n_components=None,
    *,
    algorithm: str = "parallel",
    whiten: str = "unit-variance",
    fun: str = "logcosh",
    fun_args=None,
    max_iter: int = 200,
    tol: float = 0.0001,
    w_init=None,
    whiten_solver: str = "svd",
    random_state=None,
    return_X_mean: bool = False,
    compute_sources: bool = True,
    return_n_iter: bool = False,
): ...

class FastICA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    algorithm: Incomplete
    whiten: Incomplete
    fun: Incomplete
    fun_args: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    w_init: Incomplete
    whiten_solver: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        algorithm: str = "parallel",
        whiten: str = "unit-variance",
        fun: str = "logcosh",
        fun_args=None,
        max_iter: int = 200,
        tol: float = 0.0001,
        w_init=None,
        whiten_solver: str = "svd",
        random_state=None,
    ) -> None: ...
    def fit_transform(self, X, y=None): ...
    def fit(self, X, y=None): ...
    def transform(self, X, copy: bool = True): ...
    def inverse_transform(self, X, copy: bool = True): ...
    def __sklearn_tags__(self): ...
