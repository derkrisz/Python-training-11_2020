from weather import Weather
import datetime

class HistoricalWeather(Weather):
    def __init__(self, description, temperature, location, date):
        super().__init__(description, temperature, location)
        self.__date = date

    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date

def dates_equal(func):
    def inner (*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return 'These historical values are equal'
        else:
            return 'These historical values are not equal'
    return inner

@dates_equal
def compare_dates(self, other):
    return self.date == other.date


if __name__ == '__main__':
    location1 = ('Budapest', 'HUN')
    date1 = datetime.datetime(2020, 10, 13)
    hist_weather1 = HistoricalWeather('Some place', 25, location1, date1)
    
    date2 = (1996, 8, 20)
    hist_weather2 = HistoricalWeather('A good place', 26, location1, date2)

    compared = compare_dates(hist_weather1, hist_weather2)
    print(compared)
    compared2 = compare_dates(hist_weather1, hist_weather1)
    print(compared2)
    