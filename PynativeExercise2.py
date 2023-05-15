# Exercise 2: Print the sum of the current number and the previous number.
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

print('Printing current and previous number sum in a range(10)')

previousnumber = 0

for n in range (0, 10):
    suma = previousnumber + n

    print('Current Number', n, 'Previous Number', previousnumber, 'sum:', suma)

    previousnumber = n
