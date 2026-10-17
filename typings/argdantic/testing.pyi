from argparse import Namespace
from typing import Any

from argdantic import ArgParser

class Result:
    def __init__(
        self,
        return_value: Any,
        exception: Exception | None,
        exc_info: Any | None,
    ) -> None: ...

class CLIRunner:
    def __init__(self, catch_exceptions: bool = ...) -> None: ...
    def invoke(self, cli: ArgParser, args: Namespace | None) -> Any: ...
