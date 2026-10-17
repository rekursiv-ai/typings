from typing import TypedDict

class BotoCoreError(Exception): ...
class NoRegionError(BotoCoreError): ...
class NoCredentialsError(BotoCoreError): ...

class ErrorDetail(TypedDict):
    Code: str
    Message: str

class ErrorResponse(TypedDict):
    Error: ErrorDetail

class ClientError(Exception):
    response: ErrorResponse
    def __init__(self, error_response: ErrorResponse, operation_name: str) -> None: ...
