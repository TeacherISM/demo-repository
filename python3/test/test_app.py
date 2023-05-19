from unittest import TestCase
from src import app
import sys

sys.path.append('../src')


class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")


    def setUp(self) -> None:
        self.app = app.app.test_client()

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertIn('Welcome!', str(result.data))


    def test_get_countries(self):
        response = self.app.get('/countries')
        json_data = response.get_json()

        self.assertIsInstance(json_data, list)
        self.assertEqual(len(json_data), 3)

        expected_country = {
            "area": 513120,
            "capital": "Bangkok",
            "id": 1,
            "name": "Thailand"
        }
        self.assertDictEqual(json_data[0], expected_country)

        expected_keys = {'id', 'name', 'capital', 'area'}
        for country in json_data:
            self.assertSetEqual(set(country.keys()), expected_keys)

    def test_find_next_id(self):
        next_id = app._find_next_id()
        self.assertEqual(next_id, 4)
