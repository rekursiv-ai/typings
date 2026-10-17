from _typeshed import Incomplete
from sklearn.datasets import get_data_home as get_data_home
from sklearn.datasets._base import (
    RemoteFileMetadata as RemoteFileMetadata,
    load_descr as load_descr,
)
from sklearn.datasets._svmlight_format_io import (
    load_svmlight_files as load_svmlight_files,
)
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)

XY_METADATA: Incomplete
TOPICS_METADATA: Incomplete
logger: Incomplete

def fetch_rcv1(
    *,
    data_home=None,
    subset: str = "all",
    download_if_missing: bool = True,
    random_state=None,
    shuffle: bool = False,
    return_X_y: bool = False,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
