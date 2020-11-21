import sqlite3

# open connection to db
conn = sqlite3.connect('enterprise.db') #create if not exist
curs = conn.cursor()

# statement = '''CREATE TABLE IF NOT EXISTS zoo 
# (creatures VARCHAR(64) PRIMARY KEY, 
# count INT, 
# damages FLOAT)'''
# curs.execute(statement)

# st = 'INSERT INTO zoo VALUES("duck", 5, 0.0)'
# curs.execute(st)
# st = 'INSERT INTO zoo (creatures, count, damages) VALUES(?, ?, ?)'
# curs.execute(st, ('weasel', 1, 2000.00))
# curs.execute(st, ('bear', 2, 1000.00))


# conn.commit()

st = 'SELECT * FROM zoo'
curs.execute(st)
rows = curs.fetchall()
print(rows)



# remember to clean up by closing connections and dropping cursors
curs.close()
conn.close()