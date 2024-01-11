#Exercise 3: Find the most expensive car company name

#Print most expensive car’s company name and price.

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
df3 = df [['company','price']][df.price==df['price'].max()]
print(df3)
