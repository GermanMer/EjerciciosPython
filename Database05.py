#Exercise 5: Update doctor experience in years
#The value of the experience column for each doctor is null. Implement the functionality to update the experience of a given doctor in years.
import sqlite3
import datetime
from dateutil.relativedelta import relativedelta

def get_connection():
    connection = sqlite3.connect('python_db.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def update_doctor_experience(doctor_id): # Update Doctor Experience in Years
    try:
        connection = get_connection() # Get joining date
        cursor = connection.cursor()
        select_query = """select Joining_Date from Doctor where Doctor_Id = ?"""
        cursor.execute(select_query, (doctor_id,))
        joining_date = cursor.fetchone()
        joining_year = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d') # Calculate Experience
        today_date = datetime.datetime.now()
        experience_years = relativedelta(today_date, joining_year).years
        connection = get_connection() # Update doctor's Experience
        cursor = connection.cursor()
        sql_select_query = """update Doctor set Experience = ? where Doctor_Id = ?"""
        cursor.execute(sql_select_query, (experience_years, doctor_id))
        connection.commit()
        print("Doctor Id:", doctor_id, " Experience updated to ", experience_years, " years")
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Error while getting doctor's data", error)

update_doctor_experience(101)
