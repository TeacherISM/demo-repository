import sys
from src import app
from unittest import TestCase
sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def test_welcome(self):
        result = self.get("/welcome")
        assert self.get("/index/").data == result.data
        #self.assert_template_used(result, 'welcome.html')