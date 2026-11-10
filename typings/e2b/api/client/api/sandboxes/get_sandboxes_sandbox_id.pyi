from e2b.api.client.client import AuthenticatedClient
from e2b.api.client.models import Error, SandboxDetail
from e2b.api.client.types import Response

async def asyncio_detailed(
    sandbox_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | SandboxDetail]: ...
