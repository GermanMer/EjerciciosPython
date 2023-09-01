#Exercise 16: Removal all characters from a string except integers

#Given:
#str1 = 'I am 25 years and 10 months old'

#Expected Output:
#2510

str1 = 'I am 25 years and 10 months old'

str2 = []

for i in str1:
    if i.isdigit():
        str2.append(i)
    else: continue

print(''.join(str2))
