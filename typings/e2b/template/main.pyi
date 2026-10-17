from pathlib import Path

class TemplateBuilder:
    def copy(
        self,
        src: str | Path,
        dest: str | Path,
        *,
        user: str | None = ...,
    ) -> TemplateBuilder: ...
    def run_cmd(
        self,
        command: str | list[str],
        user: str | None = ...,
    ) -> TemplateBuilder: ...

class TemplateBase:
    def __init__(
        self,
        file_context_path: str | Path | None = ...,
        file_ignore_patterns: list[str] | None = ...,
    ) -> None: ...
    def from_image(self, image: str) -> TemplateBuilder: ...
    @staticmethod
    def to_dockerfile(template: TemplateBuilder | TemplateBase) -> str: ...
    @staticmethod
    def to_json(template: TemplateBuilder | TemplateBase) -> str: ...
