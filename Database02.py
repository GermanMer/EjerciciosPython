#Exercise 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id
import sqlite3

connection = sqlite3.connect('python_db.db')
cursor = connection.cursor()
select_query_h = """select * from Hospital where Hospital_Id = 2"""
cursor.execute(select_query_h)
records = cursor.fetchall()
print("Hospital Records")
for row in records:
    print("Hospital Id:", row[0], )
    print("Hospital Name:", row[1])
    print("Bed Count:", row[2])

connection.close()


connection = sqlite3.connect('python_db.db')
cursor = connection.cursor()
select_query_d = """select * from Doctor where Doctor_Id = 105"""
cursor.execute(select_query_d)
records = cursor.fetchall()
print("Doctor Records")
for row in records:
    print("Doctor Id:", row[0], )
    print("Doctor Name:", row[1])
    print("Hospital Id:", row[2])
    print("Joining Date:", row[3])
    print("Speciality:", row[4])
    print("Salary", row[5])
    print("Experience", row[6])

connection.close()
