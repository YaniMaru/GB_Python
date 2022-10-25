import sqlite3
db = sqlite3.connect('hw_Python/hw_08/db/base.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
               id INTEGER PRIMARY KEY autoincrement,
               last_name TEXT,
               first_name TEXT,
               position TEXT,
               salary INTEGER,
               bonus INTEGER
               )''')
