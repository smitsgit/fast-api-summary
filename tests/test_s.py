import os

import pytest
from starlette.testclient import TestClient

from app.main import create_app
from app.config import Settings, get_settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    # set up
    t_app = create_app()
    t_app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(t_app) as test_client:
        # testing
        yield test_client


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}
