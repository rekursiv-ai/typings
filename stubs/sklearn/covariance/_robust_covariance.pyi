from _typeshed import Incomplete
from sklearn.covariance._empirical_covariance import (
    EmpiricalCovariance as EmpiricalCovariance,
    empirical_covariance as empirical_covariance,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import fast_logdet as fast_logdet
from sklearn.utils.validation import validate_data as validate_data

def c_step(
    X,
    n_support,
    remaining_iterations: int = 30,
    initial_estimates=None,
    verbose: bool = False,
    cov_computation_method=...,
    random_state=None,
): ...
def select_candidates(
    X,
    n_support,
    n_trials,
    select: int = 1,
    n_iter: int = 30,
    verbose: bool = False,
    cov_computation_method=...,
    random_state=None,
): ...
def fast_mcd(
    X,
    support_fraction=None,
    cov_computation_method=...,
    random_state=None,
): ...

class MinCovDet(EmpiricalCovariance):
    store_precision: Incomplete
    assume_centered: Incomplete
    support_fraction: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        support_fraction=None,
        random_state=None,
    ) -> None: ...
    raw_location_: Incomplete
    raw_covariance_: Incomplete
    raw_support_: Incomplete
    location_: Incomplete
    support_: Incomplete
    dist_: Incomplete
    def fit(self, X, y=None): ...
    def correct_covariance(self, data): ...
    def reweight_covariance(self, data): ...
