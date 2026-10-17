from _typeshed import Incomplete
from sklearn.utils.extmath import (
    safe_sparse_dot as safe_sparse_dot,
    squared_norm as squared_norm,
)

def sandwich_dot(X, W): ...

class LinearModelLoss:
    base_loss: Incomplete
    fit_intercept: Incomplete
    def __init__(self, base_loss, fit_intercept) -> None: ...
    def init_zero_coef(self, X, dtype=None): ...
    def weight_intercept(self, coef): ...
    def weight_intercept_raw(self, coef, X): ...
    def l2_penalty(self, weights, l2_reg_strength): ...
    def loss(
        self,
        coef,
        X,
        y,
        sample_weight=None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
        raw_prediction=None,
    ): ...
    def loss_gradient(
        self,
        coef,
        X,
        y,
        sample_weight=None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
        raw_prediction=None,
    ): ...
    def gradient(
        self,
        coef,
        X,
        y,
        sample_weight=None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
        raw_prediction=None,
    ): ...
    def gradient_hessian(
        self,
        coef,
        X,
        y,
        sample_weight=None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
        gradient_out=None,
        hessian_out=None,
        raw_prediction=None,
    ): ...
    def gradient_hessian_product(
        self,
        coef,
        X,
        y,
        sample_weight=None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
    ): ...
