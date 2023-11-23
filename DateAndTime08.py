#Exercise 8: Convert the following datetime into a string

#Given:
#given_date = datetime(2020, 2, 25)

#Expected output:
#"2020-02-25 00:00:00"

from datetime import datetime

given_date = datetime(2020, 2, 25)

str_time = given_date.strftime("%Y-%m-%d %H:%M:%S")

print(str_time)
