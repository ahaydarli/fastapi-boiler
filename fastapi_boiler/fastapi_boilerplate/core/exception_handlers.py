from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from .exceptions import CustomHTTPException


async def routers_exception_handler(request: Request, exception: HTTPException):
    """
    Handle exceptions raised by the routers.

    This function catches HTTPException instances raised during the processing of
    a request and returns a JSON response with the appropriate status code and
    detail message.

    Args:
        request (Request): The incoming HTTP request.
        exception (HTTPException): The exception that was raised.

    Returns:
        JSONResponse: A JSON response containing the exception details.
    """
    return JSONResponse(
        status_code=exception.status_code, content={"detail": exception.detail}
    )


def custom_exception_handler(request: Request, exception: CustomHTTPException):
    """
    Handle custom exceptions.

    This function catches CustomHTTPException instances raised during the processing
    of a request and returns a JSON response with the appropriate status code and
    custom message.

    Args:
        request (Request): The incoming HTTP request.
        exception (CustomHTTPException): The custom exception that was raised.

    Returns:
        JSONResponse: A JSON response containing the custom exception message.
    """
    return JSONResponse(
        status_code=exception.status_code, content={"message": exception.message}
    )
