#Exercise 5: Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element

#arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
#arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

#Expected Output:
#Addition of two arrays is
#[[20 39 33]
# [25 25 28]]
#Result array after calculating the square root of all elements
#[[ 400 1521 1089]
# [ 625  625  784]]

import numpy as np

arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

print("Addition of two arrays is")
res_add = arrayOne + arrayTwo
print(res_add)

print("Result array after calculating the square root of all elements")
res_sqr = res_add**2
print(res_sqr)
