from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from scipy import sparse
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
    is_classifier as is_classifier,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import (
    LinearClassifierMixin as LinearClassifierMixin,
    LinearModel as LinearModel,
)
from sklearn.linear_model._sag import sag_solver as sag_solver
from sklearn.metrics import (
    check_scoring as check_scoring,
    get_scorer as get_scorer,
    get_scorer_names as get_scorer_names,
)
from sklearn.model_selection import GridSearchCV as GridSearchCV
from sklearn.preprocessing import LabelBinarizer as LabelBinarizer
from sklearn.utils import (
    Bunch as Bunch,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_scalar as check_scalar,
    column_or_1d as column_or_1d,
    compute_sample_weight as compute_sample_weight,
)
from sklearn.utils._array_api import (
    device as device,
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
    move_to as move_to,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import (
    row_norms as row_norms,
    safe_sparse_dot as safe_sparse_dot,
)
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def ridge_regression(
    X,
    y,
    alpha,
    *,
    sample_weight=None,
    solver: str = "auto",
    max_iter=None,
    tol: float = 0.0001,
    verbose: int = 0,
    positive: bool = False,
    random_state=None,
    return_n_iter: bool = False,
    return_intercept: bool = False,
    check_input: bool = True,
): ...
def resolve_solver(solver, positive, return_intercept, is_sparse, xp): ...
def resolve_solver_for_numpy(positive, return_intercept, is_sparse): ...

class _BaseRidge(LinearModel, metaclass=ABCMeta):
    alpha: Incomplete
    fit_intercept: Incomplete
    copy_X: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    solver: Incomplete
    positive: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter=None,
        tol: float = 0.0001,
        solver: str = "auto",
        positive: bool = False,
        random_state=None,
    ): ...
    def fit(self, X, y, sample_weight=None): ...

class Ridge(MultiOutputMixin, RegressorMixin, _BaseRidge):
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter=None,
        tol: float = 0.0001,
        solver: str = "auto",
        positive: bool = False,
        random_state=None,
    ) -> None: ...
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class _RidgeClassifierMixin(LinearClassifierMixin):
    def predict(self, X): ...
    def __sklearn_tags__(self): ...

class RidgeClassifier(_RidgeClassifierMixin, _BaseRidge):
    class_weight: Incomplete
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter=None,
        tol: float = 0.0001,
        class_weight=None,
        solver: str = "auto",
        positive: bool = False,
        random_state=None,
    ) -> None: ...
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class _X_CenterStackOp(sparse.linalg.LinearOperator):
    X: Incomplete
    X_mean: Incomplete
    sqrt_sw: Incomplete
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _XT_CenterStackOp(sparse.linalg.LinearOperator):
    X: Incomplete
    X_mean: Incomplete
    sqrt_sw: Incomplete
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _IdentityRegressor(RegressorMixin, BaseEstimator):
    def decision_function(self, y_predict): ...
    def predict(self, y_predict): ...

class _IdentityClassifier(LinearClassifierMixin, BaseEstimator):
    classes_: Incomplete
    def __init__(self, classes) -> None: ...
    def decision_function(self, y_predict): ...

class _RidgeGCV(LinearModel):
    alphas: Incomplete
    fit_intercept: Incomplete
    scoring: Incomplete
    copy_X: Incomplete
    gcv_mode: Incomplete
    store_cv_results: Incomplete
    is_clf: Incomplete
    alpha_per_target: Incomplete
    def __init__(
        self,
        alphas=(0.1, 1.0, 10.0),
        *,
        fit_intercept: bool = True,
        scoring=None,
        copy_X: bool = True,
        gcv_mode=None,
        store_cv_results: bool = False,
        is_clf: bool = False,
        alpha_per_target: bool = False,
    ) -> None: ...
    cv_results_: Incomplete
    alpha_: Incomplete
    best_score_: Incomplete
    dual_coef_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y, sample_weight=None, score_params=None): ...
    def __sklearn_tags__(self): ...

class _BaseRidgeCV(LinearModel):
    alphas: Incomplete
    fit_intercept: Incomplete
    scoring: Incomplete
    cv: Incomplete
    gcv_mode: Incomplete
    store_cv_results: Incomplete
    alpha_per_target: Incomplete
    def __init__(
        self,
        alphas=(0.1, 1.0, 10.0),
        *,
        fit_intercept: bool = True,
        scoring=None,
        cv=None,
        gcv_mode=None,
        store_cv_results: bool = False,
        alpha_per_target: bool = False,
    ) -> None: ...
    alpha_: Incomplete
    best_score_: Incomplete
    cv_results_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    n_features_in_: Incomplete
    feature_names_in_: Incomplete
    def fit(self, X, y, sample_weight=None, **params): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...

class RidgeCV(MultiOutputMixin, RegressorMixin, _BaseRidgeCV):
    def fit(self, X, y, sample_weight=None, **params): ...

class RidgeClassifierCV(_RidgeClassifierMixin, _BaseRidgeCV):
    class_weight: Incomplete
    def __init__(
        self,
        alphas=(0.1, 1.0, 10.0),
        *,
        fit_intercept: bool = True,
        scoring=None,
        cv=None,
        class_weight=None,
        store_cv_results: bool = False,
    ) -> None: ...
    def fit(self, X, y, sample_weight=None, **params): ...
