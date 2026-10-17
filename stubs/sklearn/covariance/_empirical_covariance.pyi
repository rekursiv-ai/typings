from _typeshed import Incomplete
from sklearn import config_context as config_context
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.metrics.pairwise import pairwise_distances as pairwise_distances
from sklearn.utils import (
    check_array as check_array,
    metadata_routing as metadata_routing,
)
from sklearn.utils._param_validation import validate_params as validate_params
from sklearn.utils.extmath import fast_logdet as fast_logdet
from sklearn.utils.validation import validate_data as validate_data

def log_likelihood(emp_cov, precision): ...
def empirical_covariance(X, *, assume_centered: bool = False): ...

class EmpiricalCovariance(BaseEstimator):
    store_precision: Incomplete
    assume_centered: Incomplete
    def __init__(
        self,
        *,
        store_precision: bool = True,
        assume_centered: bool = False,
    ) -> None: ...
    def get_precision(self): ...
    location_: Incomplete
    def fit(self, X, y=None): ...
    def score(self, X_test, y=None): ...
    def error_norm(
        self,
        comp_cov,
        norm: str = "frobenius",
        scaling: bool = True,
        squared: bool = True,
    ): ...
    def mahalanobis(self, X): ...
