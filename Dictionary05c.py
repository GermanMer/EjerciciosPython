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

keys = ["name", "salary"]

res_dict = {}

for k in keys:
    res_dict.update({k: sample_dict[k]}) # Update() method

print(res_dict)
