from _typeshed import Incomplete
from sklearn.base import BaseEstimator, RegressorMixin, TransformerMixin

__all__ = ["IsotonicRegression", "check_increasing", "isotonic_regression"]

def check_increasing(x, y): ...
def isotonic_regression(
    y,
    *,
    sample_weight=None,
    y_min=None,
    y_max=None,
    increasing: bool = True,
): ...

class IsotonicRegression(RegressorMixin, TransformerMixin, BaseEstimator):
    y_min: Incomplete
    y_max: Incomplete
    increasing: Incomplete
    out_of_bounds: Incomplete
    def __init__(
        self,
        *,
        y_min=None,
        y_max=None,
        increasing: bool = True,
        out_of_bounds: str = "nan",
    ) -> None: ...
    def fit(self, X, y, sample_weight=None): ...
    def transform(self, T): ...
    def predict(self, T): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_tags__(self): ...
