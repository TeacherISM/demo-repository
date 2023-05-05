import sys
from src import app
from unittest import TestCase
sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def setUp(self):
        self.app = app.app.test_client()

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertIn(b"WELCOME", result.data)
    
    def test_countries(self):
        result = self.app.get('/countries')
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)
    
    def test_add_country(self):
        result = self.app.post('/countries', json={"name":"USA", "capital":"Washington", "area":"2694825"})
        self.assertIn(b"USA", result.data)
        self.assertIn(b"Washington", result.data)
        self.assertIn(b"2694825", result.data)
        self.assertIn(b"4", result.data)
        self.assertEqual(result.status_code, 201)