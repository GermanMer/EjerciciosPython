#Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart
#Note: In Pie chart display Number of units sold per year for each product in percentage.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

categorias = ["Facecream", "Facewash", "Toothpaste", "Bathingsoap", "Shampoo", "Moisturizer"]

valores = [
df["facecream"].sum(),
df["facewash"].sum(),
df["toothpaste"].sum(),
df["bathingsoap"].sum(),
df["shampoo"].sum(),
df["moisturizer"].sum()]

plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Sales Data')
plt.legend(loc='lower right')
plt.show()
