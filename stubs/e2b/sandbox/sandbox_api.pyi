from datetime import datetime
from typing import TypedDict

class SandboxNetworkOpts(TypedDict, total=False):
    allow_public_traffic: bool
    allow_out: list[str]
    deny_out: list[str]
    rules: dict[str, list[SandboxNetworkRule]]

class SandboxNetworkRule(TypedDict, total=False):
    transform: SandboxNetworkTransform

class SandboxNetworkTransform(TypedDict, total=False):
    headers: dict[str, str]

class SandboxNetworkUpdate(TypedDict, total=False):
    allow_out: list[str]
    deny_out: list[str]
    rules: dict[str, list[SandboxNetworkRule]]

class SandboxInfo:
    sandbox_id: str
    metadata: dict[str, str]
    started_at: datetime
    end_at: datetime

class SandboxQuery:
    metadata: dict[str, str] | None
    def __init__(self, metadata: dict[str, str] | None = ...) -> None: ...
