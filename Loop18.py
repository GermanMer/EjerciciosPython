#Exercise 18: Print the following pattern

#Write a program to print the following start pattern using the for loop
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

for i in range(6):
    for j in range(0, i):
        print('*', end=" ")
    print("")
for k in range(5):
    for l in range(0, 4 - k):
        print('*', end=" ")
    print("")
