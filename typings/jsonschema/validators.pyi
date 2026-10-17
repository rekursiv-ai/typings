from collections.abc import Callable, Generator, Iterable, Iterator, Mapping
from contextlib import contextmanager
from typing import Any, ClassVar, overload, type_check_only
from typing_extensions import deprecated

from _typeshed import Incomplete, SupportsKeysAndGetItem
from referencing.jsonschema import Schema, SchemaRegistry
from referencing.typing import URI

from ._format import FormatChecker
from ._types import TypeChecker
from ._utils import Unset, URIDict
from .exceptions import ValidationError
from .protocols import Validator

type _JsonObject = Mapping[str, Any]
type _JsonValue = _JsonObject | list[Any] | str | int | float | bool | None
type _ValidatorCallback = Callable[
    [Any, Any, _JsonValue, _JsonObject],
    Iterator[ValidationError],
]

@type_check_only
class _Validator(Validator):
    VALIDATORS: ClassVar[dict[Incomplete, Incomplete]]
    META_SCHEMA: ClassVar[dict[Incomplete, Incomplete]]
    TYPE_CHECKER: ClassVar[Incomplete]
    FORMAT_CHECKER: ClassVar[Incomplete]
    @staticmethod
    def ID_OF(contents: Schema) -> URI | None: ...

    schema: Schema
    format_checker: FormatChecker | None
    def __init__(
        self,
        schema: Mapping[Incomplete, Incomplete] | bool,
        resolver: Any = ...,
        format_checker: FormatChecker | None = ...,
        *,
        registry: SchemaRegistry = ...,
    ) -> None: ...
    @classmethod
    def check_schema(
        cls,
        schema: Schema,
        format_checker: FormatChecker | Unset = ...,
    ) -> None: ...
    @property
    @deprecated(
        "Accessing resolver() is deprecated as of v4.18.0, "
        "in favor of the https://github.com/python-jsonschema/referencing library.",
    )
    def resolver(self): ...
    def evolve(self, **changes) -> _Validator: ...
    @overload
    def iter_errors(self, instance: object) -> Generator[ValidationError]: ...
    @overload
    @deprecated(
        "Passing a schema to Validator.iter_errors is deprecated and will be removed in a future release.",
    )
    def iter_errors(
        self,
        instance: object,
        _schema: Schema | None,
    ) -> Generator[ValidationError]: ...
    def descend(
        self,
        instance,
        schema: Schema,
        path: Incomplete | None = ...,
        schema_path: Incomplete | None = ...,
        resolver=...,
    ) -> Generator[Incomplete]: ...
    def validate(self, *args, **kwargs) -> None: ...
    def is_type(self, instance, type) -> bool: ...
    @overload
    def is_valid(self, instance) -> bool: ...
    @overload
    @deprecated(
        "Passing a schema to Validator.is_valid is deprecated and will be removed in a future release.",
    )
    def is_valid(self, instance, _schema: Schema | None) -> bool: ...

def validates(version: str) -> Callable[[_Validator], _Validator]: ...
def create(
    meta_schema: Schema,
    validators: Mapping[str, _ValidatorCallback] | tuple[()] = ...,
    version=...,
    type_checker: TypeChecker = ...,
    format_checker: FormatChecker = ...,
    id_of: Callable[[Schema], str] = ...,
    applicable_validators: Callable[
        [Schema],
        Iterable[tuple[str, _ValidatorCallback]],
    ] = ...,
) -> type[_Validator]: ...
def extend(
    validator,
    validators=...,
    version=...,
    type_checker=...,
    format_checker=...,
): ...

class Draft3Validator(_Validator):
    __slots__ = ...

class Draft4Validator(_Validator):
    __slots__ = ...

class Draft6Validator(_Validator):
    __slots__ = ...

class Draft7Validator(_Validator):
    __slots__ = ...

class Draft201909Validator(_Validator):
    __slots__ = ...

class Draft202012Validator(_Validator):
    __slots__ = ...

type _Handler = Callable[[str], Incomplete]

@deprecated(
    "jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the "
    "https://github.com/python-jsonschema/referencing library, which "
    "provides more compliant referencing behavior as well as more "
    "flexible APIs for customization. A future release will remove "
    "RefResolver. Please file a feature request (on referencing) if you "
    "are missing an API for the kind of customization you need.",
)
class RefResolver:
    referrer: dict[str, Incomplete]
    cache_remote: Incomplete
    handlers: dict[str, _Handler]
    store: URIDict
    def __init__(
        self,
        base_uri: str,
        referrer: dict[str, Incomplete],
        store: Mapping[str, Mapping[str, Any]]
        | Iterable[tuple[str, Mapping[str, Any]]] = ...,
        cache_remote: bool = ...,
        handlers: SupportsKeysAndGetItem[str, _Handler]
        | Iterable[tuple[str, _Handler]] = ...,
        urljoin_cache=...,
        remote_cache=...,
    ) -> None: ...
    @classmethod
    def from_schema(cls, schema: Schema, id_of=..., *args, **kwargs): ...
    def push_scope(self, scope) -> None: ...
    def pop_scope(self) -> None: ...
    @property
    def resolution_scope(self): ...
    @property
    def base_uri(self) -> str: ...
    @contextmanager
    @deprecated(
        "jsonschema.RefResolver.in_scope is deprecated and will be removed in a future release.",
    )
    def in_scope(self, scope) -> Generator[None]: ...
    @contextmanager
    def resolving(self, ref: str) -> Generator[Incomplete]: ...
    def resolve(self, ref: str) -> tuple[str, Incomplete]: ...
    def resolve_from_url(self, url: str): ...
    def resolve_fragment(self, document, fragment: str): ...
    def resolve_remote(self, uri: str): ...

def validate(
    instance: object,
    schema: Schema,
    cls: type[_Validator] | None = ...,
    *args: Any,
    **kwargs: Any,
) -> None: ...
def validator_for(
    schema: Schema | bool,
    default: type[Validator] | Unset = ...,
) -> type[Validator]: ...
