#Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

#Given:
#sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

#Expected Outcome:
#unique items [87, 45, 41, 65, 94, 99]
#tuple (87, 45, 41, 65, 94, 99)
#min: 41
#max: 99

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_items = []

for i in sample_list:
    if i not in unique_items:
        unique_items.append(i)
    else: continue
print('unique items', unique_items)

tuple_items = tuple(unique_items)
print('tuple', tuple_items)

print('min:', min(tuple_items))

print('max:', max(tuple_items))
