from e2b.api.client.client import AuthenticatedClient
from e2b.connection_config import ConnectionConfig

def get_api_client(config: ConnectionConfig) -> AuthenticatedClient: ...
