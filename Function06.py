#Exercise 6: Create a recursive function

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

#A recursive function is a function that calls itself again and again.

#Expected Output: 55

def recursive(x, y):
    r = x + y
    x = r
    if y > 1:
        recursive(x, y - 1)
    else:
        print(r)

recursive(0, 10)
