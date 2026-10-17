from typing import Any, Literal, Protocol, TypedDict, overload

__all__ = [
    "SecretValue",
    "SecretsManagerClient",
    "SecretsManagerExceptions",
    "Session",
]

class SecretValue(TypedDict, total=False):
    Name: str
    SecretString: str
    SecretBinary: bytes

class SecretsManagerExceptions(Protocol):
    @property
    def ResourceNotFoundException(self) -> type[Exception]: ...
    @property
    def InvalidRequestException(self) -> type[Exception]: ...

class SecretsManagerClient(Protocol):
    @property
    def exceptions(self) -> SecretsManagerExceptions: ...
    def get_secret_value(self, *, SecretId: str) -> SecretValue: ...
    def create_secret(self, *, Name: str, SecretString: str) -> dict[str, str]: ...
    def put_secret_value(
        self,
        *,
        SecretId: str,
        SecretString: str,
    ) -> dict[str, str]: ...
    def delete_secret(
        self,
        *,
        SecretId: str,
        ForceDeleteWithoutRecovery: bool,
    ) -> dict[str, str]: ...

class Session:
    def __init__(
        self,
        *,
        profile_name: str | None = ...,
        region_name: str | None = ...,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
    ) -> None: ...
    @overload
    def client(
        self,
        service_name: Literal["secretsmanager"],
    ) -> SecretsManagerClient: ...
    @overload
    def client(self, service_name: str, **kwargs: Any) -> Any: ...
    def resource(self, service_name: str, **kwargs: Any) -> Any: ...
