from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    MetaEstimatorMixin as MetaEstimatorMixin,
    clone as clone,
)
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.metrics import (
    check_scoring as check_scoring,
    get_scorer_names as get_scorer_names,
)
from sklearn.model_selection._split import (
    StratifiedShuffleSplit as StratifiedShuffleSplit,
    check_cv as check_cv,
)
from sklearn.utils import get_tags as get_tags
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
)
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.multiclass import type_of_target as type_of_target
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    indexable as indexable,
)

class BaseThresholdClassifier(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Incomplete
    response_method: Incomplete
    def __init__(self, estimator, *, response_method: str = "auto") -> None: ...
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, **params): ...
    @property
    def classes_(self): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def decision_function(self, X): ...
    def __sklearn_tags__(self): ...

class FixedThresholdClassifier(BaseThresholdClassifier):
    pos_label: Incomplete
    threshold: Incomplete
    def __init__(
        self,
        estimator,
        *,
        threshold: str = "auto",
        pos_label=None,
        response_method: str = "auto",
    ) -> None: ...
    @property
    def classes_(self): ...
    def predict(self, X): ...
    def get_metadata_routing(self): ...

class TunedThresholdClassifierCV(BaseThresholdClassifier):
    scoring: Incomplete
    thresholds: Incomplete
    cv: Incomplete
    refit: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    store_cv_results: Incomplete
    def __init__(
        self,
        estimator,
        *,
        scoring: str = "balanced_accuracy",
        response_method: str = "auto",
        thresholds: int = 100,
        cv=None,
        refit: bool = True,
        n_jobs=None,
        random_state=None,
        store_cv_results: bool = False,
    ) -> None: ...
    def predict(self, X): ...
    def get_metadata_routing(self): ...
