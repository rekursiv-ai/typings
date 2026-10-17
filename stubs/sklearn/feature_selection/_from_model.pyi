from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MetaEstimatorMixin as MetaEstimatorMixin,
    clone as clone,
)
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.feature_selection._base import SelectorMixin as SelectorMixin
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    Options as Options,
)
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    check_scalar as check_scalar,
)

class SelectFromModel(MetaEstimatorMixin, SelectorMixin, BaseEstimator):
    estimator: Incomplete
    threshold: Incomplete
    prefit: Incomplete
    importance_getter: Incomplete
    norm_order: Incomplete
    max_features: Incomplete
    def __init__(
        self,
        estimator,
        *,
        threshold=None,
        prefit: bool = False,
        norm_order: int = 1,
        max_features=None,
        importance_getter: str = "auto",
    ) -> None: ...
    estimator_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y=None, **fit_params): ...
    @property
    def threshold_(self): ...
    def partial_fit(self, X, y=None, **partial_fit_params): ...
    @property
    def n_features_in_(self): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...
