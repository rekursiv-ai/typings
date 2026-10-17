from _typeshed import Incomplete
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._optional_dependencies import (
    check_matplotlib_support as check_matplotlib_support,
)

class PredictionErrorDisplay:
    y_true: Incomplete
    y_pred: Incomplete
    def __init__(self, *, y_true, y_pred) -> None: ...
    line_: Incomplete
    scatter_: Incomplete
    ax_: Incomplete
    figure_: Incomplete
    def plot(
        self,
        ax=None,
        *,
        kind: str = "residual_vs_predicted",
        scatter_kwargs=None,
        line_kwargs=None,
    ): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        y,
        *,
        kind: str = "residual_vs_predicted",
        subsample: int = 1000,
        random_state=None,
        ax=None,
        scatter_kwargs=None,
        line_kwargs=None,
    ): ...
    @classmethod
    def from_predictions(
        cls,
        y_true,
        y_pred,
        *,
        kind: str = "residual_vs_predicted",
        subsample: int = 1000,
        random_state=None,
        ax=None,
        scatter_kwargs=None,
        line_kwargs=None,
    ): ...
