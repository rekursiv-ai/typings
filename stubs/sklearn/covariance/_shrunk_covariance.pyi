from _typeshed import Incomplete
from sklearn.covariance import (
    EmpiricalCovariance as EmpiricalCovariance,
    empirical_covariance as empirical_covariance,
)
from sklearn.utils import check_array as check_array
from sklearn.utils._param_validation import (
    Interval as Interval,
    validate_params as validate_params,
)
from sklearn.utils.validation import validate_data as validate_data

def shrunk_covariance(emp_cov, shrinkage: float = 0.1): ...

class ShrunkCovariance(EmpiricalCovariance):
    shrinkage: Incomplete
    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        shrinkage: float = 0.1,
    ) -> None: ...
    location_: Incomplete
    def fit(self, X, y=None): ...

def ledoit_wolf_shrinkage(X, assume_centered: bool = False, block_size: int = 1000): ...
def ledoit_wolf(X, *, assume_centered: bool = False, block_size: int = 1000): ...

class LedoitWolf(EmpiricalCovariance):
    block_size: Incomplete
    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
        block_size: int = 1000,
    ) -> None: ...
    location_: Incomplete
    shrinkage_: Incomplete
    def fit(self, X, y=None): ...

def oas(X, *, assume_centered: bool = False): ...

class OAS(EmpiricalCovariance):
    location_: Incomplete
    shrinkage_: Incomplete
    def fit(self, X, y=None): ...
