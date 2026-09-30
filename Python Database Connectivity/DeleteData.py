
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

# cursor.execute("delete from students where id = ?",(1,))

cursor.execute("delete from students where id = 2")

connection.commit()

print("Students Deleted Succussfully")

connection.close()