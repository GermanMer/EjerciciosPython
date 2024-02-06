#Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

data = df['total_profit']
bins = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(data, bins=bins, label='Profit data')
plt.xlabel('Profit range in dollar')
plt.ylabel('Actual profit in dollar')
plt.xticks(bins)
plt.title('Profit data')
plt.legend(loc='upper left')
plt.show()
