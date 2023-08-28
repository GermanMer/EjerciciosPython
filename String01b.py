#Exercise 1B: Create a string made of the middle three characters

#Write a program to create a new string made of the middle three characters of an input string.

#Given:

#Case 1
#str1 = "JhonDipPeta"
#Output
#Dip

str1 = "JhonDipPeta"
print(str1[4:7])

#Case 2
#str2 = "JaSonAy"
#Output
#Son

str2 = "JaSonAy"
print(str2[2:5])

in_str = input('Entrer a word: ')
middel_l = in_str[int(len(in_str) / 2)]
first_l = in_str[int((len(in_str) / 2)-1)]
last_l = in_str[int((len(in_str) / 2)+1)]
new_str = first_l+middel_l+last_l
print(new_str)
