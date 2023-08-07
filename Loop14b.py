#Exercise 14: Reverse a given integer number

#Given:
#76542

#Expected output:
#24567

#This is an alternative way to get the result; it does not use a loop, but it is much simpler.
#Esta es una manera alternativa de obtener el resultado, no usa un blucle pero es mucho mas simple.

number = 76542
number = str(number)
print(number[: : -1])

#If you need the result as an integer, you can always typecasting it as int()
#Si necesita el resultado como un número entero, puede formatearlo como int()
