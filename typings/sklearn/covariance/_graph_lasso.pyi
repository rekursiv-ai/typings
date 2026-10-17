from _typeshed import Incomplete
from sklearn.covariance import (
    EmpiricalCovariance as EmpiricalCovariance,
    empirical_covariance as empirical_covariance,
    log_likelihood as log_likelihood,
)
from sklearn.exceptions import ConvergenceWarning as ConvergenceWarning
from sklearn.linear_model import lars_path_gram as lars_path_gram
from sklearn.model_selection import (
    check_cv as check_cv,
    cross_val_score as cross_val_score,
)
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.metadata_routing import (
    MetadataRouter as MetadataRouter,
    MethodMapping as MethodMapping,
    process_routing as process_routing,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_random_state as check_random_state,
    check_scalar as check_scalar,
    validate_data as validate_data,
)

def alpha_max(emp_cov): ...
def graphical_lasso(
    emp_cov,
    alpha,
    *,
    mode: str = "cd",
    tol: float = 0.0001,
    enet_tol: float = 0.0001,
    max_iter: int = 100,
    verbose: bool = False,
    return_costs: bool = False,
    eps=...,
    return_n_iter: bool = False,
): ...

class BaseGraphicalLasso(EmpiricalCovariance):
    tol: Incomplete
    enet_tol: Incomplete
    max_iter: Incomplete
    mode: Incomplete
    verbose: Incomplete
    eps: Incomplete
    def __init__(
        self,
        tol: float = 0.0001,
        enet_tol: float = 0.0001,
        max_iter: int = 100,
        mode: str = "cd",
        verbose: bool = False,
        eps=...,
        assume_centered: bool = False,
    ) -> None: ...

class GraphicalLasso(BaseGraphicalLasso):
    alpha: Incomplete
    covariance: Incomplete
    def __init__(
        self,
        alpha: float = 0.01,
        *,
        mode: str = "cd",
        covariance=None,
        tol: float = 0.0001,
        enet_tol: float = 0.0001,
        max_iter: int = 100,
        verbose: bool = False,
        eps=...,
        assume_centered: bool = False,
    ) -> None: ...
    location_: Incomplete
    def fit(self, X, y=None): ...

def graphical_lasso_path(
    X,
    alphas,
    cov_init=None,
    X_test=None,
    mode: str = "cd",
    tol: float = 0.0001,
    enet_tol: float = 0.0001,
    max_iter: int = 100,
    verbose: bool = False,
    eps=...,
): ...

class GraphicalLassoCV(BaseGraphicalLasso):
    alphas: Incomplete
    n_refinements: Incomplete
    cv: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        *,
        alphas: int = 4,
        n_refinements: int = 4,
        cv=None,
        tol: float = 0.0001,
        enet_tol: float = 0.0001,
        max_iter: int = 100,
        mode: str = "cd",
        n_jobs=None,
        verbose: bool = False,
        eps=...,
        assume_centered: bool = False,
    ) -> None: ...
    location_: Incomplete
    cv_results_: Incomplete
    alpha_: Incomplete
    def fit(self, X, y=None, **params): ...
    def get_metadata_routing(self): ...
