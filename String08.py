#Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

#Write a program to find all occurrences of “USA” in a given string ignoring the case.

#Given:
#str1 = "Welcome to USA. usa awesome, isn't it?"

#Expected Outcome:
#The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"
s_str1 = "USA"

def find_substring(str, sub_str):
    l_str = str.lower()
    l_sub_str = sub_str.lower()
    cantidad = l_str.count(l_sub_str)
    print('The', s_str1, 'count is:', cantidad)

find_substring(str1, s_str1)
