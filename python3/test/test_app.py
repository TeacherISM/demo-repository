import sys
from src import app
from unittest import TestCase
import json
sys.path.append('../src')


class AppTest(TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hola, soy akemi")

    # test if the response is 200 for the welcome page
    def test_welcome(self):
        response = self.app.get('/welcome')
        self.assertEqual(response.status_code, 200)

    # test if the response is 200 for the countries page
    def test_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)

    # test countries get endpoint
    def test_countries_get(self):
        result = self.app.get('/countries')
        self.assertIn(b'Thailand', result.data)
        self.assertIn(b'Bangkok', result.data)
        self.assertIn(b'513120', result.data)
        self.assertIn(b'Australia', result.data)
        self.assertIn(b'Canberra', result.data)
        self.assertIn(b'7617930', result.data)
        self.assertIn(b'Egypt', result.data)
        self.assertIn(b'Cairo', result.data)
        self.assertIn(b'1010408', result.data)
        self.assertEqual(result.status_code, 200)

    # test countries post endpoint
    def test_countries_post(self):
        countries = [
            {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
            {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
            {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
        ]
        new_country = {"name": "Mexico",
                       "capital": "Mexico City", "area": 1964375}
        result = self.app.post('/countries', json=new_country)
        self.assertIn('id', json.loads(result.data))
        self.assertEqual(len(countries) + 1, len(json.loads(result.data)))

    # test invalid post endpoint
    def test_add_country_invalid_request(self):
        result = self.app.post(
            '/countries')
        self.assertEqual(result.status_code, 415)
        self.assertEqual(json.loads(result.data), {
                         "error": "Request must be JSON"})
