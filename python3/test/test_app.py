import sys
from src import app
from unittest import TestCase
sys.path.append('../src')


class AppTest(TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def test_welcome(self):
        result = self.app.get('/welcome')
        assert result.status_code == 200
        self.assertIn(b'Bienvenidos al Himalaya!', result.data)

    def test_countries(self):
        result = self.app.get('/countries')
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)

    def test_add_country(self):
        result = self.app.post('/countries', json={"name": "New Zealand", "capital": "Wellington", "area": 268521})
        self.assertIn(b"New Zealand", result.data)
        self.assertIn(b"Wellington", result.data)
        self.assertIn(b"268521", result.data)
        self.assertIn(b"4", result.data)
        self.assertEqual(result.status_code, 201)

    def test_add_country_invalid(self):
        result = self.app.post('/countries')
        self.assertIn(b"Request must be JSON", result.data)
        self.assertEqual(result.status_code, 415)
