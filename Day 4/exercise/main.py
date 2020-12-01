from modules.cleanup import Cleanup
from weather import Weather
import requests, json

def get_data(city, country):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    city = city
    country = country
    full_path = f'{url}?q={city},{country}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
    j = ''
    try:
        res = requests.get(full_path)
        j = res.json()
    except Exception as err:
        print('Something went wrong. ', err)
    finally:
        return j

def 



if __name__ == '__main__':
    city = input('Enter a city ')
    country = input('Enter a country code (2-3 letters, like: hun, uk) ')
    cleaned = Cleanup.cleanup(city=city, country=country)
    print(cleaned)
    data = get_data(city=cleaned['city'], country=cleaned['country'])

    json_city = data['name']
    json_country = data['sys']['country']
    json_description = data['weather'][0]['description']
    json_temperature = data['main']['temp']
    json_temp_feels_like = data['main']['feels_like']
    json_wind_speed = data['wind']['speed']
    json_wind_direction = data['wind']['deg']
    #output = f'The weather in {json_city}, {json_country} is {json_description}. The temperature is {json_temperature}, it feels like {json_temp_feels_like}. Wind is {json_wind_speed} {json_wind_direction} deg.'
    #print(output)
    weather = Weather(json_city, json_country, json_description, json_temperature)
    print(weather)
    weather.change_temp()
    print(weather)
    weather.show_Kelvin_temp()