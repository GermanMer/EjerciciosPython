#Exercise 1: From the given dataset print the first and last five rows

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

print("first 5 rows")
df.head()
print("last 5 rows")
df.tail()
