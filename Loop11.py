#Exercise 11: Write a program to display all prime numbers within a range
#Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

#Examples:
#6 is not a prime mumber because it can be made by 2×3 = 6
#37 is a prime number because no other whole numbers multiply together to make it.

#Given:
#range:
#start = 25
#end = 50

#Expected output:
#Prime numbers between 25 and 50 are:
#29
#31
#37
#41
#43
#47

start = input('Enter the range start:')
end = input('Enter the range end:')

number_range = []
not_prime = []
prime = []

for x in range(int(start), int(end)+1, 1):
     number_range.append(x)

for i in number_range:
    for j in range(2, i, 1):
        if i % j == 0: not_prime.append(i)
        else: continue

#print(number_range)
#print(not_prime)

for r in number_range:
    if r not in not_prime:
        prime.append(r)
    else: continue

for p in prime:
    print(p)
