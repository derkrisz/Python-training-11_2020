class Location:
    def __init__(self, city, country):
        self.__city = city
        self.__country = country
    
    @property
    def city(self):
        return self.__city
    @city.setter
    def description(self, city):
        if isinstance(city, str) and city:
            self.__city = city
        else:
            pass

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country):
        if len(country) > 3:
            print('Use a country code for specifying the country, e.g. uk, fr, aus, tw')
        else:
            self.__country = country