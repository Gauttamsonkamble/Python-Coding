
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

# cursor.execute("""update students set course = ? where id = ? """,("java",1))

cursor.execute(""" update students set course = "Python" where id =2 """)

connection.commit()

connection.close()