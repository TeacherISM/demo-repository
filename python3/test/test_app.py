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
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome', result.data)
    
    def test_get_countries(self):
        result = self.app.get('/countries')
        self.assertEqual(result.status_code, 200)
        data = result.data.decode()
        self.assertIn('Thailand', data)
        self.assertIn('Australia', data)
        self.assertIn('Egypt', data)
    
    def test_add_country(self):
        result = self.app.post('/countries', json={"name": "New Zealand", "capital": "Wellington", "area": 268021})
        self.assertIn(b"New Zealand", result.data)
        self.assertIn(b"Wellington", result.data)
        self.assertIn(b"268021", result.data)
    
    def test_add_country_missing_json(self):
        result = self.app.post('/countries')
        self.assertEqual(result.status_code, 415)
        self.assertIn(b"Request must be JSON", result.data)
