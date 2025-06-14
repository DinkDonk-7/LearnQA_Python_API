import requests

methodTypes = ["POST", "GET", "PUT", "DELETE"]
requestMethodsArray = [requests.get, requests.post, requests.delete, requests.put]

responceWithNoParams = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Если без параметров: {responceWithNoParams.text}, {responceWithNoParams.status_code}")

responceWithNotListedMethod = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Если метод не из списка: {responceWithNotListedMethod.text}, {responceWithNotListedMethod.status_code}")

responceWithCorrectParams = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(f"Если корректные параметры: {responceWithCorrectParams.text}, {responceWithCorrectParams.status_code}")

print("Перебор начинается тут:")

for method in methodTypes:
    for requestMethod in requestMethodsArray:
        requestMethodName = requestMethod.__name__
        if requestMethodName=="get":
            responce = requestMethod("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":method})
            if method.lower()==requestMethodName and responce.text[0]=="W":
                print(f"Метод:{requestMethodName} Параметры:{method} ответ не ок")
            if method.lower()!=requestMethodName and responce.text[0]=="{":
                print(f"Метод:{requestMethodName} Параметры:{method} ответ ок")
        else:
            responce = requestMethod("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":method})
            if method.lower()==requestMethodName and responce.text[0]=="W":
                print(f"Метод:{requestMethodName} Параметры:{method} ответ не ок")
            if method.lower()!=requestMethodName and responce.text[0]=="{":
                print(f"Метод:{requestMethodName} Параметры:{method} ответ ок")