from collections.abc import Mapping
from types import ModuleType as Namespace
from typing import Protocol, TypeAlias, TypedDict

from _typeshed import Incomplete

__all__ = [
    "Array",
    "Capabilities",
    "DType",
    "DTypeKind",
    "DTypesAll",
    "DTypesAny",
    "DTypesBool",
    "DTypesComplex",
    "DTypesIntegral",
    "DTypesNumeric",
    "DTypesReal",
    "DTypesSigned",
    "DTypesUnsigned",
    "DefaultDTypes",
    "Device",
    "HasShape",
    "JustComplex",
    "JustFloat",
    "JustInt",
    "Namespace",
    "NestedSequence",
    "SupportsArrayNamespace",
    "SupportsBufferProtocol",
]

type SupportsBufferProtocol = Incomplete
type Array = Incomplete
type Device = Incomplete
type DType = Incomplete

class JustInt(Protocol):
    @property
    def __class__(self, /) -> type[int]: ...
    @__class__.setter
    def __class__(self, value: type[int], /) -> None: ...

class JustFloat(Protocol):
    @property
    def __class__(self, /) -> type[float]: ...
    @__class__.setter
    def __class__(self, value: type[float], /) -> None: ...

class JustComplex(Protocol):
    @property
    def __class__(self, /) -> type[complex]: ...
    @__class__.setter
    def __class__(self, value: type[complex], /) -> None: ...

class NestedSequence(Protocol[_T_co]):
    def __getitem__(self, key: int) -> _T_co | NestedSequence[_T_co]: ...
    def __len__(self) -> int: ...

class SupportsArrayNamespace(Protocol[_T_co]):
    def __array_namespace__(self, /, *, api_version: str | None) -> _T_co: ...

class HasShape(Protocol[_T_co]):
    @property
    def shape(self, /) -> _T_co: ...

Capabilities = TypedDict(
    "Capabilities",
    {"boolean indexing": bool, "data-dependent shapes": bool, "max dimensions": int},
)
DefaultDTypes = TypedDict(
    "DefaultDTypes",
    {
        "real floating": DType,
        "complex floating": DType,
        "integral": DType,
        "indexing": DType,
    },
)
DTypeKind: TypeAlias

class DTypesBool(TypedDict):
    bool: DType

class DTypesSigned(TypedDict):
    int8: DType
    int16: DType
    int32: DType
    int64: DType

class DTypesUnsigned(TypedDict):
    uint8: DType
    uint16: DType
    uint32: DType
    uint64: DType

class DTypesIntegral(DTypesSigned, DTypesUnsigned): ...

class DTypesReal(TypedDict):
    float32: DType
    float64: DType

class DTypesComplex(TypedDict):
    complex64: DType
    complex128: DType

class DTypesNumeric(DTypesIntegral, DTypesReal, DTypesComplex): ...
class DTypesAll(DTypesBool, DTypesNumeric): ...

type DTypesAny = Mapping[str, DType]

# Names in __all__ with no definition:
#   Capabilities
#   DefaultDTypes
