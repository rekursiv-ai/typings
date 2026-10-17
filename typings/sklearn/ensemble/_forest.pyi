from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    ClassifierMixin,
    MultiOutputMixin,
    RegressorMixin,
    TransformerMixin,
)
from sklearn.ensemble._base import BaseEnsemble

__all__ = [
    "ExtraTreesClassifier",
    "ExtraTreesRegressor",
    "RandomForestClassifier",
    "RandomForestRegressor",
    "RandomTreesEmbedding",
]

class BaseForest(MultiOutputMixin, BaseEnsemble, metaclass=ABCMeta):
    bootstrap: Incomplete
    oob_score: Incomplete
    n_jobs: Incomplete
    random_state: Incomplete
    verbose: Incomplete
    warm_start: Incomplete
    class_weight: Incomplete
    max_samples: Incomplete
    @abstractmethod
    def __init__(
        self,
        estimator,
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight=None,
        max_samples=None,
    ): ...
    def apply(self, X): ...
    def decision_path(self, X): ...
    estimators_: Incomplete
    n_classes_: Incomplete
    classes_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    @property
    def feature_importances_(self): ...
    @property
    def estimators_samples_(self): ...
    def __sklearn_tags__(self): ...

class ForestClassifier(ClassifierMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimator,
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight=None,
        max_samples=None,
    ): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def predict_log_proba(self, X): ...
    def __sklearn_tags__(self): ...

class ForestRegressor(RegressorMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimator,
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        max_samples=None,
    ): ...
    def predict(self, X): ...
    def __sklearn_tags__(self): ...

class RandomForestClassifier(ForestClassifier):
    criterion: Incomplete
    max_depth: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    max_features: Incomplete
    max_leaf_nodes: Incomplete
    min_impurity_decrease: Incomplete
    monotonic_cst: Incomplete
    ccp_alpha: Incomplete
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: str = "gini",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: str = "sqrt",
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight=None,
        ccp_alpha: float = 0.0,
        max_samples=None,
        monotonic_cst=None,
    ) -> None: ...

class RandomForestRegressor(ForestRegressor):
    criterion: Incomplete
    max_depth: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    max_features: Incomplete
    max_leaf_nodes: Incomplete
    min_impurity_decrease: Incomplete
    ccp_alpha: Incomplete
    monotonic_cst: Incomplete
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: str = "squared_error",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: float = 1.0,
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        ccp_alpha: float = 0.0,
        max_samples=None,
        monotonic_cst=None,
    ) -> None: ...

class ExtraTreesClassifier(ForestClassifier):
    criterion: Incomplete
    max_depth: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    max_features: Incomplete
    max_leaf_nodes: Incomplete
    min_impurity_decrease: Incomplete
    ccp_alpha: Incomplete
    monotonic_cst: Incomplete
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: str = "gini",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: str = "sqrt",
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight=None,
        ccp_alpha: float = 0.0,
        max_samples=None,
        monotonic_cst=None,
    ) -> None: ...

class ExtraTreesRegressor(ForestRegressor):
    criterion: Incomplete
    max_depth: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    max_features: Incomplete
    max_leaf_nodes: Incomplete
    min_impurity_decrease: Incomplete
    ccp_alpha: Incomplete
    monotonic_cst: Incomplete
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: str = "squared_error",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: float = 1.0,
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        ccp_alpha: float = 0.0,
        max_samples=None,
        monotonic_cst=None,
    ) -> None: ...

class RandomTreesEmbedding(TransformerMixin, BaseForest):
    criterion: str
    max_features: int
    max_depth: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    max_leaf_nodes: Incomplete
    min_impurity_decrease: Incomplete
    sparse_output: Incomplete
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        max_depth: int = 5,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        sparse_output: bool = True,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
    ) -> None: ...
    def fit(self, X, y=None, sample_weight=None): ...
    one_hot_encoder_: Incomplete
    def fit_transform(self, X, y=None, sample_weight=None): ...
    def get_feature_names_out(self, input_features=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
