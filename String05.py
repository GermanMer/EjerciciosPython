#Exercise 5: Count all letters, digits, and special symbols from a given string

#Given:
#str1 = "P@#yn26at^&i5ve"

#Expected Outcome:
#Total counts of chars, digits, and symbols
#Chars = 8
#Digits = 3
#Symbol = 4

str1 = "P@#yn26at^&i5ve"

chars = []
digits = []
symbol = []

for i in str1[::1]:
    if i.isalpha():
        chars.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        symbol.append(i)

print('Total counts of chars, digits, and symbols:')
print('Chars =', len(chars))
print('Digits =', len(digits))
print('Symbol =', len(symbol))
