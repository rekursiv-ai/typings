from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.decomposition import PCA as PCA
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.metrics import pairwise_distances as pairwise_distances
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import softmax as softmax
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.random import check_random_state as check_random_state
from sklearn.utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class NeighborhoodComponentsAnalysis(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    BaseEstimator,
):
    n_components: Incomplete
    init: Incomplete
    warm_start: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    callback: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        init: str = "auto",
        warm_start: bool = False,
        max_iter: int = 50,
        tol: float = 1e-05,
        callback=None,
        verbose: int = 0,
        random_state=None,
    ) -> None: ...
    random_state_: Incomplete
    n_iter_: int
    components_: Incomplete
    def fit(self, X, y): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
