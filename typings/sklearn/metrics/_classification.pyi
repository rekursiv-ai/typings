from typing import Any

from sklearn.exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from sklearn.preprocessing import (
    LabelBinarizer as LabelBinarizer,
    LabelEncoder as LabelEncoder,
)
from sklearn.utils import (
    assert_all_finite as assert_all_finite,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_scalar as check_scalar,
    column_or_1d as column_or_1d,
)
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
    move_to as move_to,
    supported_float_dtypes as supported_float_dtypes,
    xpx as xpx,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    Options as Options,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils._unique import attach_unique as attach_unique
from sklearn.utils.multiclass import (
    type_of_target as type_of_target,
    unique_labels as unique_labels,
)

def accuracy_score(
    y_true: Any,
    y_pred: Any,
    *,
    normalize: bool = True,
    sample_weight: Any = None,
) -> float: ...
def confusion_matrix(
    y_true,
    y_pred,
    *,
    labels=None,
    sample_weight=None,
    normalize=None,
): ...
def multilabel_confusion_matrix(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    labels=None,
    samplewise: bool = False,
): ...
def cohen_kappa_score(y1, y2, *, labels=None, weights=None, sample_weight=None): ...
def jaccard_score(
    y_true,
    y_pred,
    *,
    labels=None,
    pos_label: int = 1,
    average: str = "binary",
    sample_weight=None,
    zero_division: str = "warn",
): ...
def matthews_corrcoef(y_true, y_pred, *, sample_weight=None): ...
def zero_one_loss(y_true, y_pred, *, normalize: bool = True, sample_weight=None): ...
def f1_score(
    y_true,
    y_pred,
    *,
    labels=None,
    pos_label: int = 1,
    average: str = "binary",
    sample_weight=None,
    zero_division: str = "warn",
): ...
def fbeta_score(
    y_true,
    y_pred,
    *,
    beta,
    labels=None,
    pos_label: int = 1,
    average: str = "binary",
    sample_weight=None,
    zero_division: str = "warn",
): ...
def precision_recall_fscore_support(
    y_true,
    y_pred,
    *,
    beta: float = 1.0,
    labels=None,
    pos_label: int = 1,
    average=None,
    warn_for=("precision", "recall", "f-score"),
    sample_weight=None,
    zero_division: str = "warn",
): ...
def class_likelihood_ratios(
    y_true,
    y_pred,
    *,
    labels=None,
    sample_weight=None,
    raise_warning: str = "deprecated",
    replace_undefined_by=...,
): ...
def precision_score(
    y_true,
    y_pred,
    *,
    labels=None,
    pos_label: int = 1,
    average: str = "binary",
    sample_weight=None,
    zero_division: str = "warn",
): ...
def recall_score(
    y_true,
    y_pred,
    *,
    labels=None,
    pos_label: int = 1,
    average: str = "binary",
    sample_weight=None,
    zero_division: str = "warn",
): ...
def balanced_accuracy_score(
    y_true,
    y_pred,
    *,
    sample_weight=None,
    adjusted: bool = False,
): ...
def classification_report(
    y_true,
    y_pred,
    *,
    labels=None,
    target_names=None,
    sample_weight=None,
    digits: int = 2,
    output_dict: bool = False,
    zero_division: str = "warn",
): ...
def hamming_loss(y_true, y_pred, *, sample_weight=None): ...
def log_loss(
    y_true,
    y_pred,
    *,
    normalize: bool = True,
    sample_weight=None,
    labels=None,
): ...
def hinge_loss(y_true, pred_decision, *, labels=None, sample_weight=None): ...
def brier_score_loss(
    y_true,
    y_proba,
    *,
    sample_weight=None,
    pos_label=None,
    labels=None,
    scale_by_half: str = "auto",
): ...
def d2_log_loss_score(y_true, y_pred, *, sample_weight=None, labels=None): ...
def d2_brier_score(
    y_true,
    y_proba,
    *,
    sample_weight=None,
    pos_label=None,
    labels=None,
): ...
