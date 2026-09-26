
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

cursor.execute("select * from students")

# rows = cursor.fetchone()

rows = cursor.fetchall()

# rows = cursor.fetchmany(2)

for row in rows:
    print(row)




connection.close()