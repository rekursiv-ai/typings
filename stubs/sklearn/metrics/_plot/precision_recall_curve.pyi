from _typeshed import Incomplete
from sklearn.metrics._ranking import (
    average_precision_score as average_precision_score,
    precision_recall_curve as precision_recall_curve,
)
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin

class PrecisionRecallDisplay(_BinaryClassifierCurveDisplayMixin):
    name: Incomplete
    precision: Incomplete
    recall: Incomplete
    average_precision: Incomplete
    pos_label: Incomplete
    prevalence_pos_label: Incomplete
    def __init__(
        self,
        precision,
        recall,
        *,
        average_precision=None,
        name=None,
        pos_label=None,
        prevalence_pos_label=None,
        estimator_name: str = "deprecated",
    ) -> None: ...
    chance_level_: Incomplete
    def plot(
        self,
        ax=None,
        *,
        name=None,
        plot_chance_level: bool = False,
        chance_level_kw=None,
        despine: bool = False,
        **kwargs,
    ): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        y,
        *,
        sample_weight=None,
        drop_intermediate: bool = False,
        response_method: str = "auto",
        pos_label=None,
        name=None,
        ax=None,
        plot_chance_level: bool = False,
        chance_level_kw=None,
        despine: bool = False,
        **kwargs,
    ): ...
    @classmethod
    def from_predictions(
        cls,
        y_true,
        y_score=None,
        *,
        sample_weight=None,
        drop_intermediate: bool = False,
        pos_label=None,
        name=None,
        ax=None,
        plot_chance_level: bool = False,
        chance_level_kw=None,
        despine: bool = False,
        y_pred: str = "deprecated",
        **kwargs,
    ): ...
