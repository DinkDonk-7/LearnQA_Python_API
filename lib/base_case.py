import json.decoder
from datetime import datetime

from requests import Response

class BaseCase:
    def get_cookie (self, responce: Response, cookie_name):
        assert cookie_name in responce.cookies, f"Cannot find cokie with name {cookie_name} in the last responce"
        return responce.cookies[cookie_name]

    def get_header (self, responce: Response, headers_name):
        assert headers_name in responce.headers, f"Cannot find header with the name {headers_name} in the last responce"
        return responce.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }