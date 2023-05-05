import sys
from src import app
from unittest import TestCase
sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")

    def test_welcome(self):
        result = app.welcome()
        self.assertEqual(result, "Welcome to Flask")

    def find_next_id(self):
        result = app._find_next_id()
        self.assertEqual(result, 4)

    def test_get_countries(self):
        result = app.get_countries()
        self.assertEqual(result, app.jsonify(app.countries))

    def test_add_country(self):
        result = app.add_country()
        self.assertEqual(result, app.country, 201)

    # def test_add_country_error(self):

        