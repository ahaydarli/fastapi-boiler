import http
from typing import Optional, Dict, Any

from fastapi.exceptions import HTTPException
from starlette import status


class InternalServerError(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = "Internal Server Error"


class NotFoundError(HTTPException):
    def __init__(self, entity: str = None, key: str = "id"):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = (
            f"{entity.lower().capitalize()} with given {key.lower()} not found"
            if entity
            else "Error: Not Found"
        )


class NotValidError(HTTPException):
    def __init__(self, entity: str = None):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = (
            f"{entity.lower().capitalize()} is not valid"
            if entity
            else "Error: Bad Request"
        )


class SettingsError(Exception):
    pass


class CustomHTTPException(Exception):
    def __init__(
        self,
        status_code: int,
        message: str = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        if message is None:
            message = http.HTTPStatus(status_code).phrase
        self.status_code = status_code
        self.message = message
        self.headers = headers

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return (
            f"{class_name}(status_code={self.status_code!r}, message={self.message!r})"
        )
