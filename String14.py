#Exercise 14: Remove empty strings from a list of strings

#Given:
#str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

#Expected Output:
#Original list of sting
#['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

#After removing empty strings
#['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print('Original list of sting')
print(str_list)

for i in str_list:
    if i == "":
        str_list.remove(i)
    elif i == None:
        str_list.remove(i)

print('')
print('After removing empty strings')
print(str_list)
