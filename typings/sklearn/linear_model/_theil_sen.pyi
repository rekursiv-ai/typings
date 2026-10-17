from _typeshed import Incomplete
from sklearn.base import RegressorMixin as RegressorMixin
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model._base import LinearModel as LinearModel
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import validate_data as validate_data

class TheilSenRegressor(RegressorMixin, LinearModel):
    fit_intercept: Incomplete
    max_subpopulation: Incomplete
    n_subsamples: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    random_state: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        max_subpopulation: float = 10000.0,
        n_subsamples=None,
        max_iter: int = 300,
        tol: float = 0.001,
        random_state=None,
        n_jobs=None,
        verbose: bool = False,
    ) -> None: ...
    breakdown_: Incomplete
    intercept_: Incomplete
    coef_: Incomplete
    def fit(self, X, y): ...
