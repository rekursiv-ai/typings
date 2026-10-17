from typing import IO

from reportlab.graphics.shapes import Drawing

def drawToFile(
    d: Drawing,
    fn: str | IO[bytes],
    fmt: str = "GIF",
    dpi: float = 72,
    bg: int = 0xFFFFFF,
    configPIL: dict[str, object] | None = None,
    *,
    backend: str = "rlPyCairo",
    backendFmt: str = "RGB",
) -> None: ...
