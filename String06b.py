#Exercise 6: Create a mixed String using the following rules

#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

#Given:
#s1 = "Abc"
#s2 = "Xyz"

#Expected Output:
#AzbycX

s1 = "Abc"
s2 = "Xyz"

def mix_str(str1, str2):
    s3 = []
    count_str1 = 0
    count_str2 = -1
    str3 = str1 + str2
    for i in range(len(str3) // 2):
        s3.append(str3[count_str1])
        count_str1 = count_str1 + 1
        s3.append(str3[count_str2])
        count_str2 = count_str2 - 1
    print(''.join(s3))

mix_str(s1, s2)
