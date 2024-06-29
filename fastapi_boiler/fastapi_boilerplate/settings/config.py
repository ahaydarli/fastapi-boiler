from functools import lru_cache
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """
    Application settings configuration using Pydantic's BaseSettings.

    This class defines the configuration settings for the FastAPI application.
    Settings can be loaded from environment variables or default values defined here.

    Attributes:
        debug (bool): Flag to enable/disable debug mode.
        app_title (str): The title of the FastAPI application.
        app_description (str): A brief description of the FastAPI application.
        api_version (str): The version of the API.
        api_prefix (str): The prefix for the API routes.
        database (dict): Database configuration details including host, port, user,
                         database name, password, and charset.
    """

    debug: bool = True
    app_title: str = "FastAPI Boilerplate"
    app_description: str = "FastAPI Boilerplate"
    api_version: str = "v1"
    api_prefix: str = "/v1"
    database: dict = {
        "host": "localhost",
        "port": "3306",
        "user": "root",
        "db_name": "fastapi",
        "password": "<PASSWORD>",
        "charset": "utf8mb4",
    }


@lru_cache()
def get_app_settings() -> AppSettings:
    """
    Retrieve the application settings with caching.

    This function returns the application settings instance, utilizing LRU cache
    to avoid reloading the settings multiple times. The cached settings improve
    performance and ensure consistency across the application.

    Returns:
        AppSettings: The application settings instance.
    """
    return AppSettings()


# Instantiate settings using the cached function
settings = get_app_settings()
