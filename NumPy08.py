#Exercise 8: Print max from axis 0 and min from axis 1 from the following 2-D array.

#sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

#Expected Output:
#Printing Original array
#[[34 43 73]
# [82 22 12]
# [53 94 66]]
#Printing amin Of Axis 1
#[34 12 53]
#Printing amax Of Axis 0
#[82 94 73]

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print("Printing Original array")
print(sampleArray)

print("Printing amin Of Axis 1")
print(sampleArray.min(axis=1))

print("Printing amax Of Axis 0")
print(sampleArray.max(axis=0))
