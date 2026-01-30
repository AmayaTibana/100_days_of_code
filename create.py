import sqlite3

connection = sqlite3.connect('sample.db')

table = 'CREATE TABLE IF NOT EXISTS people(id integer primary key, name TEXT, surname TEXT)'

cursor = connection.cursor()
cursor.execute(table)
connection.commit()
