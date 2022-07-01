import requests
api_key = 'c684f2d26bdabc2f8187994ef4162f88'
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input('Enter a city name: ')
requests_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data['main']['temp'] - 273.15)
    print(temperature)
    print('Weather:', weather)
    print('Temperature:', temperature, 'celsius')


else:
    print("an error occured.")

