import sqlite3
connection = sqlite3.connect('duke.db')
cursor = connection.cursor()

query = 'SELECT name, age FROM users WHERE age > ?'
age_limit = 30
cursor.execute(query, (age_limit,))
results = cursor.fetchall() 