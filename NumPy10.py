#Exercise 10: Create two 2-D arrays and Plot them using matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Crear dos matrices 2-D
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Trazar las matrices
plt.subplot(1, 2, 1)  # Subgráfico 1
plt.imshow(matrix1, cmap='viridis', interpolation='none')
plt.title('Matrix 1')

plt.subplot(1, 2, 2)  # Subgráfico 2
plt.imshow(matrix2, cmap='plasma', interpolation='none')
plt.title('Matrix 2')

# Mostrar el gráfico
plt.show()
