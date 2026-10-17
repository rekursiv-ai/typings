from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassifierMixin,
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
)
from sklearn.linear_model._base import LinearClassifierMixin

__all__ = ["LinearDiscriminantAnalysis", "QuadraticDiscriminantAnalysis"]

class DiscriminantAnalysisPredictionMixin:
    def decision_function(self, X): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...

class LinearDiscriminantAnalysis(
    ClassNamePrefixFeaturesOutMixin,
    LinearClassifierMixin,
    TransformerMixin,
    BaseEstimator,
):
    solver: Incomplete
    shrinkage: Incomplete
    priors: Incomplete
    n_components: Incomplete
    store_covariance: Incomplete
    tol: Incomplete
    covariance_estimator: Incomplete
    def __init__(
        self,
        solver: str = "svd",
        shrinkage=None,
        priors=None,
        n_components=None,
        store_covariance: bool = False,
        tol: float = 0.0001,
        covariance_estimator=None,
    ) -> None: ...
    classes_: Incomplete
    priors_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y): ...
    def transform(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def decision_function(self, X): ...
    def __sklearn_tags__(self): ...

class QuadraticDiscriminantAnalysis(
    DiscriminantAnalysisPredictionMixin,
    ClassifierMixin,
    BaseEstimator,
):
    solver: Incomplete
    shrinkage: Incomplete
    priors: Incomplete
    reg_param: Incomplete
    store_covariance: Incomplete
    tol: Incomplete
    covariance_estimator: Incomplete
    def __init__(
        self,
        *,
        solver: str = "svd",
        shrinkage=None,
        priors=None,
        reg_param: float = 0.0,
        store_covariance: bool = False,
        tol: float = 0.0001,
        covariance_estimator=None,
    ) -> None: ...
    classes_: Incomplete
    priors_: Incomplete
    covariance_: Incomplete
    means_: Incomplete
    scalings_: Incomplete
    rotations_: Incomplete
    def fit(self, X, y): ...
    def decision_function(self, X): ...
