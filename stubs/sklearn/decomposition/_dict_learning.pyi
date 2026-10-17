from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.linear_model import (
    Lars as Lars,
    Lasso as Lasso,
    LassoLars as LassoLars,
    orthogonal_mp_gram as orthogonal_mp_gram,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    gen_batches as gen_batches,
    gen_even_slices as gen_even_slices,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import (
    row_norms as row_norms,
    svd_flip as svd_flip,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

def sparse_encode(
    X,
    dictionary,
    *,
    gram=None,
    cov=None,
    algorithm: str = "lasso_lars",
    n_nonzero_coefs=None,
    alpha=None,
    copy_cov: bool = True,
    init=None,
    max_iter: int = 1000,
    n_jobs=None,
    check_input: bool = True,
    verbose: int = 0,
    positive: bool = False,
): ...
def dict_learning_online(
    X,
    n_components: int = 2,
    *,
    alpha: int = 1,
    max_iter: int = 100,
    return_code: bool = True,
    dict_init=None,
    callback=None,
    batch_size: int = 256,
    verbose: bool = False,
    shuffle: bool = True,
    n_jobs=None,
    method: str = "lars",
    random_state=None,
    positive_dict: bool = False,
    positive_code: bool = False,
    method_max_iter: int = 1000,
    tol: float = 0.001,
    max_no_improvement: int = 10,
): ...
def dict_learning(
    X,
    n_components,
    *,
    alpha,
    max_iter: int = 100,
    tol: float = 1e-08,
    method: str = "lars",
    n_jobs=None,
    dict_init=None,
    code_init=None,
    callback=None,
    verbose: bool = False,
    random_state=None,
    return_n_iter: bool = False,
    positive_dict: bool = False,
    positive_code: bool = False,
    method_max_iter: int = 1000,
): ...

class _BaseSparseCoding(ClassNamePrefixFeaturesOutMixin, TransformerMixin):
    transform_algorithm: Incomplete
    transform_n_nonzero_coefs: Incomplete
    transform_alpha: Incomplete
    transform_max_iter: Incomplete
    split_sign: Incomplete
    n_jobs: Incomplete
    positive_code: Incomplete
    def __init__(
        self,
        transform_algorithm,
        transform_n_nonzero_coefs,
        transform_alpha,
        split_sign,
        n_jobs,
        positive_code,
        transform_max_iter,
    ) -> None: ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...

class SparseCoder(_BaseSparseCoding, BaseEstimator):
    dictionary: Incomplete
    def __init__(
        self,
        dictionary,
        *,
        transform_algorithm: str = "omp",
        transform_n_nonzero_coefs=None,
        transform_alpha=None,
        split_sign: bool = False,
        n_jobs=None,
        positive_code: bool = False,
        transform_max_iter: int = 1000,
    ) -> None: ...
    n_components_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X, y=None): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

class DictionaryLearning(_BaseSparseCoding, BaseEstimator):
    n_components: Incomplete
    alpha: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    fit_algorithm: Incomplete
    code_init: Incomplete
    dict_init: Incomplete
    callback: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    positive_dict: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        alpha: int = 1,
        max_iter: int = 1000,
        tol: float = 1e-08,
        fit_algorithm: str = "lars",
        transform_algorithm: str = "omp",
        transform_n_nonzero_coefs=None,
        transform_alpha=None,
        n_jobs=None,
        code_init=None,
        dict_init=None,
        callback=None,
        verbose: bool = False,
        split_sign: bool = False,
        random_state=None,
        positive_code: bool = False,
        positive_dict: bool = False,
        transform_max_iter: int = 1000,
    ) -> None: ...
    def fit(self, X, y=None): ...
    components_: Incomplete
    error_: Incomplete
    def fit_transform(self, X, y=None): ...
    def __sklearn_tags__(self): ...

class MiniBatchDictionaryLearning(_BaseSparseCoding, BaseEstimator):
    n_components: Incomplete
    alpha: Incomplete
    max_iter: Incomplete
    fit_algorithm: Incomplete
    dict_init: Incomplete
    verbose: Incomplete
    shuffle: Incomplete
    batch_size: Incomplete
    split_sign: Incomplete
    random_state: Incomplete
    positive_dict: Incomplete
    callback: Incomplete
    max_no_improvement: Incomplete
    tol: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        alpha: int = 1,
        max_iter: int = 1000,
        fit_algorithm: str = "lars",
        n_jobs=None,
        batch_size: int = 256,
        shuffle: bool = True,
        dict_init=None,
        transform_algorithm: str = "omp",
        transform_n_nonzero_coefs=None,
        transform_alpha=None,
        verbose: bool = False,
        split_sign: bool = False,
        random_state=None,
        positive_code: bool = False,
        positive_dict: bool = False,
        transform_max_iter: int = 1000,
        callback=None,
        tol: float = 0.001,
        max_no_improvement: int = 10,
    ) -> None: ...
    n_steps_: Incomplete
    n_iter_: Incomplete
    components_: Incomplete
    def fit(self, X, y=None): ...
    def partial_fit(self, X, y=None): ...
    def __sklearn_tags__(self): ...
