#Exercise 5: Find the day of the week of a given date

#Given:
#given_date = datetime(2020, 7, 26)

#Expected output:
#Sunday

import calendar #Usando el módulo calendario
from datetime import datetime

given_date = datetime(2020, 7, 26)

weekday = calendar.day_name[given_date.weekday()]

print(weekday)
