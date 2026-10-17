from _typeshed import Incomplete
from numpy import (
    ComplexWarning as ComplexWarning,
    VisibleDeprecationWarning as VisibleDeprecationWarning,
)
from scipy.sparse import sparray as sparray
from scipy.sparse.csgraph import laplacian as laplacian

np_version: Incomplete
np_base_version: Incomplete
sp_version: Incomplete
sp_base_version: Incomplete
CSR_CONTAINERS: Incomplete
CSC_CONTAINERS: Incomplete
COO_CONTAINERS: Incomplete
LIL_CONTAINERS: Incomplete
DOK_CONTAINERS: Incomplete
BSR_CONTAINERS: Incomplete
DIA_CONTAINERS: Incomplete
SPARRAY_PRESENT: bool

def pd_fillna(pd, frame): ...
def tarfile_extractall(tarfile, path) -> None: ...

PYARROW_VERSION_BELOW_17: bool
pyarrow_version: Incomplete
