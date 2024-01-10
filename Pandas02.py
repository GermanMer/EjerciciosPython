#Exercise 2: Clean the dataset and update the CSV file

#Replace all column values which contain ?, n.a, or NaN.

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

df = df.dropna()

df.to_csv("Automobile_data.csv")
