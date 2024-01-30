#Exercise 3: Read all product sales data and show it  using a multiline plot
#Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x = df['month_number']
y1 = df['facecream']
y2 = df['facewash']
y3 = df['toothpaste']
y4 = df['bathingsoap']
y5 = df['shampoo']
y6 = df['moisturizer']

plt.plot(x, y1, label='Facecream Sales Data', color='c', linestyle='-', linewidth=3, marker='o')
plt.plot(x, y2, label='Facewash Sales Data', color='orange', linestyle='-', linewidth=3, marker='o')
plt.plot(x, y3, label='Toothpaste Sales Data', color='g', linestyle='-', linewidth=3, marker='o')
plt.plot(x, y4, label='Bathingsoap Sales Data', color='r', linestyle='-', linewidth=3, marker='o')
plt.plot(x, y5, label='Shampoo Sales Data', color='purple', linestyle='-', linewidth=3, marker='o')
plt.plot(x, y6, label='Moisturizer Sales Data', color='brown', linestyle='-', linewidth=3, marker='o')
plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Sales Data')
plt.legend(loc='upper left')
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.show()
