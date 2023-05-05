from src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def test_assert_mytemplate_used(self):
        response = self.client.get('/welcome')
        self.assertIn("GINA", response.data)
        #self.assert_template_used('mytemplate.html')

