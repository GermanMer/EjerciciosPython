#Exercise 4: Initialize dictionary with default values

#In Python, we can initialize the keys with the same values.

#Given:
#employees = ['Kelly', 'Emma']
#defaults = {"designation": 'Developer', "salary": 8000}

#Expected output:
#{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Crear un diccionario que tenga como claves los items de la lista employees y como valores los items del ciccionario dafaults
resultado = dict.fromkeys(employees, defaults)

print(resultado)
