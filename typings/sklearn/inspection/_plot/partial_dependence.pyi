from _typeshed import Incomplete
from sklearn.base import is_regressor as is_regressor
from sklearn.inspection import partial_dependence as partial_dependence
from sklearn.utils import (
    Bunch as Bunch,
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._optional_dependencies import (
    check_matplotlib_support as check_matplotlib_support,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)

class PartialDependenceDisplay:
    pd_results: Incomplete
    features: Incomplete
    feature_names: Incomplete
    target_idx: Incomplete
    deciles: Incomplete
    kind: Incomplete
    subsample: Incomplete
    random_state: Incomplete
    is_categorical: Incomplete
    def __init__(
        self,
        pd_results,
        *,
        features,
        feature_names,
        target_idx,
        deciles,
        kind: str = "average",
        subsample: int = 1000,
        random_state=None,
        is_categorical=None,
    ) -> None: ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        features,
        *,
        sample_weight=None,
        categorical_features=None,
        feature_names=None,
        target=None,
        response_method: str = "auto",
        n_cols: int = 3,
        grid_resolution: int = 100,
        percentiles=(0.05, 0.95),
        custom_values=None,
        method: str = "auto",
        n_jobs=None,
        verbose: int = 0,
        line_kw=None,
        ice_lines_kw=None,
        pd_line_kw=None,
        contour_kw=None,
        ax=None,
        kind: str = "average",
        centered: bool = False,
        subsample: int = 1000,
        random_state=None,
    ): ...
    bounding_ax_: Incomplete
    figure_: Incomplete
    axes_: Incomplete
    lines_: Incomplete
    contours_: Incomplete
    bars_: Incomplete
    heatmaps_: Incomplete
    deciles_vlines_: Incomplete
    deciles_hlines_: Incomplete
    def plot(
        self,
        *,
        ax=None,
        n_cols: int = 3,
        line_kw=None,
        ice_lines_kw=None,
        pd_line_kw=None,
        contour_kw=None,
        bar_kw=None,
        heatmap_kw=None,
        pdp_lim=None,
        centered: bool = False,
    ): ...
