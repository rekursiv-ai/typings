from _typeshed import Incomplete
from sklearn.base import is_classifier as is_classifier
from sklearn.metrics import confusion_matrix as confusion_matrix
from sklearn.utils._optional_dependencies import (
    check_matplotlib_support as check_matplotlib_support,
)
from sklearn.utils.multiclass import unique_labels as unique_labels

class ConfusionMatrixDisplay:
    confusion_matrix: Incomplete
    display_labels: Incomplete
    def __init__(self, confusion_matrix, *, display_labels=None) -> None: ...
    im_: Incomplete
    text_: Incomplete
    figure_: Incomplete
    ax_: Incomplete
    def plot(
        self,
        *,
        include_values: bool = True,
        cmap: str = "viridis",
        xticks_rotation: str = "horizontal",
        values_format=None,
        ax=None,
        colorbar: bool = True,
        im_kw=None,
        text_kw=None,
    ): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        y,
        *,
        labels=None,
        sample_weight=None,
        normalize=None,
        display_labels=None,
        include_values: bool = True,
        xticks_rotation: str = "horizontal",
        values_format=None,
        cmap: str = "viridis",
        ax=None,
        colorbar: bool = True,
        im_kw=None,
        text_kw=None,
    ): ...
    @classmethod
    def from_predictions(
        cls,
        y_true,
        y_pred,
        *,
        labels=None,
        sample_weight=None,
        normalize=None,
        display_labels=None,
        include_values: bool = True,
        xticks_rotation: str = "horizontal",
        values_format=None,
        cmap: str = "viridis",
        ax=None,
        colorbar: bool = True,
        im_kw=None,
        text_kw=None,
    ): ...
