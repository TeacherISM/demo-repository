import sys
import unittest
sys.path.append('../src')

from src import app
from unittest import TestCase


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def setUp(self):
        self.app = app.app.test_client()

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertIn(b'Welcome!', result.data)

    def test_countries(self):
        result = self.app.get('/countries')
        self.assertIn(b"Thailand", result.data)
        self.assertIn(b"Australia", result.data)
        self.assertIn(b"Egypt", result.data)

    def test_add_country(self):
        result = self.app.post('/countries', json={"name": "Turkey", "capital": "Ankara", "area": 80268021})
        self.assertIn(b"Turkey", result.data)
        self.assertIn(b"Ankara", result.data)
        self.assertIn(b"80268021", result.data)


