import requests
response = requests.get("api.openweathermap.org/data/2.5/weather?q=London")
print(response)


