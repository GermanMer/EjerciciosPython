#Exercise 17: Find the sum of the series upto n terms

#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

#Given:
#number of terms: n = 5

#Expected output: 24690

t = 5

n = '2'

l = [2]

for i in range(1, t):
    n = n + '2'
    l.append(int(n))

print(sum(l))
