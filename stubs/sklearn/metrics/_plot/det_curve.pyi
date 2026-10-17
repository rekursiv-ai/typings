from _typeshed import Incomplete
from sklearn.metrics._ranking import det_curve as det_curve
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin

class DetCurveDisplay(_BinaryClassifierCurveDisplayMixin):
    fpr: Incomplete
    fnr: Incomplete
    estimator_name: Incomplete
    pos_label: Incomplete
    def __init__(self, *, fpr, fnr, estimator_name=None, pos_label=None) -> None: ...
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
        y_pred: str = "deprecated",
        **kwargs,
    ): ...
    def plot(self, ax=None, *, name=None, **kwargs): ...
