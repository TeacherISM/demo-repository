import sys
from unittest import TestCase
from src import app

sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")
