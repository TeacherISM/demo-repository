from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class AppTest(TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def test_welcome(self):
        result = self.app.get("/welcome")
        html = result.data.decode()
        assert "<h1>Hello World!</h1>" in html
        assert "<h2>Welcome to FlaskApp!</h2>" in html
        assert result.status_code == 200
        self.assertEqual(result.status_code, 200)
    
    def test_get_countries(self):
        result = self.app.get("/countries")
        result.data.decode()
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)
        self.assertEqual(result.status_code, 200)

    def test_add_country(self):
        result = self.app.post("/countries", json={"id": 4, "name": "Japan", "capital": "Tokyo", "area": 377972})
        result.data.decode()
        self.assertIn(b"Japan", result.data)
        self.assertEqual(result.status_code, 201)

    def test_add_country_error(self):
        result = self.app.post("/countries")
        result.data.decode()
        self.assertEqual(result.status_code, 415)