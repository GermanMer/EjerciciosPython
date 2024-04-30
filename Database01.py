#Exercise 1: Connect to your database server and print its version
import sqlite3
connection = sqlite3.connect('python_db.db')
cursor = connection.cursor()
cursor.execute("select sqlite_version();")
db_version = cursor.fetchone()
connection.close()
print("Database version:", db_version)
