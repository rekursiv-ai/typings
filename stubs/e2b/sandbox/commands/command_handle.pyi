from dataclasses import dataclass

from e2b.exceptions import SandboxException

@dataclass
class CommandResult:
    exit_code: int
    stdout: str
    stderr: str
    error: str | None

@dataclass
class CommandExitException(SandboxException, CommandResult): ...
