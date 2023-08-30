#Exercise 7: String characters balance Test

#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

#Given:

#Case 1:
#s1 = "Yn"
#s2 = "PYnative"
#xpected Output:
#True

#Case 2:
#s3 = "Ynf"
#s4 = "PYnative"
#Expected Output:
#False

s1 = "Yn"
s2 = "PYnative"

s3 = "Ynf"
s4 = "PYnative"

def balance_test(str1, str2):
    for i in str1:
        if i not in str2:
            break
        else: continue
    print(i in str2)

balance_test(s1, s2)

balance_test(s3, s4)
