#Exercise 2: Append new string in the middle of a given string

#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

#Given:
#s1 = "Ault"
#s2 = "Kelly"

#Expected Output:
#AuKellylt

s1 = "Ault"
s2 = "Kelly"

m_s1 = len(s1) // 2
s1a = s1[:m_s1]
s1b = s1[m_s1:]

s3 = s1a+s2+s1b
print(s3)
