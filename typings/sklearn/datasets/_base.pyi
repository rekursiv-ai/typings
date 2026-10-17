from typing import NamedTuple

from _typeshed import Incomplete
from sklearn.preprocessing import scale as scale
from sklearn.utils import (
    Bunch as Bunch,
    check_random_state as check_random_state,
)
from sklearn.utils._optional_dependencies import (
    check_pandas_support as check_pandas_support,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)

DATA_MODULE: str
DESCR_MODULE: str
IMAGES_MODULE: str

class RemoteFileMetadata(NamedTuple):
    filename: Incomplete
    url: Incomplete
    checksum: Incomplete

def get_data_home(data_home=None) -> str: ...
def clear_data_home(data_home=None) -> None: ...
def load_files(
    container_path,
    *,
    description=None,
    categories=None,
    load_content: bool = True,
    shuffle: bool = True,
    encoding=None,
    decode_error: str = "strict",
    random_state: int = 0,
    allowed_extensions=None,
): ...
def load_csv_data(
    data_file_name,
    *,
    data_module=...,
    descr_file_name=None,
    descr_module=...,
    encoding: str = "utf-8",
): ...
def load_gzip_compressed_csv_data(
    data_file_name,
    *,
    data_module=...,
    descr_file_name=None,
    descr_module=...,
    encoding: str = "utf-8",
    **kwargs,
): ...
def load_descr(descr_file_name, *, descr_module=..., encoding: str = "utf-8"): ...
def load_wine(*, return_X_y: bool = False, as_frame: bool = False): ...
def load_iris(*, return_X_y: bool = False, as_frame: bool = False): ...
def load_breast_cancer(*, return_X_y: bool = False, as_frame: bool = False): ...
def load_digits(
    *,
    n_class: int = 10,
    return_X_y: bool = False,
    as_frame: bool = False,
): ...
def load_diabetes(
    *,
    return_X_y: bool = False,
    as_frame: bool = False,
    scaled: bool = True,
): ...
def load_linnerud(*, return_X_y: bool = False, as_frame: bool = False): ...
def load_sample_images(): ...
def load_sample_image(image_name): ...
def fetch_file(
    url,
    folder=None,
    local_filename=None,
    sha256=None,
    n_retries: int = 3,
    delay: int = 1,
): ...
