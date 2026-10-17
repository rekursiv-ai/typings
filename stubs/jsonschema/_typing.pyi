from collections.abc import Callable, Iterable
from typing import Any, Protocol

from jsonschema.protocols import Validator
from referencing.jsonschema import Schema

class SchemaKeywordValidator(Protocol):
    def __call__(
        self,
        validator: Validator,
        value: Any,
        instance: Any,
        schema: Schema,
    ) -> None: ...

type id_of = Callable[[Schema], str | None]
type ApplicableValidators = Callable[[Schema], Iterable[tuple[str, Any]]]
