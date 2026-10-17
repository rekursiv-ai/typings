from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
)
from sklearn.exceptions import (
    ConvergenceWarning as ConvergenceWarning,
    NotFittedError as NotFittedError,
)
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    compute_class_weight as compute_class_weight,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.validation import (
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

LIBSVM_IMPL: Incomplete

class BaseLibSVM(BaseEstimator, metaclass=ABCMeta):
    kernel: Incomplete
    degree: Incomplete
    gamma: Incomplete
    coef0: Incomplete
    tol: Incomplete
    C: Incomplete
    nu: Incomplete
    epsilon: Incomplete
    shrinking: Incomplete
    probability: Incomplete
    cache_size: Incomplete
    class_weight: Incomplete
    verbose: Incomplete
    max_iter: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(
        self,
        kernel,
        degree,
        gamma,
        coef0,
        tol,
        C,
        nu,
        epsilon,
        shrinking,
        probability,
        cache_size,
        class_weight,
        verbose,
        max_iter,
        random_state,
    ): ...
    def __sklearn_tags__(self): ...
    shape_fit_: Incomplete
    dual_coef_: Incomplete
    n_iter_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def predict(self, X): ...
    @property
    def coef_(self): ...
    @property
    def n_support_(self): ...

class BaseSVC(ClassifierMixin, BaseLibSVM, metaclass=ABCMeta):
    decision_function_shape: Incomplete
    break_ties: Incomplete
    @abstractmethod
    def __init__(
        self,
        kernel,
        degree,
        gamma,
        coef0,
        tol,
        C,
        nu,
        shrinking,
        probability,
        cache_size,
        class_weight,
        verbose,
        max_iter,
        decision_function_shape,
        random_state,
        break_ties,
    ): ...
    def decision_function(self, X): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    @property
    def probA_(self): ...
    @property
    def probB_(self): ...
    def __sklearn_tags__(self): ...
