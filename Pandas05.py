#Exercise 5: Count total cars per company

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df['company'].value_counts()
