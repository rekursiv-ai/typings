from collections.abc import Coroutine

from e2b.sandbox.sandbox_api import (
    SandboxInfo,
    SandboxNetworkOpts,
    SandboxNetworkUpdate,
    SandboxQuery,
)
from e2b.sandbox_async.commands.command import Commands
from e2b.sandbox_async.filesystem.filesystem import Filesystem
from e2b.sandbox_async.paginator import AsyncSandboxPaginator

class AsyncSandbox:
    @property
    def sandbox_id(self) -> str: ...
    @property
    def files(self) -> Filesystem: ...
    @property
    def commands(self) -> Commands: ...
    def download_url(
        self,
        path: str,
        user: str | None = ...,
        use_signature_expiration: int | None = ...,
    ) -> str: ...
    def upload_url(
        self,
        path: str,
        user: str | None = ...,
        use_signature_expiration: int | None = ...,
    ) -> str: ...
    @classmethod
    def create(
        cls,
        template: str | None = ...,
        timeout: int | None = ...,
        metadata: dict[str, str] | None = ...,
        envs: dict[str, str] | None = ...,
        secure: bool = ...,
        allow_internet_access: bool = ...,
        *,
        network: SandboxNetworkOpts | None = ...,
        api_key: str | None = ...,
    ) -> Coroutine[object, object, AsyncSandbox]: ...
    @staticmethod
    def connect(
        sandbox_id: str,
        timeout: int | None = ...,
        *,
        api_key: str | None = ...,
    ) -> Coroutine[object, object, AsyncSandbox]: ...
    @staticmethod
    async def kill(sandbox_id: str, *, api_key: str | None = ...) -> bool: ...
    @staticmethod
    async def get_info(
        sandbox_id: str,
        *,
        api_key: str | None = ...,
    ) -> SandboxInfo: ...
    @staticmethod
    async def update_network(
        sandbox_id: str,
        *,
        network: SandboxNetworkUpdate,
        api_key: str | None = ...,
    ) -> None: ...
    @classmethod
    def list(
        cls,
        query: SandboxQuery | None = ...,
        limit: int | None = ...,
        next_token: str | None = ...,
        *,
        api_key: str | None = ...,
        request_timeout: float | None = ...,
    ) -> AsyncSandboxPaginator: ...
