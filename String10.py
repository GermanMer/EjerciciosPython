#Exercise 10: Write a program to count occurrences of all characters within a string

#Given:
#str1 = "Apple"

#Expected Outcome:
#{'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"

diccionario = {}

for i in str1:
    diccionario[i] = str1.count(i)

print(diccionario)
