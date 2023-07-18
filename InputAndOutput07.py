#Exercise 7: Accept any three string from one input() call.
#Write a program to take three names as input from a user in the single input() function call.

#Expected Output:
#Enter three string Emma Jessa Kelly
#Name1: Emma
#Name2: Jessa
#Name3: Kelly

contador = 0
cadenas = input('Enter three string:')
separadas = cadenas.split()
for i in separadas:
    contador = contador + 1
    print('Name' + str(contador) + ':', i)
