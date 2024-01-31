#Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot
#Also, add a grid in the plot. gridline style should “--“

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x = df['month_number']
y = df['toothpaste']
plt.scatter(x, y, label='Toothpaste Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Numbers of units sold')
plt.title('Toothpaste Sales Data')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--')
plt.show()
