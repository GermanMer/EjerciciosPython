#Exercise 2: Get total profit of all months and show line plot with the following Style properties

#Generated line plot must include following Style properties:
#Line Style dotted and Line-color should be red
#Show legend at the lower right location.
#X label name = Month Number
#Y label name = Total profit
#Add a circle marker.
#Line marker color as read
#Line width should be 3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x = df['month_number']
y = df['total_profit']
plt.plot(x, y, label = 'Profit data of last year', marker='o', markerfacecolor='k', linestyle='--', linewidth=3, color='r')
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Company Sales data of last year')
plt.legend(loc='lower right')
plt.show()
