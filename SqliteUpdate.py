import sqlite3

conn = sqlite3.connect('mydatabase.db')

conn.execute("UPDATE stocks SET price = 53.00 WHERE symbol = 'RHAT' ")

conn.commit()

conn.close()