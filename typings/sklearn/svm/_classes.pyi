from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    OutlierMixin as OutlierMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.linear_model._base import (
    LinearClassifierMixin as LinearClassifierMixin,
    LinearModel as LinearModel,
    SparseCoefMixin as SparseCoefMixin,
)
from sklearn.svm._base import (
    BaseLibSVM as BaseLibSVM,
    BaseSVC as BaseSVC,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.validation import validate_data as validate_data

class LinearSVC(LinearClassifierMixin, SparseCoefMixin, BaseEstimator):
    dual: Incomplete
    tol: Incomplete
    C: Incomplete
    multi_class: Incomplete
    fit_intercept: Incomplete
    intercept_scaling: Incomplete
    class_weight: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    max_iter: Incomplete
    penalty: Incomplete
    loss: Incomplete
    def __init__(
        self,
        penalty: str = "l2",
        loss: str = "squared_hinge",
        *,
        dual: str = "auto",
        tol: float = 0.0001,
        C: float = 1.0,
        multi_class: str = "ovr",
        fit_intercept: bool = True,
        intercept_scaling: int = 1,
        class_weight=None,
        verbose: int = 0,
        random_state=None,
        max_iter: int = 1000,
    ) -> None: ...
    classes_: Incomplete
    n_iter_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class LinearSVR(RegressorMixin, LinearModel):
    tol: Incomplete
    C: Incomplete
    epsilon: Incomplete
    fit_intercept: Incomplete
    intercept_scaling: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    max_iter: Incomplete
    dual: Incomplete
    loss: Incomplete
    def __init__(
        self,
        *,
        epsilon: float = 0.0,
        tol: float = 0.0001,
        C: float = 1.0,
        loss: str = "epsilon_insensitive",
        fit_intercept: bool = True,
        intercept_scaling: float = 1.0,
        dual: str = "auto",
        verbose: int = 0,
        random_state=None,
        max_iter: int = 1000,
    ) -> None: ...
    coef_: Incomplete
    n_iter_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class SVC(BaseSVC):
    def __init__(
        self,
        *,
        C: float = 1.0,
        kernel: str = "rbf",
        degree: int = 3,
        gamma: str = "scale",
        coef0: float = 0.0,
        shrinking: bool = True,
        probability: bool = False,
        tol: float = 0.001,
        cache_size: int = 200,
        class_weight=None,
        verbose: bool = False,
        max_iter: int = -1,
        decision_function_shape: str = "ovr",
        break_ties: bool = False,
        random_state=None,
    ) -> None: ...

class NuSVC(BaseSVC):
    def __init__(
        self,
        *,
        nu: float = 0.5,
        kernel: str = "rbf",
        degree: int = 3,
        gamma: str = "scale",
        coef0: float = 0.0,
        shrinking: bool = True,
        probability: bool = False,
        tol: float = 0.001,
        cache_size: int = 200,
        class_weight=None,
        verbose: bool = False,
        max_iter: int = -1,
        decision_function_shape: str = "ovr",
        break_ties: bool = False,
        random_state=None,
    ) -> None: ...

class SVR(RegressorMixin, BaseLibSVM):
    def __init__(
        self,
        *,
        kernel: str = "rbf",
        degree: int = 3,
        gamma: str = "scale",
        coef0: float = 0.0,
        tol: float = 0.001,
        C: float = 1.0,
        epsilon: float = 0.1,
        shrinking: bool = True,
        cache_size: int = 200,
        verbose: bool = False,
        max_iter: int = -1,
    ) -> None: ...

class NuSVR(RegressorMixin, BaseLibSVM):
    def __init__(
        self,
        *,
        nu: float = 0.5,
        C: float = 1.0,
        kernel: str = "rbf",
        degree: int = 3,
        gamma: str = "scale",
        coef0: float = 0.0,
        shrinking: bool = True,
        tol: float = 0.001,
        cache_size: int = 200,
        verbose: bool = False,
        max_iter: int = -1,
    ) -> None: ...

class OneClassSVM(OutlierMixin, BaseLibSVM):
    def __init__(
        self,
        *,
        kernel: str = "rbf",
        degree: int = 3,
        gamma: str = "scale",
        coef0: float = 0.0,
        tol: float = 0.001,
        nu: float = 0.5,
        shrinking: bool = True,
        cache_size: int = 200,
        verbose: bool = False,
        max_iter: int = -1,
    ) -> None: ...
    offset_: Incomplete
    def fit(self, X, y=None, sample_weight=None): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
    def predict(self, X): ...
