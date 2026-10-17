from hatchet_sdk import Context

import pydantic

class BaseWorkflow: ...

class TaskRunRef[TIn: pydantic.BaseModel, R]:
    @property
    def workflow_run_id(self) -> str: ...
    async def aio_result(self) -> R: ...
    def result(self) -> R: ...

class Standalone[TIn: pydantic.BaseModel, R](BaseWorkflow):
    def run(self, input: TIn = ...) -> R: ...
    async def aio_run(self, input: TIn = ...) -> R: ...
    def run_no_wait(
        self,
        input: TIn = ...,
        *,
        child_key: str | None = None,
    ) -> TaskRunRef[TIn, R]: ...
    async def aio_run_no_wait(
        self,
        input: TIn = ...,
        *,
        child_key: str | None = None,
    ) -> TaskRunRef[TIn, R]: ...

__all__ = ["BaseWorkflow", "Context", "Standalone", "TaskRunRef"]
