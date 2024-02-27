#Exercise 5: Generate random String of length 5
#Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.

import random
import string

def get_random_string(length):
    letters = string.ascii_letters # choose from all lowercase and uppercase letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(5)
