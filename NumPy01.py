#Exercise 1: Create a 4X2 integer array and Prints its attributes
#Note: The element must be a type of unsigned int16. And print the following Attributes: –
#The shape of an array.
#Array dimensions.
#The Length of each element of the array in bytes.

#Expected Output:
#Printing Array
#[[64392 31655]
#[32579     0]
#[49248   462]
#[    0     0]]

#Printing NumPy array Attributes
#Array Shape is:  (4, 2)
#Array dimensions are  2
#Length of each element of array in bytes is  2

import numpy

sample_array = numpy.empty([4,2], dtype = numpy.uint16)
print("Printing Array")
print(sample_array)
print("")
print("Printing NumPy array Attributes")
print("Array Shape is:", sample_array.shape)
print("Array dimensions are:", sample_array.ndim)
print("Length of each element of array in bytes is:", sample_array.itemsize)
