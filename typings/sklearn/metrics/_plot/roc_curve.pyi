from _typeshed import Incomplete
from sklearn.metrics._ranking import (
    auc as auc,
    roc_curve as roc_curve,
)
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin

class RocCurveDisplay(_BinaryClassifierCurveDisplayMixin):
    fpr: Incomplete
    tpr: Incomplete
    roc_auc: Incomplete
    name: Incomplete
    pos_label: Incomplete
    def __init__(
        self,
        *,
        fpr,
        tpr,
        roc_auc=None,
        name=None,
        pos_label=None,
        estimator_name: str = "deprecated",
    ) -> None: ...
    line_: Incomplete
    chance_level_: Incomplete
    def plot(
        self,
        ax=None,
        *,
        name=None,
        curve_kwargs=None,
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
        drop_intermediate: bool = True,
        response_method: str = "auto",
        pos_label=None,
        name=None,
        ax=None,
        curve_kwargs=None,
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
        drop_intermediate: bool = True,
        pos_label=None,
        name=None,
        ax=None,
        curve_kwargs=None,
        plot_chance_level: bool = False,
        chance_level_kw=None,
        despine: bool = False,
        y_pred: str = "deprecated",
        **kwargs,
    ): ...
    @classmethod
    def from_cv_results(
        cls,
        cv_results,
        X,
        y,
        *,
        sample_weight=None,
        drop_intermediate: bool = True,
        response_method: str = "auto",
        pos_label=None,
        ax=None,
        name=None,
        curve_kwargs=None,
        plot_chance_level: bool = False,
        chance_level_kwargs=None,
        despine: bool = False,
    ): ...
