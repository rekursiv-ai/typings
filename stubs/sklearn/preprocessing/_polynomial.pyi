from _typeshed import Incomplete
from sklearn.base import BaseEstimator, TransformerMixin

__all__ = ["PolynomialFeatures", "SplineTransformer"]

class PolynomialFeatures(TransformerMixin, BaseEstimator):
    degree: Incomplete
    interaction_only: Incomplete
    include_bias: Incomplete
    order: Incomplete
    def __init__(
        self,
        degree: int = 2,
        *,
        interaction_only: bool = False,
        include_bias: bool = True,
        order: str = "C",
    ) -> None: ...
    @property
    def powers_(self): ...
    def get_feature_names_out(self, input_features=None): ...
    n_output_features_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...

class SplineTransformer(TransformerMixin, BaseEstimator):
    n_knots: Incomplete
    degree: Incomplete
    knots: Incomplete
    extrapolation: Incomplete
    include_bias: Incomplete
    order: Incomplete
    handle_missing: Incomplete
    sparse_output: Incomplete
    def __init__(
        self,
        n_knots: int = 5,
        degree: int = 3,
        *,
        knots: str = "uniform",
        extrapolation: str = "constant",
        include_bias: bool = True,
        order: str = "C",
        handle_missing: str = "error",
        sparse_output: bool = False,
    ) -> None: ...
    def get_feature_names_out(self, input_features=None): ...
    bsplines_: Incomplete
    n_features_out_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
