from http import HTTPStatus

class Unset: ...

class Response[T]:
    status_code: HTTPStatus
    parsed: T | None
