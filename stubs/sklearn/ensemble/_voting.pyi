from abc import abstractmethod

import abc

from _typeshed import Incomplete
from sklearn.base import (
    ClassifierMixin as ClassifierMixin,
    RegressorMixin as RegressorMixin,
    TransformerMixin as TransformerMixin,
    clone as clone,
)
from sklearn.ensemble._base import _BaseHeterogeneousEnsemble
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import StrOptions as StrOptions
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
    column_or_1d as column_or_1d,
)

class _BaseVoting(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=abc.ABCMeta):
    estimators_: Incomplete
    named_estimators_: Incomplete
    feature_names_in_: Incomplete
    @abstractmethod
    def fit(self, X, y, **fit_params): ...
    def fit_transform(self, X, y=None, **fit_params): ...
    @property
    def n_features_in_(self): ...
    def get_metadata_routing(self): ...

class VotingClassifier(ClassifierMixin, _BaseVoting):
    voting: Incomplete
    weights: Incomplete
    n_jobs: Incomplete
    flatten_transform: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        estimators,
        *,
        voting: str = "hard",
        weights=None,
        n_jobs=None,
        flatten_transform: bool = True,
        verbose: bool = False,
    ) -> None: ...
    le_: Incomplete
    classes_: Incomplete
    def fit(self, X, y, **fit_params): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_tags__(self): ...

class VotingRegressor(RegressorMixin, _BaseVoting):
    weights: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        estimators,
        *,
        weights=None,
        n_jobs=None,
        verbose: bool = False,
    ) -> None: ...
    def fit(self, X, y, **fit_params): ...
    def predict(self, X): ...
    def transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
