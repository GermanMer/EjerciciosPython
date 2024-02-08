#Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

y1 = df['bathingsoap']
x = df['month_number']
y2 = df['facewash']

# Crear una figura con dos subplots
fig, axs = plt.subplots(2, 1)

# Primer subplot: Sales data of Bathingsoap
axs[0].plot(x, y1, marker='o', linewidth=3, color='black')
axs[0].set_xlabel('Month Number')
axs[0].set_ylabel('Sales unit in number')
axs[0].set_title('Sales data of Bathingsoap')
axs[0].set_xticks(df['month_number'])

# Segundo subplot: Sales data of Facewash
axs[1].plot(x, y2, marker='o', linewidth=3, color='red')
axs[1].set_xlabel('Month Number')
axs[1].set_ylabel('Sales unit in number')
axs[1].set_title('Sales data of Facewash')
axs[1].set_xticks(df['month_number'])

# Ajustar el diseño y mostrar la figura
plt.tight_layout()
plt.show()
