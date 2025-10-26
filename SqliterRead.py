import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.execute("SELECT * FROM stocks")

for row in cursor:
    print(row)

conn.close()