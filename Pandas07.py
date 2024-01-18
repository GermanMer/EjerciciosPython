#Exercise 7: Find the average mileage of each car making company

car_Manufacturers = df.groupby('company')
AVGmileageDf = car_Manufacturers[['average-mileage']].mean()
AVGmileageDf
