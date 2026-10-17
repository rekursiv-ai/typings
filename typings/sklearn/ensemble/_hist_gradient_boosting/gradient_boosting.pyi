from abc import ABC, abstractmethod
from collections.abc import Generator

import abc

from _typeshed import Incomplete
from sklearn._loss.loss import (
    BaseLoss as BaseLoss,
    HalfBinomialLoss as HalfBinomialLoss,
    HalfGammaLoss as HalfGammaLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
    HalfPoissonLoss as HalfPoissonLoss,
    PinballLoss as PinballLoss,
)
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    RegressorMixin as RegressorMixin,
    is_classifier as is_classifier,
)
from sklearn.compose import ColumnTransformer as ColumnTransformer
from sklearn.ensemble._hist_gradient_boosting.common import (
    G_H_DTYPE as G_H_DTYPE,
    X_DTYPE as X_DTYPE,
    Y_DTYPE as Y_DTYPE,
)
from sklearn.ensemble._hist_gradient_boosting.grower import TreeGrower as TreeGrower
from sklearn.metrics import check_scoring as check_scoring
from sklearn.model_selection import train_test_split as train_test_split
from sklearn.preprocessing import (
    FunctionTransformer as FunctionTransformer,
    LabelEncoder as LabelEncoder,
    OrdinalEncoder as OrdinalEncoder,
)
from sklearn.utils import (
    check_random_state as check_random_state,
    compute_sample_weight as compute_sample_weight,
    resample as resample,
)
from sklearn.utils._dataframe import is_pandas_df as is_pandas_df
from sklearn.utils._missing import is_scalar_nan as is_scalar_nan
from sklearn.utils._param_validation import (
    Interval as Interval,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class BaseHistGradientBoosting(BaseEstimator, ABC, metaclass=abc.ABCMeta):
    loss: Incomplete
    learning_rate: Incomplete
    max_iter: Incomplete
    max_leaf_nodes: Incomplete
    max_depth: Incomplete
    min_samples_leaf: Incomplete
    l2_regularization: Incomplete
    max_features: Incomplete
    max_bins: Incomplete
    monotonic_cst: Incomplete
    interaction_cst: Incomplete
    categorical_features: Incomplete
    warm_start: Incomplete
    early_stopping: Incomplete
    scoring: Incomplete
    validation_fraction: Incomplete
    n_iter_no_change: Incomplete
    tol: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(
        self,
        loss,
        *,
        learning_rate,
        max_iter,
        max_leaf_nodes,
        max_depth,
        min_samples_leaf,
        l2_regularization,
        max_features,
        max_bins,
        categorical_features,
        monotonic_cst,
        interaction_cst,
        warm_start,
        early_stopping,
        scoring,
        validation_fraction,
        n_iter_no_change,
        tol,
        verbose,
        random_state,
    ): ...
    do_early_stopping_: Incomplete
    train_score_: Incomplete
    validation_score_: Incomplete
    def fit(
        self,
        X,
        y,
        sample_weight=None,
        *,
        X_val=None,
        y_val=None,
        sample_weight_val=None,
    ): ...
    def __sklearn_tags__(self): ...
    @property
    def n_iter_(self): ...

class HistGradientBoostingRegressor(RegressorMixin, BaseHistGradientBoosting):
    quantile: Incomplete
    def __init__(
        self,
        loss: str = "squared_error",
        *,
        quantile=None,
        learning_rate: float = 0.1,
        max_iter: int = 100,
        max_leaf_nodes: int = 31,
        max_depth=None,
        min_samples_leaf: int = 20,
        l2_regularization: float = 0.0,
        max_features: float = 1.0,
        max_bins: int = 255,
        categorical_features: str = "from_dtype",
        monotonic_cst=None,
        interaction_cst=None,
        warm_start: bool = False,
        early_stopping: str = "auto",
        scoring: str = "loss",
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 10,
        tol: float = 1e-07,
        verbose: int = 0,
        random_state=None,
    ) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> Generator[Incomplete]: ...

class HistGradientBoostingClassifier(ClassifierMixin, BaseHistGradientBoosting):
    class_weight: Incomplete
    def __init__(
        self,
        loss: str = "log_loss",
        *,
        learning_rate: float = 0.1,
        max_iter: int = 100,
        max_leaf_nodes: int = 31,
        max_depth=None,
        min_samples_leaf: int = 20,
        l2_regularization: float = 0.0,
        max_features: float = 1.0,
        max_bins: int = 255,
        categorical_features: str = "from_dtype",
        monotonic_cst=None,
        interaction_cst=None,
        warm_start: bool = False,
        early_stopping: str = "auto",
        scoring: str = "loss",
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 10,
        tol: float = 1e-07,
        verbose: int = 0,
        random_state=None,
        class_weight=None,
    ) -> None: ...
    def predict(self, X): ...
    def staged_predict(self, X) -> Generator[Incomplete]: ...
    def predict_proba(self, X): ...
    def staged_predict_proba(self, X) -> Generator[Incomplete]: ...
    def decision_function(self, X): ...
    def staged_decision_function(self, X) -> Generator[Incomplete]: ...
