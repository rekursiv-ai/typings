from _typeshed import Incomplete
from sklearn.datasets._base import (
    RemoteFileMetadata as RemoteFileMetadata,
    get_data_home as get_data_home,
    load_descr as load_descr,
)
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.fixes import tarfile_extractall as tarfile_extractall

logger: Incomplete
ARCHIVE: Incomplete
FUNNELED_ARCHIVE: Incomplete
TARGETS: Incomplete

def fetch_lfw_people(
    *,
    data_home=None,
    funneled: bool = True,
    resize: float = 0.5,
    min_faces_per_person: int = 0,
    color: bool = False,
    slice_=...,
    download_if_missing: bool = True,
    return_X_y: bool = False,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
def fetch_lfw_pairs(
    *,
    subset: str = "train",
    data_home=None,
    funneled: bool = True,
    resize: float = 0.5,
    color: bool = False,
    slice_=...,
    download_if_missing: bool = True,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
