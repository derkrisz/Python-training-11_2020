from weather import Weather

if __name__ == '__main__':
    l = ('Budapest', 'hun')
    weather = Weather('home country', 20.0, l)
    print(weather)
    weather.change_temp()
    print(weather)
    weather.country = 'HUN'
    print(weather)
    weather.temperature = 12
    print(weather)
    weather.show_Kelvin_temp()

