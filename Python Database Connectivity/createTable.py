
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

cursor.execute("""create table if not exists students(id integer primary key, name text , age integer, course text) """)

connection.commit()

connection.close()