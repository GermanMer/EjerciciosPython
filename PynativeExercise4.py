#Exercise 4: Remove first n characters from a string
#Write a program to remove characters from a string starting from zero up to n and return a new string.

cadena = input("Please, enter a string:")
n = input("Please, enter number of characters to remove:")
n=int(n)
nuevacadena = cadena[n:]
print(nuevacadena)
