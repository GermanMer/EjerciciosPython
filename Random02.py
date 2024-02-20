#Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random

numbers = []

for i in range(100):
    numbers.append(random.randint(1000000000, 9999999999))

winners = random.sample(numbers, 2)

print(winners)
