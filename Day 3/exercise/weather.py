from random import randint
from location import Location

class Weather:
    def __init__(self, description, temperature, location):
        self.__description = description
        self.__temperature = temperature
        self.__location = location

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = description
   
    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, temperature):
        if not isinstance(temperature, float):
            self.__temperature = float(temperature)
        else:
            self.__temperature = temperature
    
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        if isinstance(location, Location):
            self.__location = location
        else:
            pass

    def change_temp(self):
        self.temperature = randint(-5, 30)

    def show_Kelvin_temp(self):
        print(f'{self.temperature + 273}')

    def __str__(self):
        return(f'The city is: {self.location.city} in {self.location.country}. Its description is: {self.description}, the temperature is {self.temperature}')


if __name__ == '__main__':
    l = Location('Dubai', 'ue')
    w = Weather('It\'s very warm here!', 30.5, l)
    print(w)
    w.change_temp()
    print(w)
