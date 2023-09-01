#Exercise 15: Remove special symbols / punctuation from a string

#Given:
#str1 = "/*Jon is @developer & musician"

#Expected Output:
#"Jon is developer musician"

str1 = "/*Jon is @developer & musician"

import string

clean_str = str1.translate(str.maketrans('', '', string.punctuation))

print(clean_str)
