from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
)

__all__ = ["TruncatedSVD"]

class TruncatedSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    algorithm: Incomplete
    n_components: Incomplete
    n_iter: Incomplete
    n_oversamples: Incomplete
    power_iteration_normalizer: Incomplete
    random_state: Incomplete
    tol: Incomplete
    def __init__(
        self,
        n_components: int = 2,
        *,
        algorithm: str = "randomized",
        n_iter: int = 5,
        n_oversamples: int = 10,
        power_iteration_normalizer: str = "auto",
        random_state=None,
        tol: float = 0.0,
    ) -> None: ...
    def fit(self, X, y=None): ...
    components_: Incomplete
    explained_variance_: Incomplete
    explained_variance_ratio_: Incomplete
    singular_values_: Incomplete
    def fit_transform(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...
