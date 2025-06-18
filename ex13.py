import requests
import pytest
import json

class TestUserAgent:
    user_agents_list = [{
        "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "expected_values": {
            'platform': 'Mobile',
            'browser': 'No',
            'device': 'Android'
        }},
        {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "expected_values": {
            'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'
        }},
        {
        "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "expected_values": {
            'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'
        }},
        {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "expected_values": {
            'platform': 'Web', 'browser': 'Chrome', 'device': 'No'
        }},
        {
        "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "expected_values": {
            'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'
        }}

    ]

    @pytest.mark.parametrize('user_agent_value', user_agents_list)
    def test_user_agent_responce(self, user_agent_value):
        user_agent = user_agent_value['user_agent']
        responce = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"User-Agent":user_agent}
            )
        responce_json = json.loads(responce.text)
        actual_device = responce_json['device'] 
        actual_platform = responce_json['platform']
        actual_browser = responce_json['browser']

        expected_values = user_agent_value['expected_values']
        expected_device = expected_values['device']
        expected_platform = expected_values['platform']
        expected_browser = expected_values['browser']

        assert actual_device==expected_device, f"User agent: {user_agent}, device is not correct. Expected: {expected_device}. Actual: {actual_device}"
        assert actual_platform==expected_platform, f"User agent: {user_agent}, platform is not correct. Expected: {expected_platform}. Actual: {actual_platform}"
        assert actual_browser==expected_browser, f"User agent: {user_agent}, browser is not correct. Expected: {expected_browser}. Actual: {actual_browser}"