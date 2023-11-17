#Exercise 9: Counts the number of occurrences of item 50 from a tuple

#Given:
#tuple1 = (50, 10, 60, 70, 50)

#Expected output:
#2

tuple1 = (50, 10, 60, 70, 50)

contador = 0

for i in tuple1:
    if i == 50:
        contador = contador + 1
    else: continue

print(contador)
