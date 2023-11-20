#Exercise 3: Subtract a week (7 days)  from a given date in Python

#Given:
#given_date = datetime(2020, 2, 25)

#Expected output:
#2020-02-18

from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)

res_date = given_date - timedelta(weeks=1)

print(res_date)
