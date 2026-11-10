from enum import StrEnum

from e2b.api.client.types import Unset

class SandboxState(StrEnum):
    PAUSED = "paused"
    RUNNING = "running"

class SandboxPauseMode(StrEnum):
    FILESYSTEM = "filesystem"
    FULL = "full"

class SandboxDetail:
    state: SandboxState
    cpu_count: int
    memory_mb: int
    pause_mode: SandboxPauseMode | Unset

class Error:
    code: int
    message: str
