#Exercise 2: Concatenate two lists index-wise

#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

#Given:
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]

#Expected output:
#['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

tuples = list(zip(list1, list2))

list3 = []

for i in tuples:
    j = i[0] + i[1]
    list3.append(j)

print(list3)
