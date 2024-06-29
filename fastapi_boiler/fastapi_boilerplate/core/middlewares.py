import logging
import time
import traceback
from fastapi import Request, status
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


async def catch_exceptions_middleware(request: Request, call_next):
    """
    Middleware to catch and handle exceptions during request processing.

    This middleware logs detailed information about exceptions that occur during
    the processing of a request, including the method, parameters, path, client IP,
    and headers. It also measures the time taken to process the request.

    Args:
        request (Request): The incoming HTTP request.
        call_next: The next middleware or endpoint to call.

    Returns:
        JSONResponse: A JSON response with status code 500 in case of an error.
    """
    start_time = time.time()
    try:
        # Process the request and get the response from the next middleware or endpoint
        response = await call_next(request)
    except Exception as e:
        # Log the full traceback for debugging purposes
        logger.error("Exception occurred:\n%s", traceback.format_exc())

        # Prepare the error response
        response = JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal Server Error"},
        )

        # Collect detailed error data
        error_data = {
            "status": response.status_code,
            "method": request.method,
            "params": dict(request.query_params),
            "path_params": request.path_params,
            "ip": request.client.host,
            "time": time.time() - start_time,
            "headers": dict(request.headers),
            "error": traceback.format_exc()[-1800:],
        }

        # Log the error data for further analysis
        logger.error("Error data: %s", error_data)

    finally:
        end_time = time.time()
        logger.info("Request processing took %.2f seconds", end_time - start_time)

    return response
