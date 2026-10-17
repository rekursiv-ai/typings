from collections.abc import Callable

from e2b.template.logger import LogEntry
from e2b.template.main import TemplateBase, TemplateBuilder
from e2b.template.types import BuildInfo

class AsyncTemplate(TemplateBase):
    @classmethod
    async def build(
        cls,
        template: TemplateBuilder | TemplateBase,
        name: str | None = ...,
        *,
        cpu_count: int = ...,
        memory_mb: int = ...,
        min_free_disk_mb: int | None = ...,
        api_key: str | None = ...,
        on_build_logs: Callable[[LogEntry], None] | None = ...,
    ) -> BuildInfo: ...
