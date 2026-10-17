from sklearn.metrics.cluster._expected_mutual_info_fast import (
    expected_mutual_information as expected_mutual_information,
)
from sklearn.utils import deprecated as deprecated
from sklearn.utils._array_api import (
    get_namespace_and_device as get_namespace_and_device,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.multiclass import type_of_target as type_of_target
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
)

def check_clusterings(labels_true, labels_pred): ...
def contingency_matrix(
    labels_true,
    labels_pred,
    *,
    eps=None,
    sparse: bool = False,
    dtype=...,
): ...
def pair_confusion_matrix(labels_true, labels_pred): ...
def rand_score(labels_true, labels_pred): ...
def adjusted_rand_score(labels_true, labels_pred): ...
def homogeneity_completeness_v_measure(
    labels_true,
    labels_pred,
    *,
    beta: float = 1.0,
): ...
def homogeneity_score(labels_true, labels_pred): ...
def completeness_score(labels_true, labels_pred): ...
def v_measure_score(labels_true, labels_pred, *, beta: float = 1.0): ...
def mutual_info_score(labels_true, labels_pred, *, contingency=None): ...
def adjusted_mutual_info_score(
    labels_true,
    labels_pred,
    *,
    average_method: str = "arithmetic",
): ...
def normalized_mutual_info_score(
    labels_true,
    labels_pred,
    *,
    average_method: str = "arithmetic",
): ...
def fowlkes_mallows_score(labels_true, labels_pred, *, sparse: str = "deprecated"): ...
def entropy(labels): ...
