from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    ClassifierMixin as ClassifierMixin,
    RegressorMixin as RegressorMixin,
    TransformerMixin as TransformerMixin,
    clone as clone,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
)
from sklearn.ensemble._base import _BaseHeterogeneousEnsemble
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.linear_model import (
    LogisticRegression as LogisticRegression,
    RidgeCV as RidgeCV,
)
from sklearn.model_selection import (
    check_cv as check_cv,
    cross_val_predict as cross_val_predict,
)
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    StrOptions as StrOptions,
)
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
    type_of_target as type_of_target,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    column_or_1d as column_or_1d,
)

class _BaseStacking(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=ABCMeta):
    final_estimator: Incomplete
    cv: Incomplete
    stack_method: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    passthrough: Incomplete
    @abstractmethod
    def __init__(
        self,
        estimators,
        final_estimator=None,
        *,
        cv=None,
        stack_method: str = "auto",
        n_jobs=None,
        verbose: int = 0,
        passthrough: bool = False,
    ): ...
    estimators_: Incomplete
    named_estimators_: Incomplete
    feature_names_in_: Incomplete
    stack_method_: Incomplete
    def fit(self, X, y, **fit_params): ...
    @property
    def n_features_in_(self): ...
    def get_feature_names_out(self, input_features=None): ...
    def predict(self, X, **predict_params): ...
    def get_metadata_routing(self): ...

class StackingClassifier(ClassifierMixin, _BaseStacking):
    def __init__(
        self,
        estimators,
        final_estimator=None,
        *,
        cv=None,
        stack_method: str = "auto",
        n_jobs=None,
        passthrough: bool = False,
        verbose: int = 0,
    ) -> None: ...
    classes_: Incomplete
    def fit(self, X, y, **fit_params): ...
    def predict(self, X, **predict_params): ...
    def predict_proba(self, X): ...
    def decision_function(self, X): ...
    def transform(self, X): ...

class StackingRegressor(RegressorMixin, _BaseStacking):
    def __init__(
        self,
        estimators,
        final_estimator=None,
        *,
        cv=None,
        n_jobs=None,
        passthrough: bool = False,
        verbose: int = 0,
    ) -> None: ...
    def fit(self, X, y, **fit_params): ...
    def transform(self, X): ...
    def fit_transform(self, X, y, **fit_params): ...
    def predict(self, X, **predict_params): ...
