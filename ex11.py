import requests
class TestCookie:
    def test_cookie_included(self):
        responce = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_name = 'HomeWork'
        print(responce.cookies.get_dict())
        assert cookie_name in responce.cookies, f"The {cookie_name} is not in the list of cookies"