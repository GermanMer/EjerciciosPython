#Exercise 6: Find each company’s Higesht price car

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers[['company','price']].max()
priceDf
