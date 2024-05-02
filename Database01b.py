#Exercise 1: Connect to your database server and print its version
import sqlite3

def get_connection():
    connection = sqlite3.connect('python_db.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("You are connected to SQLite version: ", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()
