#Exercise 4: Get a list of doctors from a given hospital
#Note: Implement the functionality to fetch all the doctors as per the given Hospital Id. You must display the hospital name of a doctor.
import sqlite3

def get_connection():
    connection = sqlite3.connect('python_db.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_hospital_name(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        hospital_name_query = """select * from Hospital where Hospital_Id = ?"""
        cursor.execute(hospital_name_query, (hospital_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1]
    except (Exception, sqlite3.Error) as error:
        print("Error while getting data", error)

def get_doctors(hospital_id): #Fetch All doctors within given Hospital
    try:
        hospital_name = get_hospital_name(hospital_id)
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Doctor where Hospital_Id = ?"""
        cursor.execute(select_query, (hospital_id,))
        records = cursor.fetchall()
        print("Printing doctors where Hospital is", hospital_name, "\n")
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

get_doctors(2)
