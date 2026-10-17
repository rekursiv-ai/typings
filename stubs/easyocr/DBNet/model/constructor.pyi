from typing import Any, Self

class State:
    def __init__(self, autoload=..., default=...) -> None: ...

class StateMeta(type):
    def __new__(mcs, name, bases, attrs) -> Self: ...

class Configurable(metaclass=StateMeta):
    def __init__(self, *args, cmd=..., **kwargs) -> None: ...
    @staticmethod
    def construct_class_from_config(args) -> Any: ...
    @staticmethod
    def extract_class_from_args(args) -> Any: ...
    def load_all(self, **kwargs) -> None: ...
    def load(self, state_name, **kwargs) -> None: ...
    def create_member_from_config(
        self,
        conf,
    ) -> (
        int
        | float
        | str
        | list[
            Any
            | int
            | float
            | str
            | list[Any]
            | dict[
                Any,
                Any
                | int
                | float
                | str
                | list[Any | int | float | str | list[Any] | dict[Any, Any]]
                | dict[Any, Any],
            ]
        ]
        | Any
        | dict[
            Any,
            Any
            | int
            | float
            | str
            | list[Any | int | float | str | list[Any] | dict[Any, Any]]
            | dict[Any, Any],
        ]
    ): ...
    def dump(self) -> dict[Any, Any]: ...
    def dump_obj(
        self,
        obj,
    ) -> (
        int
        | float
        | str
        | list[
            Any
            | int
            | float
            | str
            | list[Any]
            | dict[Any, Any | int | float | str | list[Any] | dict[Any, Any] | None]
            | None
        ]
        | dict[Any, Any]
        | None
    ): ...
