#Exercise 1: Read Total profit of all months and show it using a line plot

#Total profit data provided for each month. Generated line plot must include the following properties:
#X label name = Month Number
#Y label name = Total profit

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
x = df['month_number']
y = df['total_profit']
plt.plot(x, y)
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Company profit per month')
plt.show()
