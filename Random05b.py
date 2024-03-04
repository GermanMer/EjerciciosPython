#Exercise 5: Generate random String of length 5
#Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.

import random
import string

letters = string.ascii_letters
result_str = ''.join(random.choice(letters) for i in range(5))
print(result_str)
