#Exercise 4: Print a date in a the following format
#Day_name  Day_number  Month_name  Year

#Given:
#given_date = datetime(2020, 2, 25)

#Expected output:
#Tuesday 25 February 2020

from datetime import datetime

given_date = datetime(2020, 2, 25)

conv_date = given_date.strftime("%A %d %B %Y")

print(conv_date)

#Ojo, el resultado ya no será un objeto datetime sino una cadena, porque strftime( ) lo convierte a cadena
#>>> type(given_date)
#<class 'datetime.datetime'>
#>>> type(conv_date)
#<class 'str'>
