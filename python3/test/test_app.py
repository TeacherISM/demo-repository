from flask.testing import FlaskClient
import pytest
from src import app


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_home(client: FlaskClient):
    result = client.get('/')
    assert result.status_code == 200
    assert result.data == b"Hello, World!"


def test_welcome(client: FlaskClient):
    result = client.get('/welcome')
    assert result.status_code == 200
    assert result.content_type == 'text/html; charset=utf-8'


def test_find_next_id():
    result = app._find_next_id()
    assert result == 4


def test_get_countries(client: FlaskClient):
    result = client.get('/countries')
    assert result.status_code == 200
    assert result.content_type == 'application/json'

    def setUp(self):
        self.app = app.app.test_client()

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertIn(b"WELCOME!", result.data)

    def test_countries(self):
        result = self.app.get('/countries')
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)

    def test_add_country(self):
        result = self.app.post('/countries', json={"name": "New Zealand", "capital": "Wellington", "area": 268021})
        self.assertIn(b"New Zealand", result.data)
        self.assertIn(b"Wellington", result.data)
        self.assertIn(b"268021", result.data)
        self.assertIn(b"4", result.data)
        self.assertEqual(result.status_code, 201)

def test_post_countries(client: FlaskClient):
    result = client.post('/countries', json={"name": "Japan", "capital": "Tokyo", "area": 377975})
    assert result.status_code == 201
    assert result.content_type == 'application/json'

    err_result = client.post('/countries', data="hola")
    assert err_result.status_code == 415
    assert err_result.content_type == 'application/json'
