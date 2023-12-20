#Exercise 3: Following is the provided numPy array. Return array of items by taking the third column from all rows

#sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

#Expected Output:
#Printing Input Array
#[[11 22 33]
# [44 55 66]
# [77 88 99]]
#Printing array of items in the third column from all rows
#[33 66 99]

import numpy as np

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print("Printing Input Array")
print(sampleArray)
print("Printing array of items in the third column from all rows")
print(sampleArray[:, 2])
