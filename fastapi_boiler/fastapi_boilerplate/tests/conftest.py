import pytest
from fastapi.testclient import TestClient

from core.factory import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    yield app


@pytest.fixture(scope="module")
def client(app):
    return TestClient(app)
