from src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")
