from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MetaEstimatorMixin as MetaEstimatorMixin,
    clone as clone,
    is_classifier as is_classifier,
)
from sklearn.feature_selection._base import SelectorMixin as SelectorMixin
from sklearn.metrics import (
    check_scoring as check_scoring,
    get_scorer_names as get_scorer_names,
)
from sklearn.model_selection import (
    check_cv as check_cv,
    cross_val_score as cross_val_score,
)
from sklearn.utils._metadata_requests import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
)
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class SequentialFeatureSelector(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Incomplete
    n_features_to_select: Incomplete
    tol: Incomplete
    direction: Incomplete
    scoring: Incomplete
    cv: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        estimator,
        *,
        n_features_to_select: str = "auto",
        tol=None,
        direction: str = "forward",
        scoring=None,
        cv: int = 5,
        n_jobs=None,
    ) -> None: ...
    n_features_to_select_: Incomplete
    support_: Incomplete
    def fit(self, X, y=None, **params): ...
    def __sklearn_tags__(self): ...
    def get_metadata_routing(self): ...
