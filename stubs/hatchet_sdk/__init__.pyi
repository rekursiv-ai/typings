from collections.abc import Awaitable, Callable, Mapping, Sequence
from datetime import timedelta

from hatchet_sdk.runnables.workflow import BaseWorkflow, Standalone

import pydantic

class Context:
    @property
    def workflow_run_id(self) -> str: ...
    def log(
        self,
        line: str | Mapping[str, object],
        raise_on_error: bool = False,
    ) -> None: ...
    async def aio_log(
        self,
        line: str | Mapping[str, object],
        raise_on_error: bool = False,
    ) -> None: ...

class DurableContext(Context): ...

class Worker:
    def start(self) -> None: ...

class Hatchet:
    def __init__(self) -> None: ...
    def task[
        TIn: pydantic.BaseModel,
        R: pydantic.BaseModel | Mapping[str, object] | None,
    ](
        self,
        *,
        name: str | None = None,
        input_validator: type[TIn],
        retries: int = 0,
        execution_timeout: timedelta | str = ...,
        schedule_timeout: timedelta | str = ...,
    ) -> Callable[
        [Callable[[TIn, Context], R | Awaitable[R]]],
        Standalone[TIn, R],
    ]: ...
    def durable_task[
        TIn: pydantic.BaseModel,
        R: pydantic.BaseModel | Mapping[str, object] | None,
    ](
        self,
        *,
        name: str | None = None,
        input_validator: type[TIn],
        retries: int = 0,
        execution_timeout: timedelta | str = ...,
        schedule_timeout: timedelta | str = ...,
    ) -> Callable[
        [Callable[[TIn, DurableContext], R | Awaitable[R]]],
        Standalone[TIn, R],
    ]: ...
    def worker(
        self,
        name: str,
        slots: int | None = None,
        *,
        workflows: Sequence[BaseWorkflow] | None = None,
    ) -> Worker: ...
