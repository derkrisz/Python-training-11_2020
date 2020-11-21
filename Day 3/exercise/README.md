# Python Review Exercise 3

Classes, inheritance, modules, decorators, overrides and file input/output
(plus some nice print formatting)

We need a class to represent 'Weather' with properties for

- weather description which must be a non-empty string
- weather temperature which must be a floating point number
(You could use property decorators to do this)

The Weather class should also have a method 'changeTemp' which alters the original
temperature by a small random amount, e.g. from random inport randint
tempChange = randint(-5,5)
Override the __str__ so your Weather instances will print nicely

Also declare a data structure for 'location' with data members for 'city' and 'country'
(This could be a 'Location' class or just a simple dictionary)
Consider restricting 'country' to be any one of a set of 2 or 3 letter values
  e.g. countries = {'ie', 'uk', 'fr', 'aus', 'tw'}
Add 'location' as a property to the 'Weather' class, making sure it is an instance of

your 'Location' class or dictionary

Use separate modules to hold your class(es) and import them into a 'main.py' module
You should consider writing descriptive docstrings in each class and making use of
if __name__ == '__main__': to write immediate code to exercise each module as a unit

In the main module, create several weather instances with typical values and exercise

your code thoroughly

Write another class called 'HistoricalWeather' that inherits from 'Weather'
This should have a field for 'day' so you can store what day this report was made
Override the __eq__ method so Weather and HistoricalWeather instances can be compared
(You could also override __lt__, __gt__ etc. for these classes)

## Optional

In your 'Weather' class, write a method to show the temperature in Kelvin
( Kelvin = Celcius + 273 )
See if you can write a 'validator' function which you use to decorate fields
such as 'city' and 'description' to ensure they are non-empty strings
Decide on an approach to write a weather report to a text file. For example

- write a nicely formatted weather report, including city, country and description
- append to an ongoing weather_report.txt file
- consider adding a datetime stamp (import the datetime library to do this)
Write another module which can read in from this text file and present it nicely
