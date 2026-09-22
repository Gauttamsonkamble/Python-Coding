
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

cursor.execute("""insert into students (name , age , course) 
values("Rahul",20,"Python")""")

connection.commit()

connection.close()