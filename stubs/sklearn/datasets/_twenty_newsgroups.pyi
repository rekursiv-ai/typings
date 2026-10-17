from _typeshed import Incomplete
from sklearn import preprocessing as preprocessing
from sklearn.datasets import (
    get_data_home as get_data_home,
    load_files as load_files,
)
from sklearn.datasets._base import (
    RemoteFileMetadata as RemoteFileMetadata,
    load_descr as load_descr,
)
from sklearn.feature_extraction.text import CountVectorizer as CountVectorizer
from sklearn.utils import (
    Bunch as Bunch,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.fixes import tarfile_extractall as tarfile_extractall

logger: Incomplete
ARCHIVE: Incomplete
CACHE_NAME: str
TRAIN_FOLDER: str
TEST_FOLDER: str

def strip_newsgroup_header(text): ...
def strip_newsgroup_quoting(text): ...
def strip_newsgroup_footer(text): ...
def fetch_20newsgroups(
    *,
    data_home=None,
    subset: str = "train",
    categories=None,
    shuffle: bool = True,
    random_state: int = 42,
    remove=(),
    download_if_missing: bool = True,
    return_X_y: bool = False,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
def fetch_20newsgroups_vectorized(
    *,
    subset: str = "train",
    remove=(),
    data_home=None,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    normalize: bool = True,
    as_frame: bool = False,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
