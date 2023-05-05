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


    def test_add_country(self):
        # create a new country to add
        new_country = {
            "name": "Germany",
            "capital": "Berlin",
            "area": 357386,
        }
        
        # send a POST request to add the new country
        response = self.app.post('/countries', json=new_country)

        # check that the response status code is 201
        self.assertEqual(response.status_code, 201)

        # check that the response JSON contains the new country
        self.assertIn(new_country, app.json.loads(response.data))

        # check that the new country was added to the countries list
        self.assertIn(new_country, app.countries)

        # check that the new country has an id assigned by _find_next_id()
        self.assertEqual(new_country['id'], app._find_next_id())


    def test_add_country_invalid_request(self):
        # send a POST request with invalid data
        response = self.app.post('/countries', data='not a JSON request')

        # check that the response status code is 415
        self.assertEqual(response.status_code, 415)

        # check that the response JSON contains an error message
        expected_error = {"error": "Request must be JSON"}
        self.assertEqual(app.app.json.loads(response.data), expected_error)

        # check that the countries list was not modified
        self.assertEqual(len(app.countries), 3)
