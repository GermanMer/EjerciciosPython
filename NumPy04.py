#Exercise 4: Return array of odd rows and even columns from below numpy array

#sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
#[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

#Expected Output:
#Printing Input Array
#[[ 3  6  9 12]
# [15 18 21 24]
# [27 30 33 36]
# [39 42 45 48]
# [51 54 57 60]]
#Printing array of odd rows and even columns
#[[ 6 12]
# [30 36]
# [54 60]]

import numpy as np

sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print("Printing Input Array")
print(sampleArray)
print("Printing array of odd rows and even columns")
print(sampleArray[0:5:2, 1:4:2])
