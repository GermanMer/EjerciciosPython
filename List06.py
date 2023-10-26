#Exercise 6: Remove empty strings from the list of strings

#list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

#Expected output:
#["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res_list = []

for i in list1:
    if i != '':
        res_list.append(i)
    else: continue

print(res_list)
