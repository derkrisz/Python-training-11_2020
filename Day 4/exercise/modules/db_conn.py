import sqlite3
import datetime

def create_db(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    statement = '''CREATE TABLE IF NOT EXISTS weather 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
city VARCHAR,
country VARCHAR,
description VARCHAR, 
temperature FLOAT,
timestamp INT)'''

    cursor.execute(statement)
    cursor.close()
    conn.close()

def add_weather_to_db(db, weather):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    data = (weather.city, weather.country, weather.description, weather.temperature, datetime.datetime.now())

    cursor.execute('INSERT INTO weather (city,country,description,temperature,timestamp) VALUES(?,?,?,?,?)', data)
    conn.commit()
    cursor.close()
    conn.close()

def retrieve_weathers(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute('SELECT * from weather')
    rows = cursor.fetchall()
    print(rows)




