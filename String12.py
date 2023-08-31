#Exercise 12: Find the last position of a given substring

#Write a program to find the last position of a substring “Emma” in a given string.

#Given:
#str1 = "Emma is a data scientist who knows Python. Emma works at google."

#Expected Output:
#Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."

sub_str = 'Emma'

print('Last occurrence of', sub_str, 'starts at index', str1.rfind(sub_str))
