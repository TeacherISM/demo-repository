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
        #self.assert_template_used('mytemplate.html')

