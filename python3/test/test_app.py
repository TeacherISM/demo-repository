import sys
import unittest
from unittest import TestCase

sys.path.append('../src')
from src import app

class AppTest(TestCase):
    def test_home(self):
        result = app.home()
        self.assertEqual(result, "Hello, World!")
    
    def test_welcome(self):
        result = app.welcome()
        # get contents of templates/welcome.html
        with open("templates/welcome.html") as f:
            contents = f.read()
        self.assertEqual(result, contents)

    
    def test_get_countries(self):
        countries_test = [
            {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
            {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
            {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
        ]
        result = app.get_countries()
        #convert result to a dictionary
        result = result.get_json()
        self.assertDictContainsSubset(result,countries_test)
    
    def test_add_country(self):
        test_country= {"id": app._find_next_id(), "name": "country", "capital": "capital", "area": 123456}
        result = app.add_country()
        self.assertEqual(result,test_country)

