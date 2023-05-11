#El programa solicita al usuario su fecha de nacimiento y le dice que día de la semana fué.
#The program asks the user for their date of birth and tells them what day of the week it was.

import datetime
import locale

idioma = input("Para idioma español, escriba español. For english, write english: ")

if idioma.lower() == "español":
    # Establecer el idioma a español
    locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')
    msg_ingreso_fecha = "Ingresa tu fecha de nacimiento en formato DD MM AAAA: "
    msg_formato_incorrecto = "El formato ingresado es incorrecto, por favor ingresa tu fecha de nacimiento en formato DD MM AAAA"
    msg_naciste = "Naciste un"
elif idioma.lower() == "english":
    # Establecer el idioma a inglés
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
    msg_ingreso_fecha = "Enter your date of birth in DD MM YYYY format: "
    msg_formato_incorrecto = "The entered format is incorrect, please enter your date of birth in DD MM YYYY format"
    msg_naciste = "You were born on a"
else:
    print("Opción de idioma no válida. Se establecerá el idioma en español por defecto.\nInvalid language option. The language will be set to Spanish by default.")
    # Establecer el idioma a español
    locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')
    msg_ingreso_fecha = "Ingresa tu fecha de nacimiento en formato DD MM AAAA: "
    msg_formato_incorrecto = "El formato ingresado es incorrecto, por favor ingresa tu fecha de nacimiento en formato DD MM AAAA"
    msg_naciste = "Naciste un"

while True:
    fecha_nacimiento = input(msg_ingreso_fecha)
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d %m %Y")
        break
    except ValueError:
        print(msg_formato_incorrecto)

dia_semana = fecha_nacimiento.strftime("%A")
print(msg_naciste, dia_semana)
