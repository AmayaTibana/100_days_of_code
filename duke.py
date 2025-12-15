# Exercise 1: Variables and Data Types

# 1. Create variables
name = "Carlos"         # string
age = 29                # integer
height = 1.75           # float
is_student = True       # boolean

# 2. Print descriptive sentences
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} meters")
print(f"I am a student: {is_student}")

# 3. Print the type of each variable
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

import csv
import sqlite3

# Input CSV file
input_file = "raw_data.csv"

# SQLite database
conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Create table
create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
"""
cur.execute(create_table_sql)
conn.commit()

# Read CSV and insert into database
with open(input_file, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Basic data cleaning
        name = row['name'].strip().title()
        age = int(row['age'])
        email = row['email'].strip().lower()

        cur.execute(
            "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
            (name, age, email)
        )

conn.commit()
conn.close()

print("CSV data loaded into SQLite database successfully!")
