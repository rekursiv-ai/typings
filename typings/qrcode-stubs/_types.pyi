# Type aliases used in this stub package
from typing import Any, Protocol, type_check_only

from _typeshed import SupportsWrite

type Box = tuple[tuple[int, int], tuple[int, int]]
type Ink = tuple[int, int, int] | tuple[int, int, int, int]

# Don't try to make these Literal[x, y, z] as this really wreaks
# havoc with overloads in mypy.
type ErrorCorrect = int
type MaskPattern = int

@type_check_only
class Writeable(SupportsWrite[bytes], Protocol):
    def seek(self, offset: int, /) -> Any: ...
