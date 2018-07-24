import unittest

from hotels_api import get_hotels_info


class TestApi(unittest.TestCase):
    response = get_hotels_info("Екатеринбург")

    def test_status_code_with_correct_city(self):
        response_status = self.response.status_code
        self.assertEqual(response_status, 200)

    def test_no_errors_with_correct_city(self):
        response_body = self.response.json()
        self.assertIsNone(response_body['error'])
        self.assertIsNotNone(response_body['result'])

    def test_country_in_result(self):
        response_body = self.response.json()
        response_find_result = response_body['result']
        for element in response_find_result:
            self.assertIsNotNone(element['country'])

    def test_name_ascii_in_result(self):
        response_body = self.response.json()
        response_find_result = response_body['result']
        for element in response_find_result:
            self.assertIsNotNone(element['name_ascii'])

    def test_type_in_result(self):
        response_body = self.response.json()
        response_find_result = response_body['result']
        for element in response_find_result:
            self.assertIsNotNone(element['type'])
