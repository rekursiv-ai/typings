from _typeshed import Incomplete
from sklearn.base import (
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.linear_model._base import LinearModel as LinearModel
from sklearn.model_selection import check_cv as check_cv
from sklearn.utils import (
    Bunch as Bunch,
    as_float_array as as_float_array,
    check_array as check_array,
)
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
    FLOAT_DTYPES as FLOAT_DTYPES,
    validate_data as validate_data,
)

premature: str

def orthogonal_mp(
    X,
    y,
    *,
    n_nonzero_coefs=None,
    tol=None,
    precompute: bool = False,
    copy_X: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
): ...
def orthogonal_mp_gram(
    Gram,
    Xy,
    *,
    n_nonzero_coefs=None,
    tol=None,
    norms_squared=None,
    copy_Gram: bool = True,
    copy_Xy: bool = True,
    return_path: bool = False,
    return_n_iter: bool = False,
): ...

class OrthogonalMatchingPursuit(MultiOutputMixin, RegressorMixin, LinearModel):
    n_nonzero_coefs: Incomplete
    tol: Incomplete
    fit_intercept: Incomplete
    precompute: Incomplete
    def __init__(
        self,
        *,
        n_nonzero_coefs=None,
        tol=None,
        fit_intercept: bool = True,
        precompute: str = "auto",
    ) -> None: ...
    n_nonzero_coefs_: Incomplete
    coef_: Incomplete
    def fit(self, X, y): ...

class OrthogonalMatchingPursuitCV(RegressorMixin, LinearModel):
    copy: Incomplete
    fit_intercept: Incomplete
    max_iter: Incomplete
    cv: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    def __init__(
        self,
        *,
        copy: bool = True,
        fit_intercept: bool = True,
        max_iter=None,
        cv=None,
        n_jobs=None,
        verbose: bool = False,
    ) -> None: ...
    n_nonzero_coefs_: Incomplete
    coef_: Incomplete
    intercept_: Incomplete
    n_iter_: Incomplete
    def fit(self, X, y, **fit_params): ...
    def get_metadata_routing(self): ...
