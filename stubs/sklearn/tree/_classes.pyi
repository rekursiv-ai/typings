from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassifierMixin,
    MultiOutputMixin,
    RegressorMixin,
)

__all__ = [
    "DecisionTreeClassifier",
    "DecisionTreeRegressor",
    "ExtraTreeClassifier",
    "ExtraTreeRegressor",
]

class BaseDecisionTree(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    criterion: Incomplete
    splitter: Incomplete
    max_depth: Incomplete
    min_samples_split: Incomplete
    min_samples_leaf: Incomplete
    min_weight_fraction_leaf: Incomplete
    max_features: Incomplete
    max_leaf_nodes: Incomplete
    random_state: Incomplete
    min_impurity_decrease: Incomplete
    class_weight: Incomplete
    ccp_alpha: Incomplete
    monotonic_cst: Incomplete
    @abstractmethod
    def __init__(
        self,
        *,
        criterion,
        splitter,
        max_depth,
        min_samples_split,
        min_samples_leaf,
        min_weight_fraction_leaf,
        max_features,
        max_leaf_nodes,
        random_state,
        min_impurity_decrease,
        class_weight=None,
        ccp_alpha: float = 0.0,
        monotonic_cst=None,
    ): ...
    def get_depth(self): ...
    def get_n_leaves(self): ...
    def predict(self, X, check_input: bool = True): ...
    def apply(self, X, check_input: bool = True): ...
    def decision_path(self, X, check_input: bool = True): ...
    def cost_complexity_pruning_path(self, X, y, sample_weight=None): ...
    @property
    def feature_importances_(self): ...
    def __sklearn_tags__(self): ...

class DecisionTreeClassifier(ClassifierMixin, BaseDecisionTree):
    def __init__(
        self,
        *,
        criterion: str = "gini",
        splitter: str = "best",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features=None,
        random_state=None,
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        class_weight=None,
        ccp_alpha: float = 0.0,
        monotonic_cst=None,
    ) -> None: ...
    def fit(self, X, y, sample_weight=None, check_input: bool = True): ...
    def predict_proba(self, X, check_input: bool = True): ...
    def predict_log_proba(self, X): ...
    def __sklearn_tags__(self): ...

class DecisionTreeRegressor(RegressorMixin, BaseDecisionTree):
    def __init__(
        self,
        *,
        criterion: str = "squared_error",
        splitter: str = "best",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features=None,
        random_state=None,
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        ccp_alpha: float = 0.0,
        monotonic_cst=None,
    ) -> None: ...
    def fit(self, X, y, sample_weight=None, check_input: bool = True): ...
    def __sklearn_tags__(self): ...

class ExtraTreeClassifier(DecisionTreeClassifier):
    def __init__(
        self,
        *,
        criterion: str = "gini",
        splitter: str = "random",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: str = "sqrt",
        random_state=None,
        max_leaf_nodes=None,
        min_impurity_decrease: float = 0.0,
        class_weight=None,
        ccp_alpha: float = 0.0,
        monotonic_cst=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...

class ExtraTreeRegressor(DecisionTreeRegressor):
    def __init__(
        self,
        *,
        criterion: str = "squared_error",
        splitter: str = "random",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: float = 1.0,
        random_state=None,
        min_impurity_decrease: float = 0.0,
        max_leaf_nodes=None,
        ccp_alpha: float = 0.0,
        monotonic_cst=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
