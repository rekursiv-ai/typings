from _typeshed import Incomplete
from sklearn.ensemble._hist_gradient_boosting.common import (
    PREDICTOR_RECORD_DTYPE as PREDICTOR_RECORD_DTYPE,
    Y_DTYPE as Y_DTYPE,
)

class TreePredictor:
    nodes: Incomplete
    binned_left_cat_bitsets: Incomplete
    raw_left_cat_bitsets: Incomplete
    def __init__(
        self,
        nodes,
        binned_left_cat_bitsets,
        raw_left_cat_bitsets,
    ) -> None: ...
    def get_n_leaf_nodes(self): ...
    def get_max_depth(self): ...
    def predict(self, X, known_cat_bitsets, f_idx_map, n_threads): ...
    def predict_binned(self, X, missing_values_bin_idx, n_threads): ...
    def compute_partial_dependence(self, grid, target_features, out) -> None: ...
