from app import app
import unittest
import json
import config


def get_value_from_response(response):
    if response is None:
        return ''
    data = json.loads(response.data)
    size = len(data)
    if size == 1:
        result = list(data.values())[0]
    else:
        result = [value for value in data.values()]
    return result


def get_key_from_response(response):
    decoded = get_value_from_response(response)
    size = len(decoded)
    return decoded[1:-2] if size == 6 else decoded


class FlaskKeys(unittest.TestCase):

    def setUp(self):
        """
        Creates a test client.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_generation(self):
        result = self.app.post('/acquire_key')
        decoded = get_key_from_response(result)
        self.assertIsNotNone(decoded)
        self.assertTrue(len(decoded) == 4)
        return decoded

    def test_status(self):
        key_code = self.test_generation()
        updated = self.app.get('/keys/{}'.format(key_code))
        decoded = get_value_from_response(updated)
        self.assertIsNotNone(decoded)
        self.assertTrue(decoded.get(config.KEY_CODE) == key_code)
        self.assertTrue(decoded.get(config.KEY_ISSUED))
        self.assertFalse(decoded.get(config.KEY_EXPIRED))

    def test_count(self):
        result = self.app.get('/keys_count')
        self.assertTrue(str(get_value_from_response(result)).isdigit())

    def test_expire(self):
        key_code = self.test_generation()
        self.app.put('/keys/{}'.format(key_code))
        updated = self.app.get('/keys/{}'.format(key_code))
        updated = get_value_from_response(updated)
        self.assertTrue(updated.get(config.KEY_CODE) == key_code)
        self.assertTrue(updated.get(config.KEY_ISSUED))
        self.assertTrue(updated.get(config.KEY_EXPIRED))
