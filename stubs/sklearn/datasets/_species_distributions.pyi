from _typeshed import Incomplete
from sklearn.datasets import get_data_home as get_data_home
from sklearn.datasets._base import RemoteFileMetadata as RemoteFileMetadata
from sklearn.utils import Bunch as Bunch
from sklearn.utils._param_validation import (
    Interval as Interval,
    validate_params as validate_params,
)

SAMPLES: Incomplete
COVERAGES: Incomplete
DATA_ARCHIVE_NAME: str
logger: Incomplete

def construct_grids(batch): ...
def fetch_species_distributions(
    *,
    data_home=None,
    download_if_missing: bool = True,
    n_retries: int = 3,
    delay: float = 1.0,
): ...
