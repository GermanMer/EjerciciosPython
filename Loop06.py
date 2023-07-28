#Exercise 6: Count the total number of digits in a number
#Write a program to count the total number of digits in a number using a while loop.

#For example, the number is 75869, so the output should be 5.

number = input('Enter a number:')

number = int(number)

contador = 0

while number > 0:
    number = number // 10
    contador = contador + 1

print(contador)
