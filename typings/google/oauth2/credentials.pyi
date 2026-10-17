from collections.abc import Sequence
from typing import Self

from google.auth import credentials

class Credentials(credentials.Credentials):
    refresh_token: str | None
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        token: str | None,
        refresh_token: str | None = ...,
        id_token: str | None = ...,
        token_uri: str | None = ...,
        client_id: str | None = ...,
        client_secret: str | None = ...,
        scopes: Sequence[str] | None = ...,
        default_scopes: Sequence[str] | None = ...,
        quota_project_id: str | None = ...,
        expiry: object | None = ...,
        rapt_token: str | None = ...,
        refresh_handler: object | None = ...,
        enable_reauth_refresh: bool = ...,
        granted_scopes: Sequence[str] | None = ...,
        trust_boundary: object | None = ...,
        universe_domain: str = ...,
        account: str = ...,
    ) -> None: ...
    def to_json(self, strip: Sequence[str] | None = ...) -> str: ...
    @classmethod
    def from_authorized_user_info(
        cls,
        info: dict[str, object],
        scopes: Sequence[str] | None = ...,
    ) -> Self: ...
    @classmethod
    def from_authorized_user_file(
        cls,
        filename: str,
        scopes: Sequence[str] | None = ...,
    ) -> Self: ...
