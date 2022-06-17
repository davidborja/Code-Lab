import pytest
import os
from app import create_app
from app import db as _db


@pytest.fixture(scope="session")
def app():
    flask_env = os.environ.get("FLASK_ENV")
    app = create_app(flask_env)
    yield app


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        with app.app_context():
            _db.drop_all()
            _db.create_all()
        yield client


@pytest.fixture(scope="session")
def db(app):
    app.app_context().push()
    _db.init_app(app)
    _db.create_all()
    yield _db
    _db.session.close()
    _db.drop_all()
