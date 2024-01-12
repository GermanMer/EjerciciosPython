#Exercise 4: Print All Toyota Cars details

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df = df [df.company=="toyota"]
df
