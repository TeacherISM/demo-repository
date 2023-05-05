import sys
from flask.testing import FlaskClient
from src.app import app
from unittest import TestCase

sys.path.append("../src")


class AppTest(TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        result = self.client.get('/')
        self.assertEqual(result.data, b"Hello, World!")

    def test_welcome(self):
        result = self.client.get("/welcome")
        self.assertIn(b"Welcome!", result.data)

    def test_get_countries(self):
        result = self.client.get("/countries")
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)

    def test_add_country(self):
        result = self.client.post('/countries', json={"name": "New Zealand", "capital": "Wellington", "area": 268021})
        self.assertIn(b"New Zealand", result.data)
        self.assertIn(b"Wellington", result.data)
        self.assertIn(b"268021", result.data)

    def test_add_country_missing_json(self):
        result = self.client.post('/countries')
        self.assertEqual(result.status_code, 415)
        self.assertIn(b"Request must be JSON", result.data)

