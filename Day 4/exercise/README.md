# Review Exercise 4: Weather and Databases

Write modules to implement a weather service
You can use the following end-point to get the current weather as JSON:
<http://api.openweathermap.org/data/2.5/weather?q=edinburgh,uk&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1>

In your main module, ask the user to input a city and a country (edinburgh and uk above) and inject them into the url
Validate that they entered a non-empty string for city and 2 or 3 letters for (permitted) country

Make a 'get' request to openweathermap and convert the response from JSON into a Python structure using response.json()
(or just read in the json from the text file given above, regardless of user-entered values)
Print the weather description, temperature, wind-speed and wind-direction

If you have a 'weather' class from yesterday, populate it with the returned weather data

Initialise a weather database with a table and some weather data members (pick some, don't use them all)
Use an auto-increment ID as the primary key, e.g.
 CREATE TABLE weather( id int primary key, desc varchar(64), temperature decimal .....)
Also include fields for 'city' and 'country'
For every weather report put the results into the database, optionally with a date-time stamp
Provide a way to read back all the weather reports

## Optional

Use pickle to serialize/deserialize the weather report structure and persist into a (retrievable) text file
Write tests (even before writing code?) to exercise some of the functions and/or classes in your modules
For example, check edge-cases for validation, check for exceptions, check for positive outcomes and data-types
You may use doctest and/or unittest as you choose
