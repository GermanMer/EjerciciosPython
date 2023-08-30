#Exercise 9: Calculate the sum and average of the digits present in a string

#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

#Given:
#str1 = "PYnative29@#8496"

#Expected Outcome:
#Sum is: 38 Average is  6.333333333333333

str1 = "PYnative29@#8496"

lista = []

for i in str1:
    if i.isdigit():
        lista.append(int(i))
    else: continue

print('Sum is:', sum(lista), 'Average is', (sum(lista)/len(lista)))
