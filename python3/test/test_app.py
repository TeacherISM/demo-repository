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
        rv = self.app.get('/welcome')
        self.assertIn(b"Welcome!", rv.data)

    def test_countries(self):
        rv = self.app.get('/countries')
        self.assertIn(b"Thailand", rv.data)
        self.assertIn(b"Australia", rv.data)
        self.assertIn(b"Egypt", rv.data)

    def test_add_country(self):
        rv = self.app.post('/countries', json={"name": "New Zealand", "capital": "Wellington", "area": 268021})
        self.assertIn(b"New Zealand", rv.data)
        self.assertIn(b"Wellington", rv.data)
        self.assertIn(b"268021", rv.data)
        self.assertIn(b"4", rv.data)
        self.assertEqual(rv.status_code, 201)
    
    def test_add_country_invalid(self):
        rv = self.app.post('/countries', data="This is not JSON")
        self.assertIn(b"Request must be JSON", rv.data)
        self.assertEqual(rv.status_code, 415)
        