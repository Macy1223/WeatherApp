from readapi_key import readapi_key
import requests

api_key = readapi_key("api_key.txt")

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=warsaw&appid={api_key.strip()}")

temp = response.json()["main"]["temp"]
print(temp)
