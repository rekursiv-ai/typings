from typing import Any

from sklearn.exceptions import UndefinedMetricWarning as UndefinedMetricWarning
from sklearn.preprocessing import label_binarize as label_binarize
from sklearn.utils import (
    assert_all_finite as assert_all_finite,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    column_or_1d as column_or_1d,
)
from sklearn.utils._array_api import (
    get_namespace_and_device as get_namespace_and_device,
    size as size,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.multiclass import type_of_target as type_of_target
from sklearn.utils.sparsefuncs import count_nonzero as count_nonzero

def auc(x, y): ...
def average_precision_score(
    y_true,
    y_score,
    *,
    average: str = "macro",
    pos_label: int = 1,
    sample_weight=None,
): ...
def det_curve(
    y_true,
    y_score,
    pos_label=None,
    sample_weight=None,
    drop_intermediate: bool = False,
): ...
def roc_auc_score(
    y_true: Any,
    y_score: Any,
    *,
    average: str = "macro",
    sample_weight: Any = None,
    max_fpr: Any = None,
    multi_class: str = "raise",
    labels: Any = None,
) -> float: ...
def confusion_matrix_at_thresholds(
    y_true,
    y_score,
    pos_label=None,
    sample_weight=None,
): ...
def precision_recall_curve(
    y_true,
    y_score,
    *,
    pos_label=None,
    sample_weight=None,
    drop_intermediate: bool = False,
): ...
def roc_curve(
    y_true,
    y_score,
    *,
    pos_label=None,
    sample_weight=None,
    drop_intermediate: bool = True,
): ...
def label_ranking_average_precision_score(y_true, y_score, *, sample_weight=None): ...
def coverage_error(y_true, y_score, *, sample_weight=None): ...
def label_ranking_loss(y_true, y_score, *, sample_weight=None): ...
def dcg_score(
    y_true,
    y_score,
    *,
    k=None,
    log_base: int = 2,
    sample_weight=None,
    ignore_ties: bool = False,
): ...
def ndcg_score(
    y_true,
    y_score,
    *,
    k=None,
    sample_weight=None,
    ignore_ties: bool = False,
): ...
def top_k_accuracy_score(
    y_true,
    y_score,
    *,
    k: int = 2,
    normalize: bool = True,
    sample_weight=None,
    labels=None,
): ...
