#Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set

#Given:
#first_set = {27, 43, 34}
#second_set = {34, 93, 22, 27, 43, 53, 48}

#Expected Output:
#First set is subset of second set - True
#Second set is subset of First set - False
#First set is Super set of second set - False
#Second set is Super set of First set - True
#First Set set()
#Second Set {48, 34, 53, 22, 27, 43, 93}

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print('First set is subset of second set -', first_set.issubset(second_set))
print('Second set is subset of First set -', second_set.issubset(first_set))
print('First set is Super set of second set -', first_set.issuperset(second_set))
print('Second set is Super set of First set - ', second_set.issuperset(first_set))
if first_set.issubset(second_set): first_set.clear()
print('First Set', first_set)
if second_set.issubset(first_set): second_set.clear()
print('Second Set', second_set)
