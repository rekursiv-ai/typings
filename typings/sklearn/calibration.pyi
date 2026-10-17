from _typeshed import Incomplete
from sklearn._loss import (
    HalfBinomialLoss as HalfBinomialLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
)
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    MetaEstimatorMixin as MetaEstimatorMixin,
    RegressorMixin as RegressorMixin,
    clone as clone,
)
from sklearn.frozen import FrozenEstimator as FrozenEstimator
from sklearn.isotonic import IsotonicRegression as IsotonicRegression
from sklearn.model_selection import (
    LeaveOneOut as LeaveOneOut,
    check_cv as check_cv,
    cross_val_predict as cross_val_predict,
)
from sklearn.preprocessing import (
    LabelEncoder as LabelEncoder,
    label_binarize as label_binarize,
)
from sklearn.svm import LinearSVC as LinearSVC
from sklearn.utils import (
    Bunch as Bunch,
    column_or_1d as column_or_1d,
    get_tags as get_tags,
    indexable as indexable,
)
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
    move_to as move_to,
)
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin
from sklearn.utils.extmath import softmax as softmax
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
)

class CalibratedClassifierCV(ClassifierMixin, MetaEstimatorMixin, BaseEstimator):
    estimator: Incomplete
    method: Incomplete
    cv: Incomplete
    n_jobs: Incomplete
    ensemble: Incomplete
    def __init__(
        self,
        estimator=None,
        *,
        method: str = "sigmoid",
        cv=None,
        n_jobs=None,
        ensemble: str = "auto",
    ) -> None: ...
    calibrated_classifiers_: Incomplete
    classes_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, sample_weight=None, **fit_params): ...
    def predict_proba(self, X): ...
    def predict(self, X): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...

class _CalibratedClassifier:
    estimator: Incomplete
    calibrators: Incomplete
    classes: Incomplete
    method: Incomplete
    def __init__(
        self,
        estimator,
        calibrators,
        *,
        classes,
        method: str = "sigmoid",
    ) -> None: ...
    def predict_proba(self, X): ...

class _SigmoidCalibration(RegressorMixin, BaseEstimator):
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, T): ...

class _TemperatureScaling(RegressorMixin, BaseEstimator):
    beta_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...

def calibration_curve(
    y_true,
    y_prob,
    *,
    pos_label=None,
    n_bins: int = 5,
    strategy: str = "uniform",
): ...

class CalibrationDisplay(_BinaryClassifierCurveDisplayMixin):
    prob_true: Incomplete
    prob_pred: Incomplete
    y_prob: Incomplete
    estimator_name: Incomplete
    pos_label: Incomplete
    def __init__(
        self,
        prob_true,
        prob_pred,
        y_prob,
        *,
        estimator_name=None,
        pos_label=None,
    ) -> None: ...
    line_: Incomplete
    def plot(self, *, ax=None, name=None, ref_line: bool = True, **kwargs): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        y,
        *,
        n_bins: int = 5,
        strategy: str = "uniform",
        pos_label=None,
        name=None,
        ax=None,
        ref_line: bool = True,
        **kwargs,
    ): ...
    @classmethod
    def from_predictions(
        cls,
        y_true,
        y_prob,
        *,
        n_bins: int = 5,
        strategy: str = "uniform",
        pos_label=None,
        name=None,
        ax=None,
        ref_line: bool = True,
        **kwargs,
    ): ...
