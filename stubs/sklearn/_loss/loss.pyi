from _typeshed import Incomplete
from sklearn._loss._loss import (
    CyAbsoluteError as CyAbsoluteError,
    CyExponentialLoss as CyExponentialLoss,
    CyHalfBinomialLoss as CyHalfBinomialLoss,
    CyHalfGammaLoss as CyHalfGammaLoss,
    CyHalfMultinomialLoss as CyHalfMultinomialLoss,
    CyHalfPoissonLoss as CyHalfPoissonLoss,
    CyHalfSquaredError as CyHalfSquaredError,
    CyHalfTweedieLoss as CyHalfTweedieLoss,
    CyHalfTweedieLossIdentity as CyHalfTweedieLossIdentity,
    CyHuberLoss as CyHuberLoss,
    CyPinballLoss as CyPinballLoss,
)
from sklearn._loss.link import (
    HalfLogitLink as HalfLogitLink,
    IdentityLink as IdentityLink,
    Interval as Interval,
    LogitLink as LogitLink,
    LogLink as LogLink,
    MultinomialLogit as MultinomialLogit,
)
from sklearn.utils import check_scalar as check_scalar

class BaseLoss:
    differentiable: bool
    need_update_leaves_values: bool
    is_multiclass: bool
    closs: Incomplete
    link: Incomplete
    approx_hessian: bool
    constant_hessian: bool
    n_classes: Incomplete
    interval_y_true: Incomplete
    interval_y_pred: Incomplete
    def __init__(self, closs, link, n_classes=None) -> None: ...
    def in_y_true_range(self, y): ...
    def in_y_pred_range(self, y): ...
    def loss(
        self,
        y_true,
        raw_prediction,
        sample_weight=None,
        loss_out=None,
        n_threads: int = 1,
    ): ...
    def loss_gradient(
        self,
        y_true,
        raw_prediction,
        sample_weight=None,
        loss_out=None,
        gradient_out=None,
        n_threads: int = 1,
    ): ...
    def gradient(
        self,
        y_true,
        raw_prediction,
        sample_weight=None,
        gradient_out=None,
        n_threads: int = 1,
    ): ...
    def gradient_hessian(
        self,
        y_true,
        raw_prediction,
        sample_weight=None,
        gradient_out=None,
        hessian_out=None,
        n_threads: int = 1,
    ): ...
    def __call__(
        self,
        y_true,
        raw_prediction,
        sample_weight=None,
        n_threads: int = 1,
    ): ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...
    def init_gradient_and_hessian(self, n_samples, dtype=..., order: str = "F"): ...

class HalfSquaredError(BaseLoss):
    constant_hessian: Incomplete
    def __init__(self, sample_weight=None) -> None: ...

class AbsoluteError(BaseLoss):
    differentiable: bool
    need_update_leaves_values: bool
    approx_hessian: bool
    constant_hessian: Incomplete
    def __init__(self, sample_weight=None) -> None: ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...

class PinballLoss(BaseLoss):
    differentiable: bool
    need_update_leaves_values: bool
    approx_hessian: bool
    constant_hessian: Incomplete
    def __init__(self, sample_weight=None, quantile: float = 0.5) -> None: ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...

class HuberLoss(BaseLoss):
    differentiable: bool
    need_update_leaves_values: bool
    quantile: Incomplete
    approx_hessian: bool
    constant_hessian: bool
    def __init__(
        self,
        sample_weight=None,
        quantile: float = 0.9,
        delta: float = 0.5,
    ) -> None: ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...

class HalfPoissonLoss(BaseLoss):
    interval_y_true: Incomplete
    def __init__(self, sample_weight=None) -> None: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...

class HalfGammaLoss(BaseLoss):
    interval_y_true: Incomplete
    def __init__(self, sample_weight=None) -> None: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...

class HalfTweedieLoss(BaseLoss):
    interval_y_true: Incomplete
    def __init__(self, sample_weight=None, power: float = 1.5) -> None: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...

class HalfTweedieLossIdentity(BaseLoss):
    interval_y_true: Incomplete
    interval_y_pred: Incomplete
    def __init__(self, sample_weight=None, power: float = 1.5) -> None: ...

class HalfBinomialLoss(BaseLoss):
    interval_y_true: Incomplete
    def __init__(self, sample_weight=None) -> None: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...
    def predict_proba(self, raw_prediction): ...

class HalfMultinomialLoss(BaseLoss):
    is_multiclass: bool
    interval_y_true: Incomplete
    interval_y_pred: Incomplete
    def __init__(self, sample_weight=None, n_classes: int = 3) -> None: ...
    def in_y_true_range(self, y): ...
    def fit_intercept_only(self, y_true, sample_weight=None): ...
    def predict_proba(self, raw_prediction): ...
    def gradient_proba(
        self,
        y_true,
        raw_prediction,
        sample_weight=None,
        gradient_out=None,
        proba_out=None,
        n_threads: int = 1,
    ): ...

class ExponentialLoss(BaseLoss):
    interval_y_true: Incomplete
    def __init__(self, sample_weight=None) -> None: ...
    def constant_to_optimal_zero(self, y_true, sample_weight=None): ...
    def predict_proba(self, raw_prediction): ...
