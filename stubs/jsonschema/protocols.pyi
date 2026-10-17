from collections.abc import Iterator, Mapping, Sequence
from typing import Any, ClassVar, Protocol

from _typeshed import Incomplete
from jsonschema._format import FormatChecker
from jsonschema._types import TypeChecker
from jsonschema.exceptions import ValidationError

import referencing.jsonschema

type _JsonParameter = (
    str
    | int
    | float
    | bool
    | Mapping[str, _JsonParameter]
    | Sequence[_JsonParameter]
    | None
)

class Validator(Protocol):
    META_SCHEMA: ClassVar[dict[Incomplete, Incomplete]]
    VALIDATORS: ClassVar[dict[Incomplete, Incomplete]]
    TYPE_CHECKER: ClassVar[TypeChecker]
    FORMAT_CHECKER: ClassVar[FormatChecker]
    schema: referencing.jsonschema.Schema
    def __init__(
        self,
        schema: Mapping[Incomplete, Incomplete] | bool,
        resolver: Any = ...,
        format_checker: FormatChecker | None = ...,
        *,
        registry: referencing.jsonschema.SchemaRegistry = ...,
    ) -> None: ...
    @classmethod
    def check_schema(cls, schema: dict[Incomplete, Incomplete]) -> None: ...
    def is_type(self, instance: object, type: str) -> bool: ...
    def is_valid(self, instance: object) -> bool: ...
    def iter_errors(self, instance: object) -> Iterator[ValidationError]: ...
    def validate(self, instance: object) -> None: ...
    def evolve(self, **kwargs) -> Validator: ...
