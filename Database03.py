#Exercise 3: Get the list Of doctors as per the given specialty and salary
import sqlite3

def get_connection():
    connection = sqlite3.connect('python_db.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_specialist_doctors_list(speciality, salary): #Fetch doctor's details as per Speciality and Salary
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Speciality = ? and Salary > ?"""
        cursor.execute(select_query, (speciality, salary))
        records = cursor.fetchall()
        print("Printing doctors whose specialty is", speciality, "and salary greater than", salary, "\n")
        for row in records:
            print("Doctor Id:", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)

get_specialist_doctors_list("Garnacologist", 30000)
