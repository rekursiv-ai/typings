from _typeshed import Incomplete
from sklearn.base import is_regressor as is_regressor
from sklearn.metrics import (
    accuracy_score as accuracy_score,
    average_precision_score as average_precision_score,
    balanced_accuracy_score as balanced_accuracy_score,
    brier_score_loss as brier_score_loss,
    class_likelihood_ratios as class_likelihood_ratios,
    d2_absolute_error_score as d2_absolute_error_score,
    d2_brier_score as d2_brier_score,
    d2_log_loss_score as d2_log_loss_score,
    explained_variance_score as explained_variance_score,
    f1_score as f1_score,
    jaccard_score as jaccard_score,
    log_loss as log_loss,
    matthews_corrcoef as matthews_corrcoef,
    max_error as max_error,
    mean_absolute_error as mean_absolute_error,
    mean_absolute_percentage_error as mean_absolute_percentage_error,
    mean_gamma_deviance as mean_gamma_deviance,
    mean_poisson_deviance as mean_poisson_deviance,
    mean_squared_error as mean_squared_error,
    mean_squared_log_error as mean_squared_log_error,
    median_absolute_error as median_absolute_error,
    precision_score as precision_score,
    r2_score as r2_score,
    recall_score as recall_score,
    roc_auc_score as roc_auc_score,
    root_mean_squared_error as root_mean_squared_error,
    root_mean_squared_log_error as root_mean_squared_log_error,
    top_k_accuracy_score as top_k_accuracy_score,
)
from sklearn.metrics.cluster import (
    adjusted_mutual_info_score as adjusted_mutual_info_score,
    adjusted_rand_score as adjusted_rand_score,
    completeness_score as completeness_score,
    fowlkes_mallows_score as fowlkes_mallows_score,
    homogeneity_score as homogeneity_score,
    mutual_info_score as mutual_info_score,
    normalized_mutual_info_score as normalized_mutual_info_score,
    rand_score as rand_score,
    v_measure_score as v_measure_score,
)
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.metadata_routing import (
    MetadataRequest as MetadataRequest,
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    _MetadataRequester,
    get_routing_for_object as get_routing_for_object,
    process_routing as process_routing,
)

class _MultimetricScorer:
    def __init__(self, *, scorers, raise_exc: bool = True) -> None: ...
    def __call__(self, estimator, *args, **kwargs): ...
    def get_metadata_routing(self): ...

class _BaseScorer(_MetadataRequester):
    def __init__(
        self,
        score_func,
        sign,
        kwargs,
        response_method: str = "predict",
    ) -> None: ...
    def __call__(self, estimator, X, y_true, sample_weight=None, **kwargs): ...
    def set_score_request(self, **kwargs): ...

class _Scorer(_BaseScorer): ...

def get_scorer(scoring): ...

class _PassthroughScorer(_MetadataRequester):
    def __init__(self, estimator) -> None: ...
    def __call__(self, estimator, *args, **kwargs): ...
    def get_metadata_routing(self): ...

def make_scorer(
    score_func,
    *,
    response_method: str = "predict",
    greater_is_better: bool = True,
    **kwargs,
): ...

explained_variance_scorer: Incomplete
r2_scorer: Incomplete
neg_max_error_scorer: Incomplete
neg_mean_squared_error_scorer: Incomplete
neg_mean_squared_log_error_scorer: Incomplete
neg_mean_absolute_error_scorer: Incomplete
neg_mean_absolute_percentage_error_scorer: Incomplete
neg_median_absolute_error_scorer: Incomplete
neg_root_mean_squared_error_scorer: Incomplete
neg_root_mean_squared_log_error_scorer: Incomplete
neg_mean_poisson_deviance_scorer: Incomplete
neg_mean_gamma_deviance_scorer: Incomplete
d2_absolute_error_scorer: Incomplete
d2_brier_score_scorer: Incomplete
d2_log_loss_scorer: Incomplete
accuracy_scorer: Incomplete
balanced_accuracy_scorer: Incomplete
matthews_corrcoef_scorer: Incomplete

def positive_likelihood_ratio(y_true, y_pred): ...
def negative_likelihood_ratio(y_true, y_pred): ...

positive_likelihood_ratio_scorer: Incomplete
neg_negative_likelihood_ratio_scorer: Incomplete
top_k_accuracy_scorer: Incomplete
roc_auc_scorer: Incomplete
average_precision_scorer: Incomplete
roc_auc_ovo_scorer: Incomplete
roc_auc_ovo_weighted_scorer: Incomplete
roc_auc_ovr_scorer: Incomplete
roc_auc_ovr_weighted_scorer: Incomplete
neg_log_loss_scorer: Incomplete
neg_brier_score_scorer: Incomplete
brier_score_loss_scorer: Incomplete
adjusted_rand_scorer: Incomplete
rand_scorer: Incomplete
homogeneity_scorer: Incomplete
completeness_scorer: Incomplete
v_measure_scorer: Incomplete
mutual_info_scorer: Incomplete
adjusted_mutual_info_scorer: Incomplete
normalized_mutual_info_scorer: Incomplete
fowlkes_mallows_scorer: Incomplete

def get_scorer_names(): ...

qualified_name: Incomplete

def check_scoring(
    estimator=None,
    scoring=None,
    *,
    allow_none: bool = False,
    raise_exc: bool = True,
): ...

class _CurveScorer(_BaseScorer):
    def __init__(
        self,
        score_func,
        sign,
        kwargs,
        thresholds,
        response_method,
    ) -> None: ...
    @classmethod
    def from_scorer(cls, scorer, response_method, thresholds): ...
