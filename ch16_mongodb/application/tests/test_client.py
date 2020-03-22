import pytest
import sys
import os

from application.pypi_org import app
from application.pypi_org.app import app as flask_app

container_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
))
sys.path.insert(0, container_folder)


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    client = flask_app.test_client()
    try:
        app.register_blueprints()
    except Exception as e:
        pass

    app.setup_db()
    yield client
