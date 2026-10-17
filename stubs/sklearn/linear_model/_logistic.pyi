from _typeshed import Incomplete
from sklearn._loss.loss import (
    HalfBinomialLoss as HalfBinomialLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
)
from sklearn.linear_model._base import (
    BaseEstimator as BaseEstimator,
    LinearClassifierMixin as LinearClassifierMixin,
    SparseCoefMixin as SparseCoefMixin,
)
from sklearn.linear_model._glm.glm import NewtonCholeskySolver as NewtonCholeskySolver
from sklearn.linear_model._linear_loss import LinearModelLoss as LinearModelLoss
from sklearn.linear_model._sag import sag_solver as sag_solver
from sklearn.metrics import (
    get_scorer as get_scorer,
    get_scorer_names as get_scorer_names,
)
from sklearn.model_selection import check_cv as check_cv
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import (
    Bunch as Bunch,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_random_state as check_random_state,
    compute_class_weight as compute_class_weight,
)
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import (
    row_norms as row_norms,
    softmax as softmax,
)
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
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class LogisticRegression(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    penalty: Incomplete
    C: Incomplete
    l1_ratio: Incomplete
    dual: Incomplete
    tol: Incomplete
    fit_intercept: Incomplete
    intercept_scaling: Incomplete
    class_weight: Incomplete
    random_state: Incomplete
    solver: Incomplete
    max_iter: Incomplete
    verbose: Incomplete
    warm_start: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        penalty: str = "deprecated",
        *,
        C: float = 1.0,
        l1_ratio: float = 0.0,
        dual: bool = False,
        tol: float = 0.0001,
        fit_intercept: bool = True,
        intercept_scaling: int = 1,
        class_weight=None,
        random_state=None,
        solver: str = "lbfgs",
        max_iter: int = 100,
        verbose: int = 0,
        warm_start: bool = False,
        n_jobs=None,
    ) -> None: ...
    classes_: Incomplete
    n_iter_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def __sklearn_tags__(self): ...

class LogisticRegressionCV(LogisticRegression, LinearClassifierMixin, BaseEstimator):
    Cs: Incomplete
    l1_ratios: Incomplete
    fit_intercept: Incomplete
    cv: Incomplete
    dual: Incomplete
    penalty: Incomplete
    scoring: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    class_weight: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    solver: Incomplete
    refit: Incomplete
    intercept_scaling: Incomplete
    random_state: Incomplete
    use_legacy_attributes: Incomplete
    def __init__(
        self,
        *,
        Cs: int = 10,
        l1_ratios: str = "warn",
        fit_intercept: bool = True,
        cv=None,
        dual: bool = False,
        penalty: str = "deprecated",
        scoring=None,
        solver: str = "lbfgs",
        tol: float = 0.0001,
        max_iter: int = 100,
        class_weight=None,
        n_jobs=None,
        verbose: int = 0,
        refit: bool = True,
        intercept_scaling: float = 1.0,
        random_state=None,
        use_legacy_attributes: str = "warn",
    ) -> None: ...
    Cs_: Incomplete
    n_iter_: Incomplete
    scores_: Incomplete
    coefs_paths_: Incomplete
    C_: Incomplete
    l1_ratio_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    l1_ratios_: Incomplete
    def fit(self, X, y, sample_weight=None, **params): ...
    def score(self, X, y, sample_weight=None, **score_params): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...
