import sqlite3

conn = sqlite3.connect('mydatabase.db')

conn.execute("INSERT INTO stocks VALUES ('2004-09-29', 'BUY', 'RHAT',100, 35.14)")
conn.execute("INSERT INTO stocks VALUES ('2024-03-28', 'BUY', 'IBM', 1000, 45.00)")
conn.execute("INSERT INTO stocks VALUES ('2024-04-06', 'SELL', 'IBM', 500, 53.00)")

conn.commit()

conn.close()