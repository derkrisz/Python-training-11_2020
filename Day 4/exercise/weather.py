from random import randint
from modules.validation import validate_string, validate_country

class Weather:
    def __init__(self, city, country, description, temperature):
        self.__city = city
        self.__country = country
        self.__description = description
        self.__temperature = temperature

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = self.validate_city(city)

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = self.validate_country(country)

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = self.validate_description(description)
   
    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, temperature):
        if not isinstance(temperature, float):
            self.__temperature = float(temperature)
        else:
            self.__temperature = temperature

    @validate_country
    def validate_country(self, country):
        return country

    @validate_string
    def validate_description(self, description):
        return description

    @validate_string
    def validate_city(self, city):
        return city

    def change_temp(self):
        self.temperature = randint(-5, 30)

    def show_Kelvin_temp(self):
        print(f'Kelvin temp in {self.city} is {self.temperature + 273}')

    def __str__(self):
        return(f'The city is: {self.city} in {self.country}. Its description is: {self.description}, the temperature is {self.temperature}')
