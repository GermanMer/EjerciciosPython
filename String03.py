#Exercise 3: Create a new string made of the first, middle, and last characters of each input string

#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

#Given:
#s1 = "America"
#s2 = "Japan"

#Expected Output:
#AJrpan

s1 = "America"
s2 = "Japan"

s1a = s1[0]
s1b = s1[len(s1) // 2]
s1c = s1[-1]

s2a = s2[0]
s2b = s2[len(s2) // 2]
s2c = s2[-1]

s3 = s1a+s2a+s1b+s2b+s1c+s2c
print(s3)
