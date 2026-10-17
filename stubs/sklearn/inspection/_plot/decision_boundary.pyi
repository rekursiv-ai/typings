from _typeshed import Incomplete
from sklearn.base import is_regressor as is_regressor
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils._dataframe import (
    is_pandas_df as is_pandas_df,
    is_polars_df as is_polars_df,
)
from sklearn.utils._optional_dependencies import (
    check_matplotlib_support as check_matplotlib_support,
)
from sklearn.utils.validation import check_is_fitted as check_is_fitted

class DecisionBoundaryDisplay:
    xx0: Incomplete
    xx1: Incomplete
    response: Incomplete
    multiclass_colors: Incomplete
    xlabel: Incomplete
    ylabel: Incomplete
    def __init__(
        self,
        *,
        xx0,
        xx1,
        response,
        multiclass_colors=None,
        xlabel=None,
        ylabel=None,
    ) -> None: ...
    surface_: Incomplete
    multiclass_colors_: Incomplete
    ax_: Incomplete
    figure_: Incomplete
    def plot(
        self,
        plot_method: str = "contourf",
        ax=None,
        xlabel=None,
        ylabel=None,
        **kwargs,
    ): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        *,
        grid_resolution: int = 100,
        eps: float = 1.0,
        plot_method: str = "contourf",
        response_method: str = "auto",
        class_of_interest=None,
        multiclass_colors=None,
        xlabel=None,
        ylabel=None,
        ax=None,
        **kwargs,
    ): ...
