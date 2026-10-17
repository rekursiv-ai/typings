from abc import ABCMeta, abstractmethod
from collections.abc import Generator

from _typeshed import Incomplete
from sklearn._loss.loss import (
    AbsoluteError as AbsoluteError,
    ExponentialLoss as ExponentialLoss,
    HalfBinomialLoss as HalfBinomialLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
    HalfSquaredError as HalfSquaredError,
    HuberLoss as HuberLoss,
    PinballLoss as PinballLoss,
)
from sklearn.base import (
    ClassifierMixin as ClassifierMixin,
    RegressorMixin as RegressorMixin,
    is_classifier as is_classifier,
)
from sklearn.dummy import (
    DummyClassifier as DummyClassifier,
    DummyRegressor as DummyRegressor,
)
from sklearn.ensemble._base import BaseEnsemble as BaseEnsemble
from sklearn.ensemble._gradient_boosting import (
    predict_stage as predict_stage,
    predict_stages as predict_stages,
)
from sklearn.exceptions import NotFittedError as NotFittedError
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.tree import DecisionTreeRegressor as DecisionTreeRegressor
from sklearn.tree._tree import (
    DOUBLE as DOUBLE,
    DTYPE as DTYPE,
    TREE_LEAF as TREE_LEAF,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
)
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def set_huber_delta(loss, y_true, raw_prediction, sample_weight=None) -> None: ...

class VerboseReporter:
    verbose: Incomplete
    def __init__(self, verbose) -> None: ...
    verbose_fmt: Incomplete
    verbose_mod: int
    start_time: Incomplete
    begin_at_stage: Incomplete
    def init(self, est, begin_at_stage: int = 0) -> None: ...
    def update(self, j, est) -> None: ...

class BaseGradientBoosting(BaseEnsemble, metaclass=ABCMeta):
    n_estimators: Incomplete
    learning_rate: Incomplete
    loss: Incomplete
    criterion: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    subsample: Incomplete
    max_features: Incomplete
    max_depth: Incomplete
    min_impurity_decrease: Incomplete
    ccp_alpha: Incomplete
    init: Incomplete
    random_state: Incomplete
    alpha: Incomplete
    verbose: Incomplete
    max_leaf_nodes: Incomplete
    warm_start: Incomplete
    validation_fraction: Incomplete
    n_iter_no_change: Incomplete
    tol: Incomplete
    @abstractmethod
    def __init__(
        self,
        *,
        loss,
        learning_rate,
        n_estimators,
        criterion,
        min_samples_split,
        min_samples_leaf,
        min_weight_fraction_leaf,
        max_depth,
        min_impurity_decrease,
        init,
        subsample,
        max_features,
        ccp_alpha,
        random_state,
        alpha: float = 0.9,
        verbose: int = 0,
        max_leaf_nodes=None,
        warm_start: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change=None,
        tol: float = 0.0001,
    ): ...
    estimators_: Incomplete
    train_score_: Incomplete
    oob_improvement_: Incomplete
    oob_scores_: Incomplete
    oob_score_: Incomplete
    n_estimators_: Incomplete
    def fit(self, X, y, sample_weight=None, monitor=None): ...
    @property
    def feature_importances_(self): ...
    def apply(self, X): ...
    def __sklearn_tags__(self): ...

class GradientBoostingClassifier(ClassifierMixin, BaseGradientBoosting):
    def __init__(
        self,
        *,
        loss: str = "log_loss",
        learning_rate: float = 0.1,
        n_estimators: int = 100,
        subsample: float = 1.0,
        criterion: str = "friedman_mse",
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_depth: int = 3,
        min_impurity_decrease: float = 0.0,
        init=None,
        random_state=None,
        max_features=None,
        verbose: int = 0,
        max_leaf_nodes=None,
        warm_start: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change=None,
        tol: float = 0.0001,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def decision_function(self, X): ...
    def staged_decision_function(self, X) -> Generator[Incomplete, Incomplete]: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> Generator[Incomplete]: ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def staged_predict_proba(self, X) -> Generator[Incomplete]: ...

class GradientBoostingRegressor(RegressorMixin, BaseGradientBoosting):
    def __init__(
        self,
        *,
        loss: str = "squared_error",
        learning_rate: float = 0.1,
        n_estimators: int = 100,
        subsample: float = 1.0,
        criterion: str = "friedman_mse",
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_depth: int = 3,
        min_impurity_decrease: float = 0.0,
        init=None,
        random_state=None,
        max_features=None,
        alpha: float = 0.9,
        verbose: int = 0,
        max_leaf_nodes=None,
        warm_start: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change=None,
        tol: float = 0.0001,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> Generator[Incomplete]: ...
    def apply(self, X): ...
