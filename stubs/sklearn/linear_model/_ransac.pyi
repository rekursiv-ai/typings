from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MetaEstimatorMixin as MetaEstimatorMixin,
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
    clone as clone,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import LinearRegression as LinearRegression
from sklearn.utils import (
    check_consistent_length as check_consistent_length,
    check_random_state as check_random_state,
    get_tags as get_tags,
)
from sklearn.utils._bunch import Bunch as Bunch
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    Options as Options,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
)
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.random import (
    sample_without_replacement as sample_without_replacement,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    has_fit_parameter as has_fit_parameter,
    validate_data as validate_data,
)

class RANSACRegressor(
    MetaEstimatorMixin,
    RegressorMixin,
    MultiOutputMixin,
    BaseEstimator,
):
    estimator: Incomplete
    min_samples: Incomplete
    residual_threshold: Incomplete
    is_data_valid: Incomplete
    is_model_valid: Incomplete
    max_trials: Incomplete
    max_skips: Incomplete
    stop_n_inliers: Incomplete
    stop_score: Incomplete
    stop_probability: Incomplete
    random_state: Incomplete
    loss: Incomplete
    def __init__(
        self,
        estimator=None,
        *,
        min_samples=None,
        residual_threshold=None,
        is_data_valid=None,
        is_model_valid=None,
        max_trials: int = 100,
        max_skips=...,
        stop_n_inliers=...,
        stop_score=...,
        stop_probability: float = 0.99,
        loss: str = "absolute_error",
        random_state=None,
    ) -> None: ...
    n_skips_no_inliers_: int
    n_skips_invalid_data_: int
    n_skips_invalid_model_: int
    n_trials_: int
    estimator_: Incomplete
    inlier_mask_: Incomplete
    def fit(self, X, y, sample_weight=None, **fit_params): ...
    def predict(self, X, **params): ...
    def score(self, X, y, **params): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...
