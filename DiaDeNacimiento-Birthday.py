#El programa solicita al usuario su fecha de nacimiento y le dice que día de la semana fué. (For English follow the instructions below).

import datetime
import locale

# Establecer el idioma a español
locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')

while True:
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato DD MM AAAA: ")
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d %m %Y")
        break
    except ValueError:
        print("El formato ingresado es incorrecto, por favor ingresa tu fecha de nacimiento en formato DD MM AAAA")

dia_semana = fecha_nacimiento.strftime("%A")
print("Naciste un", dia_semana)

#The program asks the user for their date of birth and tells them what day of the week it was. It's configured for Spanish language, but you can switch it to English by adding a # to the beginning of each line before this and removing the # from all subsequent lines.

#import datetime

#while True:
#    fecha_nacimiento = input("Enter your date of birth in DD MM YYYY format: ")
#    try:
#        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d %m %Y")
#        break
#    except ValueError:
#        print("The entered format is incorrect, please enter your date of birth in DD MM YYYY format")

#dia_semana = fecha_nacimiento.strftime("%A")
#print("You were born on a", dia_semana)
