from app import app
from mock import MagicMock

import requests
import unittest
import json


class MyTestClass(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_root(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_temp(self):
        def get_stub(*args, **kwargs):
            response = requests.get.return_value
            with open(
                    'fixtures/api.worldweatheronline.com_london.json',
                    'r') as f:
                response.text = f.read()
                return response
        requests.get = MagicMock(side_effect=get_stub)

        result = self.app.get('/temp')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.data)
        assert 'temp' in data.keys()
        self.assertRegexpMatches(data['temp'], r'^[0-9]+$')


if __name__ == '__main__':
    unittest.main()
