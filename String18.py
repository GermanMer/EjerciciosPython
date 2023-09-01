#Exercise 18: Replace each special symbol with # in the following string

#Given:
#str1 = '/*Jon is @developer & musician!!'

#Expected Output:
##Jon is #developer # musician##

str1 = '/*Jon is @developer & musician!!'

import string

for i in str1:
    if i in string.punctuation:
        str1 = str1.replace(i, '#')

print(str1)
