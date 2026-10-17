from _typeshed import Incomplete
from sklearn.ensemble._hist_gradient_boosting._bitset import (
    set_raw_bitset_from_binned_bitset as set_raw_bitset_from_binned_bitset,
)
from sklearn.ensemble._hist_gradient_boosting.common import (
    PREDICTOR_RECORD_DTYPE as PREDICTOR_RECORD_DTYPE,
    X_BITSET_INNER_DTYPE as X_BITSET_INNER_DTYPE,
    MonotonicConstraint as MonotonicConstraint,
)
from sklearn.ensemble._hist_gradient_boosting.histogram import (
    HistogramBuilder as HistogramBuilder,
)
from sklearn.ensemble._hist_gradient_boosting.predictor import (
    TreePredictor as TreePredictor,
)
from sklearn.ensemble._hist_gradient_boosting.splitting import Splitter as Splitter

class TreeNode:
    depth: Incomplete
    sample_indices: Incomplete
    n_samples: Incomplete
    sum_gradients: Incomplete
    sum_hessians: Incomplete
    value: Incomplete
    is_leaf: bool
    allowed_features: Incomplete
    interaction_cst_indices: Incomplete
    split_info: Incomplete
    left_child: Incomplete
    right_child: Incomplete
    histograms: Incomplete
    partition_start: Incomplete
    partition_stop: Incomplete
    def __init__(
        self,
        *,
        depth,
        sample_indices,
        partition_start,
        partition_stop,
        sum_gradients,
        sum_hessians,
        value=None,
    ) -> None: ...
    children_lower_bound: Incomplete
    children_upper_bound: Incomplete
    def set_children_bounds(self, lower, upper) -> None: ...
    def __lt__(self, other_node): ...

class TreeGrower:
    with_monotonic_cst: Incomplete
    histogram_builder: Incomplete
    splitter: Incomplete
    X_binned: Incomplete
    max_leaf_nodes: Incomplete
    max_depth: Incomplete
    min_samples_leaf: Incomplete
    min_gain_to_split: Incomplete
    n_bins_non_missing: Incomplete
    missing_values_bin_idx: Incomplete
    has_missing_values: Incomplete
    is_categorical: Incomplete
    monotonic_cst: Incomplete
    interaction_cst: Incomplete
    l2_regularization: Incomplete
    shrinkage: Incomplete
    n_features: Incomplete
    n_threads: Incomplete
    splittable_nodes: Incomplete
    finalized_leaves: Incomplete
    total_find_split_time: float
    total_compute_hist_time: float
    total_apply_split_time: float
    n_categorical_splits: int
    n_nodes: int
    def __init__(
        self,
        X_binned,
        gradients,
        hessians,
        max_leaf_nodes=None,
        max_depth=None,
        min_samples_leaf: int = 20,
        min_gain_to_split: float = 0.0,
        min_hessian_to_split: float = 0.001,
        n_bins: int = 256,
        n_bins_non_missing=None,
        has_missing_values: bool = False,
        is_categorical=None,
        monotonic_cst=None,
        interaction_cst=None,
        l2_regularization: float = 0.0,
        feature_fraction_per_split: float = 1.0,
        rng=...,
        shrinkage: float = 1.0,
        n_threads=None,
    ) -> None: ...
    def grow(self) -> None: ...
    def split_next(self): ...
    def make_predictor(self, binning_thresholds): ...
