
import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()

connection.commit()

connection.close()