from abc import ABC, abstractmethod

import abc

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    RegressorMixin as RegressorMixin,
    is_classifier as is_classifier,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.metrics import (
    accuracy_score as accuracy_score,
    r2_score as r2_score,
)
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.neural_network._base import (
    ACTIVATIONS as ACTIVATIONS,
    DERIVATIVES as DERIVATIVES,
    LOSS_FUNCTIONS as LOSS_FUNCTIONS,
)
from sklearn.neural_network._stochastic_optimizers import (
    AdamOptimizer as AdamOptimizer,
    SGDOptimizer as SGDOptimizer,
)
from sklearn.preprocessing import LabelBinarizer as LabelBinarizer
from sklearn.utils import (
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    gen_batches as gen_batches,
    shuffle as shuffle,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    Options as Options,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.metaestimators import available_if as available_if
from sklearn.utils.multiclass import (
    type_of_target as type_of_target,
    unique_labels as unique_labels,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class BaseMultilayerPerceptron(BaseEstimator, ABC, metaclass=abc.ABCMeta):
    activation: Incomplete
    solver: Incomplete
    alpha: Incomplete
    batch_size: Incomplete
    learning_rate: Incomplete
    learning_rate_init: Incomplete
    power_t: Incomplete
    max_iter: Incomplete
    loss: Incomplete
    hidden_layer_sizes: Incomplete
    shuffle: Incomplete
    random_state: Incomplete
    tol: Incomplete
    verbose: Incomplete
    warm_start: Incomplete
    momentum: Incomplete
    nesterovs_momentum: Incomplete
    early_stopping: Incomplete
    validation_fraction: Incomplete
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    n_iter_no_change: Incomplete
    max_fun: Incomplete
    @abstractmethod
    def __init__(
        self,
        hidden_layer_sizes,
        activation,
        solver,
        alpha,
        batch_size,
        learning_rate,
        learning_rate_init,
        power_t,
        max_iter,
        loss,
        shuffle,
        random_state,
        tol,
        verbose,
        warm_start,
        momentum,
        nesterovs_momentum,
        early_stopping,
        validation_fraction,
        beta_1,
        beta_2,
        epsilon,
        n_iter_no_change,
        max_fun,
    ): ...
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...

class MLPClassifier(ClassifierMixin, BaseMultilayerPerceptron):
    def __init__(
        self,
        hidden_layer_sizes=(100,),
        activation: str = "relu",
        *,
        solver: str = "adam",
        alpha: float = 0.0001,
        batch_size: str = "auto",
        learning_rate: str = "constant",
        learning_rate_init: float = 0.001,
        power_t: float = 0.5,
        max_iter: int = 200,
        shuffle: bool = True,
        random_state=None,
        tol: float = 0.0001,
        verbose: bool = False,
        warm_start: bool = False,
        momentum: float = 0.9,
        nesterovs_momentum: bool = True,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-08,
        n_iter_no_change: int = 10,
        max_fun: int = 15000,
    ) -> None: ...
    def predict(self, X): ...
    def partial_fit(self, X, y, sample_weight=None, classes=None): ...
    def predict_log_proba(self, X): ...
    def predict_proba(self, X): ...
    def __sklearn_tags__(self): ...

class MLPRegressor(RegressorMixin, BaseMultilayerPerceptron):
    def __init__(
        self,
        loss: str = "squared_error",
        hidden_layer_sizes=(100,),
        activation: str = "relu",
        *,
        solver: str = "adam",
        alpha: float = 0.0001,
        batch_size: str = "auto",
        learning_rate: str = "constant",
        learning_rate_init: float = 0.001,
        power_t: float = 0.5,
        max_iter: int = 200,
        shuffle: bool = True,
        random_state=None,
        tol: float = 0.0001,
        verbose: bool = False,
        warm_start: bool = False,
        momentum: float = 0.9,
        nesterovs_momentum: bool = True,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-08,
        n_iter_no_change: int = 10,
        max_fun: int = 15000,
    ) -> None: ...
    def predict(self, X): ...
    def partial_fit(self, X, y, sample_weight=None): ...
