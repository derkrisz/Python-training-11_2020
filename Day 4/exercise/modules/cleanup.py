class Cleanup:

    @staticmethod
    def cleanup(**kwargs):
        city = ''
        try:
            city = kwargs['city'].lower().strip()
            if not city or not isinstance(city, str):
                print('You need to pick a city. Defaulting to Edinburgh')
                city = 'edinburgh'
        except AttributeError as err:
            print(err)

        country = ''    
        try:
            country = kwargs['country'].lower().strip()
            if not isinstance(country, str) or len(country) not in range (1, 4):
                print('You need to pick a country code (2 or 3 letters, e.g. hun, uk). Defaulting to UK')
                country = 'uk'
        except AttributeError as err:
            print (err)
        return {'city': city, 'country': country}

    def __init__(self):
        pass

if __name__ == '__main__':
    result = Cleanup.cleanup(city='budapest', country='hun')
    print('result1: ', result)