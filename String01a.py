#Exercise 1A: Create a string made of the first, middle and last character

#Write a program to create a new string made of an input string’s first, middle, and last character.

#Given:
#str1 = "James"

#Expected Output:
#Jms

str1 = "James"
n_str = str1[::2]
print(n_str)


in_str = input('Entrer a word: ')
first_l = in_str[0]
middel_l = in_str[int(len(in_str) / 2)]
last_l = in_str[-1]
new_str = first_l+middel_l+last_l
print(new_str)
