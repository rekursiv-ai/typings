from _typeshed import Incomplete
from sklearn.base import BaseEstimator, RegressorMixin

__all__ = ["TransformedTargetRegressor"]

class TransformedTargetRegressor(RegressorMixin, BaseEstimator):
    regressor: Incomplete
    transformer: Incomplete
    func: Incomplete
    inverse_func: Incomplete
    check_inverse: Incomplete
    def __init__(
        self,
        regressor=None,
        *,
        transformer=None,
        func=None,
        inverse_func=None,
        check_inverse: bool = True,
    ) -> None: ...
    regressor_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, **fit_params): ...
    def predict(self, X, **predict_params): ...
    def __sklearn_tags__(self): ...
    @property
    def n_features_in_(self): ...
    def get_metadata_routing(self): ...
