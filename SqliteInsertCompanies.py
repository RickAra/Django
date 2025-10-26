import sqlite3


conn = sqlite3.connect('mydatabase.db')

conn.execute('''CREATE TABLE companies (symbol text, name text, sector text)''')

conn.execute("INSERT INTO companies VALUES ('RHAT', 'Red Hat Inc.', 'Software')")
conn.execute("INSERT INTO companies VALUES ('IBM', 'Int. Bus. Mach. Corp.', 'Tecnology')")
conn.execute("INSERT INTO companies VALUES ('AAPL', 'Aple Inc.', 'Tecnology')")

conn.commit()

conn.close()