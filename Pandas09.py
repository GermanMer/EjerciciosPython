#Exercise 9: Concatenate two data frames using the following conditions

#Create two data frames using the following two dictionaries.
#GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
#japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

import pandas as pd
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
dfGER = pd.DataFrame(GermanCars)
dfJAP = pd.DataFrame(japaneseCars)
pd.concat([dfGER, dfJAP], keys=['Germany', 'Japan'])
