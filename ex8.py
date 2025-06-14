import requests
import time

responceCreate = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
seconds = responceCreate.json()['seconds']
token = responceCreate.json()['token']
print(f"{token}, {seconds}")

responceCheck = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
if(responceCheck.json()['status']!="Job is NOT ready"):
    print("Ответ сервера не совпадает с ожидаемым")

time.sleep(seconds)
responceCheck = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
if(responceCheck.json()['status']!="Job is ready"):
    print("Ответ сервера не совпадает с ожидаемым, поле статуса")
if "result" not in responceCheck.json():
    print("Ответ сервера не совпадает с ожидаемым, нет поля результата")