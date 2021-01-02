from readapi_key import readapi_key
import requests
from Kalkulator import kel_to_cel

api_key = readapi_key("api_key.txt")

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=warsaw&appid={api_key.strip()}")

temp = response.json()["main"]["temp"]
feel_temperature = response.json()["main"]["feels_like"]

print(kel_to_cel(temp))
print(kel_to_cel(feel_temperature))
