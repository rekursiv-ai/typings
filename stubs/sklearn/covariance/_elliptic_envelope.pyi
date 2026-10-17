from _typeshed import Incomplete
from sklearn.base import OutlierMixin as OutlierMixin
from sklearn.covariance._robust_covariance import MinCovDet as MinCovDet
from sklearn.metrics import accuracy_score as accuracy_score
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.validation import check_is_fitted as check_is_fitted

class EllipticEnvelope(OutlierMixin, MinCovDet):
    contamination: Incomplete
    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction=None,
        contamination: float = 0.1,
        random_state=None,
    ) -> None: ...
    offset_: Incomplete
    def fit(self, X, y=None): ...
    def decision_function(self, X): ...
    def score_samples(self, X): ...
    def predict(self, X): ...
    def score(self, X, y, sample_weight=None): ...
