import requests
class TestHeader:
    def test_header_included(self):
        responce = requests.get("https://playground.learnqa.ru/api/homework_header")
        header_name = 'x-secret-homework-header'
        print(responce.headers)
        assert header_name in responce.headers, f"The {header_name} is not in the list of headers"