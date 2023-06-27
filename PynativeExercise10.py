#Exercise 10: Create a new list from a two list using the following condition: Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

#Given:
#list1 = [10, 20, 25, 30, 35]
#list2 = [40, 45, 60, 75, 90]

#Expected Output:
#result list: [25, 35, 40, 60, 90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = []

#impares_lista1
for i in list1:
    if i % 2 != 0:
        result_list.append(i)
    else: continue

#pares_lista2
for p in list2:
    if p % 2 == 0:
        result_list.append(p)
    else: continue

result_list.sort()

print('result list:', result_list)
