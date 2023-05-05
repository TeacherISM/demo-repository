from src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def test_welcome(self):
        self.assertTemplateUsed('welcome.html')
