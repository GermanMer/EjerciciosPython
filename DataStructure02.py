#Exercise 2: Remove and add item in a list

#Write a program to remove the item present at inlist1.append(n)dex 4 and add it to the 2nd position and at the end of the list.

#Given:
#list1 = [34, 54, 67, 89, 11, 43, 94]

#Expected Output:
#List After removing element at index 4  [34, 54, 67, 89, 43, 94]
#List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
#List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

list1 = [34, 54, 67, 89, 11, 43, 94]

n = list1.pop(4)
print('List After removing element at index 4', list1)

list1.insert(2, n)
print('List after Adding element at index 2', list1)

list1.append(n)
print('List after Adding element at last', list1)
