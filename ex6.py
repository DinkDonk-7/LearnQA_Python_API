import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
numberOfRedirests = len(response.history)
finalRequest = response.history[numberOfRedirests-1]
print(numberOfRedirests)
print(finalRequest.url)