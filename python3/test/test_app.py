import sys
sys.path.append('../src')

from src import app
from unittest import TestCase

class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

