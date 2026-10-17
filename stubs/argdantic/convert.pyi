from collections.abc import Generator
from typing import Any

from argdantic.parsing import ActionTracker, Argument
from pydantic import BaseModel
from pydantic.fields import FieldInfo

def format_description(
    description: str | None,
    has_default: bool,
    is_required: bool,
) -> str: ...
def argument_from_field(
    field_info: FieldInfo,
    kebab_name: str,
    delimiter: str,
    internal_delimiter: str,
    parent_path: tuple[str, ...],
    custom_identifier: str | None = ...,
) -> Argument: ...
def model_to_args(
    model: type[BaseModel],
    delimiter: str,
    internal_delimiter: str,
    parent_path: tuple[str, ...] = ...,
) -> Generator[Argument]: ...
def args_to_dict_tree(
    kwargs: dict[str, Any],
    internal_delimiter: str,
    remove_helpers: bool = ...,
    cli_trackers: dict[str, ActionTracker] | None = ...,
) -> dict[str, Any]: ...
