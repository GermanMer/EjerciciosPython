#Exercise 12: Calculate income tax for the given income by adhering to the below rules

#Taxable Income     Rate (in %)
#First $10,000      0
#Next $10,000       10
#The remaining      20

#Expected Output:
#For example, suppose the taxable income is 45000 the income tax payable is 10000*0% + 10000*10%  + 25000*20% = $6000.

income = 45000

if income <= 10000:
    tax = 0
elif income > 10000 and income <= 20000:
    tax = (income - 10000) * 0.1
else:
    tax = (10000 * 0.1) + ((income - 20000) * 0.2)

print('Tax is: $' + str(tax))
