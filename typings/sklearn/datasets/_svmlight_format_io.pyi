from sklearn import __version__ as __version__
from sklearn.utils import check_array as check_array
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)

def load_svmlight_file(
    f,
    *,
    n_features=None,
    dtype=...,
    multilabel: bool = False,
    zero_based: str = "auto",
    query_id: bool = False,
    offset: int = 0,
    length: int = -1,
): ...
def load_svmlight_files(
    files,
    *,
    n_features=None,
    dtype=...,
    multilabel: bool = False,
    zero_based: str = "auto",
    query_id: bool = False,
    offset: int = 0,
    length: int = -1,
): ...
def dump_svmlight_file(
    X,
    y,
    f,
    *,
    zero_based: bool = True,
    comment=None,
    query_id=None,
    multilabel: bool = False,
) -> None: ...
