import pytest
from alembic import command
from alembic.config import Config
from starlette.testclient import TestClient
from sqlalchemy_utils import database_exists, create_database, drop_database

from {{ cookiecutter.project }} import app, settings


@pytest.fixture(autouse=True)
def create_test_database():
    test_url = str(settings.TEST_DATABASE_URL)
    assert not database_exists(test_url), 'Test database already exists. Aborting tests.'
    create_database(test_url)
    config = Config("alembic.ini")
    try:
        command.upgrade(config, "head", "--sql")  # offline, for coverage
        command.upgrade(config, "head")
        yield
        command.downgrade(config, "base")
    finally:
        drop_database(test_url)


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
