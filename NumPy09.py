#Exercise 9: Delete the second column from a given array and insert the following new column in its place.

#sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
#newColumn = numpy.array([[10,10,10]])

#Expected Output:
#Printing Original array
#[[34 43 73]
# [82 22 12]
# [53 94 66]]
#Array after deleting column 2 on axis 1
#[[34 73]
# [82 12]
# [53 66]]
#Array after inserting column 2 on axis 1
#[[34 10 73]
# [82 10 12]
# [53 10 66]]

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])

print("Printing Original array")
print(sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = np.delete(sampleArray, 1, axis=1) # 1 es el índice de la columna a eliminar. La función numpy.delete() permite eliminar elementos a lo largo de un eje específico.
print(sampleArray)

print("Array after inserting column 2 on axis 1")
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1) # 1 es el índice de la posición de inserción.
print(sampleArray)
