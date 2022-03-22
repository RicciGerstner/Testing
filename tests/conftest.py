"""
Fixture functions that run before the test suite.
"""
import pytest
from starlette.testclient import TestClient

from Demo.app import create_app


@pytest.fixture
def client():
    app = create_app()

    with TestClient(app) as client:
        yield client
