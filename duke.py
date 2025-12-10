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