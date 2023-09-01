#Exercise 17: Find words with both alphabets and numbers

#Write a program to find words with both alphabets and numbers from an input string.

#Given:
#str1 = "Emma25 is Data scientist50 and AI Expert"

#Expected Output:
#Emma25
#scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"

str1 = str1.split()

for i in str1:
    if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
        print(i)
    else: continue
