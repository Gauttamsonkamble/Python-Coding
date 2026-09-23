
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

name = input("Enter name : ")
age = int(input("Enter age : "))
course = input("Enter course : ")


cursor.execute("""insert into students(name,age,course) values(?,?,?)""",(name,age,course) )

connection.commit()

connection.close()