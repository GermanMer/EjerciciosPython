#Exercise 4: Count the occurrence of each element from a list

#Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

#Given:
#sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

#Expected Output:
#Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

res_dict = {}

for i in sample_list:
    if i not in res_dict:
        res_dict[i] = 1
    else:
        res_dict[i] = res_dict[i] + 1

print('Printing count of each item', res_dict)
