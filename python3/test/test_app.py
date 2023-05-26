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
        self.assertIn(b"Bangkok", result.data)
        self.assertIn(b"Canberra", result.data)
        self.assertIn(b"Cairo", result.data)
        self.assertIn(b"513120", result.data)
        self.assertIn(b"7617930", result.data)
        self.assertIn(b"1010408", result.data)
        self.assertIn(b"1", result.data)
        self.assertIn(b"2", result.data)
        self.assertIn(b"3", result.data)
        self.assertIn(b"id", result.data)
        self.assertIn(b"name", result.data)
        self.assertIn(b"capital", result.data)
        self.assertIn(b"area", result.data)
        

    def test_add_country(self):
        result = self.app.post('/countries', json={"name": "New Zealand", "capital": "Wellington", "area": 268021})
        self.assertIn(b"New Zealand", result.data)
        self.assertIn(b"Wellington", result.data)
        self.assertIn(b"268021", result.data)
        self.assertIn(b"4", result.data)
        self.assertIn(b"id", result.data)
        self.assertIn(b"name", result.data)
        self.assertIn(b"capital", result.data)
        self.assertIn(b"area", result.data)
        self.assertEqual(result.status_code, 201)
       
    def test_add_country_invalid(self):
        result = self.app.post('/countries', data="This is not JSON")
        self.assertIn(b"Request must be JSON", result.data)
        self.assertEqual(result.status_code, 415)
        self.assertEqual(result.status_code, 201)

    def test_add_country_invalid(self):
        result = self.app.post('/countries', data="This is not JSON")
        self.assertIn(b"Request must be JSON", result.data)
        self.assertEqual(result.status_code, 415)

