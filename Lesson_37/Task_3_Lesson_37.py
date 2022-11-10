import requests
import json

API_Key = "20cf2c1c6dfe0c928d432ce25eba3ce2"

try:

    city_name = input('Enter your city name: ')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric&lang=ua"

    response = requests.get(url)

    data = response.json()

    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    print('wind speed:', data['wind']['speed'])
except Exception as e:
    print('FATAL ERROR')
    pass
