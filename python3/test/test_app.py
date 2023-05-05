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

    def test_html(self):
        result = self.app.get('/welcome')
        self.assertIn(b"GINA", result.data)
    
    def test_countries(self):
        result = self.app.get('/countries')
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)

    def test_post(self):
        result = self.app.post('/countries', json={"name":"Mexico", "capital":"CDMX", "area":"4561534"})
        self.assertIn(b"Mexico", result.data)
        self.assertIn(b"CDMX", result.data)
        self.assertIn(b"4561534", result.data)
        self.assertIn(b"4", result.data)
        self.assertEqual(result.status_code, 201)


