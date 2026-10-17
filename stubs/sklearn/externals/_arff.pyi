from collections.abc import Generator, Iterator
from typing_extensions import TypedDict

from _typeshed import Incomplete

__author_email__: str
__version__: str
type ArffDenseDataType = Iterator[list]
type ArffSparseDataType = tuple[list, ...]

class ArffContainerType(TypedDict):
    description: str
    relation: str
    attributes: list
    data: ArffDenseDataType | ArffSparseDataType

DENSE: int
COO: int
LOD: int
DENSE_GEN: int
LOD_GEN: int

class ArffException(Exception):
    message: str | None
    line: int
    def __init__(self) -> None: ...

class BadRelationFormat(ArffException):
    message: str

class BadAttributeFormat(ArffException):
    message: str

class BadDataFormat(ArffException):
    message: Incomplete
    def __init__(self, value) -> None: ...

class BadAttributeType(ArffException):
    message: str

class BadAttributeName(ArffException):
    message: Incomplete
    def __init__(self, value, value2) -> None: ...

class BadNominalValue(ArffException):
    message: Incomplete
    def __init__(self, value) -> None: ...

class BadNominalFormatting(ArffException):
    message: Incomplete
    def __init__(self, value) -> None: ...

class BadNumericalValue(ArffException):
    message: str

class BadStringValue(ArffException):
    message: str

class BadLayout(ArffException):
    message: str
    def __init__(self, msg: str = "") -> None: ...

class BadObject(ArffException):
    msg: Incomplete
    def __init__(self, msg: str = "Invalid object.") -> None: ...

def encode_string(s): ...

class EncodedNominalConversor:
    values: Incomplete
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class NominalConversor:
    values: Incomplete
    zero_value: Incomplete
    def __init__(self, values) -> None: ...
    def __call__(self, value): ...

class DenseGeneratorData:
    def decode_rows(self, stream, conversors) -> Generator[Incomplete]: ...
    def encode_data(self, data, attributes) -> Generator[Incomplete]: ...

class _DataListMixin:
    def decode_rows(self, stream, conversors): ...

class Data(_DataListMixin, DenseGeneratorData): ...

class COOData:
    def decode_rows(self, stream, conversors): ...
    def encode_data(self, data, attributes) -> Generator[Incomplete]: ...

class LODGeneratorData:
    def decode_rows(self, stream, conversors) -> Generator[Incomplete]: ...
    def encode_data(self, data, attributes) -> Generator[Incomplete]: ...

class LODData(_DataListMixin, LODGeneratorData): ...

class ArffDecoder:
    def __init__(self) -> None: ...
    def decode(self, s, encode_nominal: bool = False, return_type=...): ...

class ArffEncoder:
    def encode(self, obj): ...
    def iter_encode(self, obj) -> Generator[Incomplete, Incomplete]: ...

def load(fp, encode_nominal: bool = False, return_type=...): ...
def loads(s, encode_nominal: bool = False, return_type=...): ...
def dump(obj, fp): ...
def dumps(obj): ...
