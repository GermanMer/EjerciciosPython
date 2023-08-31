#Exercise 13: Split a string on hyphens

#Write a program to split a given string on hyphens and display each substring.

#Given:
#str1 = Emma-is-a-data-scientist

#Expected Output:
#Displaying each substring
#Emma
#is
#a
#data
#scientist

print('Displaying each substring')

str1 = 'Emma-is-a-data-scientist'

l = str1.split('-')

for i in l:
    print(i)
