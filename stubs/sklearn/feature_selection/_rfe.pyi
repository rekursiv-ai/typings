from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MetaEstimatorMixin as MetaEstimatorMixin,
    clone as clone,
    is_classifier as is_classifier,
)
from sklearn.feature_selection._base import SelectorMixin as SelectorMixin
from sklearn.metrics import get_scorer as get_scorer
from sklearn.model_selection import check_cv as check_cv
from sklearn.utils import (
    Bunch as Bunch,
    metadata_routing as metadata_routing,
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
)
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class RFE(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Incomplete
    n_features_to_select: Incomplete
    step: Incomplete
    importance_getter: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        estimator,
        *,
        n_features_to_select=None,
        step: int = 1,
        verbose: int = 0,
        importance_getter: str = "auto",
    ) -> None: ...
    @property
    def classes_(self): ...
    def fit(self, X, y, **fit_params): ...
    def predict(self, X, **predict_params): ...
    def score(self, X, y, **score_params): ...
    def decision_function(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def __sklearn_tags__(self): ...
    def get_metadata_routing(self): ...

class RFECV(RFE):
    estimator: Incomplete
    step: Incomplete
    importance_getter: Incomplete
    cv: Incomplete
    scoring: Incomplete
    verbose: Incomplete
    n_jobs: Incomplete
    min_features_to_select: Incomplete
    def __init__(
        self,
        estimator,
        *,
        step: int = 1,
        min_features_to_select: int = 1,
        cv=None,
        scoring=None,
        verbose: int = 0,
        n_jobs=None,
        importance_getter: str = "auto",
    ) -> None: ...
    support_: Incomplete
    n_features_: Incomplete
    ranking_: Incomplete
    estimator_: Incomplete
    cv_results_: Incomplete
    def fit(self, X, y, **params): ...
    def score(self, X, y, **score_params): ...
    def get_metadata_routing(self): ...
