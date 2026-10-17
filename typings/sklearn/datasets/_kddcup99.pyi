from _typeshed import Incomplete
from sklearn.datasets import get_data_home as get_data_home
from sklearn.datasets._base import (
    RemoteFileMetadata as RemoteFileMetadata,
    load_descr as load_descr,
)
from sklearn.utils import (
    Bunch as Bunch,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)

ARCHIVE: Incomplete
ARCHIVE_10_PERCENT: Incomplete
logger: Incomplete

def fetch_kddcup99(
    *,
    subset=None,
    data_home=None,
    shuffle: bool = False,
    random_state=None,
    percent10: bool = True,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    as_frame: bool = False,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
