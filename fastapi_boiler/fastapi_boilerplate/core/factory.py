from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app import views as api_views
from .exceptions import CustomHTTPException
from settings import settings
from .middlewares import catch_exceptions_middleware
from .extensions import db
from .database import db_connection
from .exception_handlers import routers_exception_handler, custom_exception_handler


def register_extensions(app: FastAPI):
    """
    Register third-party extensions.

    This function is a placeholder for registering extensions such as databases,
    cache systems, or any other third-party services that need to be initialized
    and attached to the FastAPI application instance.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    # Example: Initialize a database connection and attach it to the app.
    db.initialize(db_connection)
    return None


def register_routers(app: FastAPI):
    """
    Register app routers.

    This function registers the various routers for different parts of the
    application, which handle specific sets of endpoints. The prefix setting
    is used to prepend a common prefix to all routes in the router.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    app.include_router(api_views.router, prefix=settings.api_prefix)
    return None


def register_middlewares(app: FastAPI):
    """
    Register middleware.

    This function is a placeholder for adding middleware to the application.
    Middleware can handle tasks such as request/response logging, CORS, GZip,
    and other pre- or post-processing of requests and responses.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    # Example: Add CORS middleware
    app.middleware("http")(catch_exceptions_middleware)
    return None


def register_exceptions(app: FastAPI):
    """
    Register exception handlers.

    This function is a placeholder for adding custom exception handlers to the
    application. Exception handlers can catch specific exceptions and return
    custom responses.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    # Example: Handle 404 Not Found exceptions
    app.add_exception_handler(HTTPException, routers_exception_handler)
    app.add_exception_handler(CustomHTTPException, custom_exception_handler)

    return None


def on_startup():
    """
    Startup events.

    This function is a placeholder for tasks that need to be executed when
    the application starts up. This could include actions like initializing
    resources, logging, or running background tasks.

    """
    # Example: Log startup events
    pass


def on_shutdown():
    """
    Shutdown events.

    This function is a placeholder for tasks that need to be executed when
    the application shuts down. This could include actions like closing
    database connections, stopping background tasks, or flushing logs.

    """
    # Example: Close database connections
    pass


def create_app() -> FastAPI:
    """
    App factory.

    This function creates and configures the FastAPI application instance.
    It sets the application metadata such as title, description, and version.
    It also registers extensions, routers, middleware, and exception handlers,
    and defines startup and shutdown events.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    app = FastAPI(
        title=settings.app_title,
        description=settings.app_description,
        version=settings.api_version,
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
    )

    # Register various components with the app instance
    register_extensions(app)
    register_routers(app)
    register_middlewares(app)
    register_exceptions(app)

    return app
