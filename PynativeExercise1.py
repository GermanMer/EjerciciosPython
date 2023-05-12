# Exercise 1: Calculate the multiplication and sum of two numbers.
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

primernumero = input('Ingrese el primer número: ')
segundonumero = input('Ingrese el segundo número: ')

if int(primernumero) * int(segundonumero) <= 1000:
    print('El resultado es', int(primernumero) * int(segundonumero))
else:
    print('El resultado es', int(primernumero) + int(segundonumero))
