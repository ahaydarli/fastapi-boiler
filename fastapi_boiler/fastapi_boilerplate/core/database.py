from abc import ABC
from peewee import Model, MySQLDatabase, DoesNotExist
from playhouse.shortcuts import ReconnectMixin

from settings import settings
from core.extensions import db
from core.exceptions import NotFoundError


class StrictMySQLDatabase(ReconnectMixin, MySQLDatabase, ABC):
    """
    Custom MySQL database class that includes automatic reconnection capabilities.

    This class inherits from ReconnectMixin and MySQLDatabase, adding the capability
    to automatically reconnect to the database if the connection is lost.

    Args:
        ReconnectMixin: Provides automatic reconnection logic.
        MySQLDatabase: The base class for MySQL database connection in Peewee.
        ABC: Abstract Base Class for additional structure.
    """

    def _connect(self, **kwargs):
        """
        Establishes a connection to the database.

        This method overrides the _connect method from MySQLDatabase to use the
        reconnection logic provided by ReconnectMixin.

        Returns:
            The database connection object.
        """
        return super(StrictMySQLDatabase, self)._connect()


# Create a database connection using the custom StrictMySQLDatabase class
db_connection = StrictMySQLDatabase(
    str(settings.database["db_name"]),
    user=str(settings.database["user"]),
    password=str(settings.database["password"]),
    host=str(settings.database["host"]),
    port=settings.database["port"],
    charset=settings.database["charset"],
)


class BaseModel(Model):
    """
    Base model class for Peewee ORM models.

    This class sets the default database connection for all models that inherit from it
    and provides additional utility methods.

    Meta:
        database (StrictMySQLDatabase): The database connection to use for this model.
    """

    class Meta:
        database = db

    @classmethod
    def get_or_404(cls, *query, **filters):
        """
        Retrieves a single record matching the given query or raises a 404 error.

        This method attempts to retrieve a record matching the specified query and filters.
        If no matching record is found, it raises a NotFoundError.

        Args:
            *query: Positional arguments for the query.
            **filters: Keyword arguments for filtering the query.

        Returns:
            The matching record.

        Raises:
            NotFoundError: If no matching record is found.
        """
        try:
            return cls.get(*query, **filters)
        except DoesNotExist:
            entity = cls.__name__
            raise NotFoundError(entity=entity)
