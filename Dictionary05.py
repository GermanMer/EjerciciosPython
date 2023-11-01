#Exercise 5: Create a dictionary by extracting the keys from a given dictionary

#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

#Given dictionary:
#sample_dict = {
#    "name": "Kelly",
#    "age": 25,
#    "salary": 8000,
#    "city": "New york"}

# Keys to extract
#keys = ["name", "salary"]

#Expected output:
#{'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

res_dict = {}

for i in sample_dict:
    if i == 'name':
        res_dict['name'] = sample_dict['name']
    elif i == 'salary':
        res_dict['salary'] = sample_dict['salary']
    else: continue

print(res_dict)
