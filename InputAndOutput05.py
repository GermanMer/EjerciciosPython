#Exercise 5: Accept a list of 5 float numbers as an input from the user
#Expected Output: [78.6, 78.6, 85.3, 1.2, 3.5]

numbers = []
for i in range(5):
    number = input('Enter a number:')
    numbers.append(float(number))
print(numbers)
