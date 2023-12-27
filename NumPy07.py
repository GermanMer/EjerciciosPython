#Exercise 7: Sort following NumPy array
#Case 1: Sort array by the second row
#Case 2: Sort the array by the second column
#sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

#Expected Output:
#Printing Original array
#[[34 43 73]
# [82 22 12]
# [53 94 66]]
#Sorting Original array by second row
#[[73 43 34]
# [12 22 82]
# [66 94 53]]
#Sorting Original array by second column
#[[82 22 12]
# [34 43 73]
# [53 94 66]]

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print("Printing Original array")
print(sampleArray)
print("Printing Original array sorted - Not required")
sorted_arr = np.sort(sampleArray)
print(sorted_arr)
print("Sorting Original array by second row")
indices_fila2 = np.argsort(sampleArray[1, :])
sorted_arr_fila2 = sampleArray[:, indices_fila2]
print(sorted_arr_fila2)
print("Sorting Original array by second column")
indices_col2 = np.argsort(sampleArray[:, 1])
sorted_arr_col2 = sampleArray[indices_col2, :]
print(sorted_arr_col2)
