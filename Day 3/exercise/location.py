from modules.validation import validate_string, validate_country

class Location:
    def __init__(self, city, country):
        self.__city = city
        self.__country = country
    
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
        self.__country = self.country_validation(country)
    
    @validate_string
    def validate_city(self, city):
        return city

    @validate_country
    def country_validation(self, country):
        return country.lower().strip()

if __name__ == '__main__':
    l1 = Location('Budapest', 'HUN')
    l1.city = 'Oregon'
    print(l1.city, l1.country)
    l1.country = 'KW'
    print(l1.country)