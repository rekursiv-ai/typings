from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
)
from sklearn.discriminant_analysis import (
    DiscriminantAnalysisPredictionMixin as DiscriminantAnalysisPredictionMixin,
)
from sklearn.metrics.pairwise import (
    pairwise_distances as pairwise_distances,
    pairwise_distances_argmin as pairwise_distances_argmin,
)
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import get_tags as get_tags
from sklearn.utils._available_if import available_if as available_if
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.sparsefuncs import csc_median_axis_0 as csc_median_axis_0
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class NearestCentroid(
    DiscriminantAnalysisPredictionMixin,
    ClassifierMixin,
    BaseEstimator,
):
    metric: Incomplete
    shrink_threshold: Incomplete
    priors: Incomplete
    def __init__(
        self,
        metric: str = "euclidean",
        *,
        shrink_threshold=None,
        priors: str = "uniform",
    ) -> None: ...
    classes_: Incomplete
    class_prior_: Incomplete
    centroids_: Incomplete
    within_class_std_dev_: Incomplete
    deviations_: Incomplete
    def fit(self, X, y): ...
    def predict(self, X): ...
    decision_function: Incomplete
    predict_proba: Incomplete
    predict_log_proba: Incomplete
    def __sklearn_tags__(self): ...
