import pytest
from src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

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

    def test_add_country_invalid(self):
        result = self.app.post('/countries', data="This is not JSON")
        self.assertIn(b"Request must be JSON", result.data)
        self.assertEqual(result.status_code, 415)


@pytest.fixture
def client():
    """Create a test client for the app."""
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_home(client):
    """Test that the home endpoint returns 'Hello, World!'."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"


def test_welcome(client):
    """Test that the welcome endpoint returns a rendered template."""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert "Welcome" in response.get_data(as_text=True)


def test_get_countries(client):
    """Test that the get_countries endpoint returns a list of countries."""
    response = client.get("/countries")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert all("id" in country for country in data)
    assert all("name" in country for country in data)
    assert all("capital" in country for country in data)
    assert all("area" in country for country in data)


def test_add_country(client):
    """Test that the add_country endpoint adds a new country to the list."""
    # Test adding a new country successfully
    new_country = {"name": "Canada", "capital": "Ottawa", "area": 9984670}
    response = client.post("/countries", json=new_country)
    assert response.status_code == 201
    assert response.content_type == "application/json"
    data = response.get_json()
    assert "id" in data
    assert data["name"] == new_country["name"]
    assert data["capital"] == new_country["capital"]
    assert data["area"] == new_country["area"]

    response = client.get("/countries")
    assert response.status_code == 200
    assert response.content_type == "application/json"
    data = response.get_json()
    assert len(data) == 4

    # Test adding a new country with invalid request format
    invalid_country = {"name": "USA", "capital": "Washington D.C.", "area": 9833520}
    response = client.post("/countries", data=invalid_country)
    assert response.status_code == 415
    assert response.content_type == "application/json"
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Request must be JSON"