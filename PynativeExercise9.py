#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.

#A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

#Expected Output:
#original number 121
#Yes. given number is palindrome number
#original number 125
#No. given number is not palindrome number

while True:
    numero=input("Please, enter a number:")
    try:
        numero=int(numero)
        break
    except:
        print("That's not a number, please enter a number")

numero_invertido = str(numero)
numero_invertido = numero_invertido[::-1]
numero_invertido = int(numero_invertido)

if numero == numero_invertido:
    respuesta = 'Yes. given number is palindrome number'
else:
    respuesta = 'No. given number is not palindrome number'

print('original number', numero)
print(respuesta)
