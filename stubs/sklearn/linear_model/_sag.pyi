from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import make_dataset as make_dataset
from sklearn.linear_model._sag_fast import (
    sag32 as sag32,
    sag64 as sag64,
)
from sklearn.utils import check_array as check_array
from sklearn.utils.extmath import row_norms as row_norms

def get_auto_step_size(
    max_squared_sum,
    alpha_scaled,
    loss,
    fit_intercept,
    n_samples=None,
    is_saga: bool = False,
): ...
def sag_solver(
    X,
    y,
    sample_weight=None,
    loss: str = "log",
    alpha: float = 1.0,
    beta: float = 0.0,
    max_iter: int = 1000,
    tol: float = 0.001,
    verbose: int = 0,
    random_state=None,
    check_input: bool = True,
    max_squared_sum=None,
    warm_start_mem=None,
    is_saga: bool = False,
): ...
