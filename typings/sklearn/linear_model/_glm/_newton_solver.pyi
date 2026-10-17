from abc import ABC, abstractmethod

import abc

from _typeshed import Incomplete
from sklearn._loss.loss import HalfSquaredError as HalfSquaredError
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._linear_loss import LinearModelLoss as LinearModelLoss

class NewtonSolver(ABC, metaclass=abc.ABCMeta):
    coef: Incomplete
    linear_loss: Incomplete
    l2_reg_strength: Incomplete
    tol: Incomplete
    max_iter: Incomplete
    n_threads: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        coef,
        linear_loss=...,
        l2_reg_strength: float = 0.0,
        tol: float = 0.0001,
        max_iter: int = 100,
        n_threads: int = 1,
        verbose: int = 0,
    ) -> None: ...
    loss_value: Incomplete
    def setup(self, X, y, sample_weight) -> None: ...
    @abstractmethod
    def update_gradient_hessian(self, X, y, sample_weight): ...
    @abstractmethod
    def inner_solve(self, X, y, sample_weight): ...
    converged: Incomplete
    def fallback_lbfgs_solve(self, X, y, sample_weight) -> None: ...
    coef_old: Incomplete
    loss_value_old: Incomplete
    gradient_old: Incomplete
    use_fallback_lbfgs_solve: bool
    raw_prediction: Incomplete
    def line_search(self, X, y, sample_weight) -> None: ...
    def check_convergence(self, X, y, sample_weight) -> None: ...
    def finalize(self, X, y, sample_weight) -> None: ...
    iteration: int
    def solve(self, X, y, sample_weight): ...

class NewtonCholeskySolver(NewtonSolver):
    coef: Incomplete
    gradient: Incomplete
    hessian: Incomplete
    is_multinomial_with_intercept: Incomplete
    is_multinomial_no_penalty: Incomplete
    def setup(self, X, y, sample_weight) -> None: ...
    def update_gradient_hessian(self, X, y, sample_weight) -> None: ...
    use_fallback_lbfgs_solve: bool
    coef_newton: Incomplete
    gradient_times_newton: Incomplete
    def inner_solve(self, X, y, sample_weight) -> None: ...
    def finalize(self, X, y, sample_weight) -> None: ...
