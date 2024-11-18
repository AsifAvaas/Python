import requests

API_KEY="27130f814bd1225b15be8abd2ef73930"
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def toCel(n):
    return 5/9*(n-32)

def weatherInfo(city):
    weather_data=requests.get(f"{BASE_URL}?q={city}&units=imperial&APPID={API_KEY}")
    # print(weather_data.json())
    if weather_data.json()['cod']!=200:
        print("Invalid city Name.")
        return
    # print(weather_data.json())
    weather=weather_data.json()['weather'][0]['main']
    temp=weather_data.json()['main']['temp']
    temp=(toCel(temp))
    feelslike=weather_data.json()['main']['feels_like']
    feelslike=round(toCel(feelslike))
    print(f"The weather is {weather}")
    print(f"Temperature: {temp}, feels like: {feelslike}")
    print("")
    

while True:
    
    choice=input("Press 1 to see the weather, any other key to exit: ")
    if choice!='1':
        break

    city=input("Enter a city name: ")
    weatherInfo(city)
