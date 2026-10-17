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
    validate_params as validate_params,
)

FACES: Incomplete

def fetch_olivetti_faces(
    *,
    data_home=None,
    shuffle: bool = False,
    random_state: int = 0,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
