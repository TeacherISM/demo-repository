from src import app
from unittest import TestCase
from flask import json
import sys

sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")
    
class MyAppTestCase(TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_greeting(self):
        rv = self.app.get('/welcome')
        self.assertIn(b"Welcome!", rv.data)
        