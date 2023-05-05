import datetime
import locale

# Establecer el idioma a español
locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')

fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato DD MM AAAA: ")
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d %m %Y")
dia_semana = fecha_nacimiento.strftime("%A")

print("Naciste un", dia_semana)
