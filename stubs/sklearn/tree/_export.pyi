from _typeshed import Incomplete
from sklearn.base import is_classifier as is_classifier
from sklearn.tree import (
    DecisionTreeClassifier as DecisionTreeClassifier,
    DecisionTreeRegressor as DecisionTreeRegressor,
)
from sklearn.tree._reingold_tilford import (
    Tree as Tree,
    buchheim as buchheim,
)
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)

class Sentinel: ...

SENTINEL: Incomplete

def plot_tree(
    decision_tree,
    *,
    max_depth=None,
    feature_names=None,
    class_names=None,
    label: str = "all",
    filled: bool = False,
    impurity: bool = True,
    node_ids: bool = False,
    proportion: bool = False,
    rounded: bool = False,
    precision: int = 3,
    ax=None,
    fontsize=None,
): ...

class _BaseTreeExporter:
    max_depth: Incomplete
    feature_names: Incomplete
    class_names: Incomplete
    label: Incomplete
    filled: Incomplete
    impurity: Incomplete
    node_ids: Incomplete
    proportion: Incomplete
    rounded: Incomplete
    precision: Incomplete
    fontsize: Incomplete
    def __init__(
        self,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label: str = "all",
        filled: bool = False,
        impurity: bool = True,
        node_ids: bool = False,
        proportion: bool = False,
        rounded: bool = False,
        precision: int = 3,
        fontsize=None,
    ) -> None: ...
    def get_color(self, value): ...
    def get_fill_color(self, tree, node_id): ...
    def node_to_str(self, tree, node_id, criterion): ...
    def str_escape(self, string): ...

class _DOTTreeExporter(_BaseTreeExporter):
    leaves_parallel: Incomplete
    out_file: Incomplete
    special_characters: Incomplete
    fontname: Incomplete
    rotate: Incomplete
    characters: Incomplete
    ranks: Incomplete
    colors: Incomplete
    def __init__(
        self,
        out_file=...,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label: str = "all",
        filled: bool = False,
        leaves_parallel: bool = False,
        impurity: bool = True,
        node_ids: bool = False,
        proportion: bool = False,
        rotate: bool = False,
        rounded: bool = False,
        special_characters: bool = False,
        precision: int = 3,
        fontname: str = "helvetica",
    ) -> None: ...
    def export(self, decision_tree) -> None: ...
    def tail(self) -> None: ...
    def head(self) -> None: ...
    def recurse(
        self,
        tree,
        node_id,
        criterion,
        parent=None,
        depth: int = 0,
    ) -> None: ...
    def str_escape(self, string): ...

class _MPLTreeExporter(_BaseTreeExporter):
    fontsize: Incomplete
    ranks: Incomplete
    colors: Incomplete
    characters: Incomplete
    bbox_args: Incomplete
    arrow_args: Incomplete
    def __init__(
        self,
        max_depth=None,
        feature_names=None,
        class_names=None,
        label: str = "all",
        filled: bool = False,
        impurity: bool = True,
        node_ids: bool = False,
        proportion: bool = False,
        rounded: bool = False,
        precision: int = 3,
        fontsize=None,
    ) -> None: ...
    def export(self, decision_tree, ax=None): ...
    def recurse(self, node, tree, ax, max_x, max_y, depth: int = 0) -> None: ...

def export_graphviz(
    decision_tree,
    out_file=None,
    *,
    max_depth=None,
    feature_names=None,
    class_names=None,
    label: str = "all",
    filled: bool = False,
    leaves_parallel: bool = False,
    impurity: bool = True,
    node_ids: bool = False,
    proportion: bool = False,
    rotate: bool = False,
    rounded: bool = False,
    special_characters: bool = False,
    precision: int = 3,
    fontname: str = "helvetica",
): ...
def export_text(
    decision_tree,
    *,
    feature_names=None,
    class_names=None,
    max_depth: int = 10,
    spacing: int = 3,
    decimals: int = 2,
    show_weights: bool = False,
): ...
